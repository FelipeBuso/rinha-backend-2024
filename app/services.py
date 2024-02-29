from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import Transaction, Client
from .schemas import CreateTransaction
from sqlalchemy import text
from datetime import datetime


def create_transaction(client_id: int, transaction: CreateTransaction, db: Session):

    client = db.query(Client).filter(Client.id == client_id).with_for_update().first()

    valor = transaction.valor if transaction.tipo == "c" else transaction.valor * -1

    if transaction.tipo == "d" and (client.limite * -1 > client.saldo + valor):
        raise HTTPException(status_code=422, detail="Limite insuficiente")

    create_transaction = Transaction(
        valor=valor,
        tipo=transaction.tipo,
        descricao=transaction.descricao,
        client_id=client_id,
    )

    update_client = text("UPDATE clientes SET saldo = :new_saldo WHERE id = :client_id")
    try:
        db.add(create_transaction)
        db.execute(
            update_client, {"client_id": client_id, "new_saldo": client.saldo + valor}
        )
        db.commit()
        db.refresh(client)
        return {"limite": client.limite, "saldo": client.saldo}
    except Exception:
        db.rollback()
        return


def get_transactions(client_id: int, db: Session):
    client = db.query(Client).filter(Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente não localizado")

    transactions = (
        db.query(
            Transaction.valor,
            Transaction.tipo,
            Transaction.descricao,
            Transaction.realizada_em,
        )
        .filter(Transaction.client_id == client_id)
        .order_by(Transaction.realizada_em.desc())
        .limit(10)
        .all()
    )

    return {
        "saldo": {
            "total": client.saldo,
            "data_extrato": datetime.now(),
            "limite": client.limite,
        },
        "ultimas_transacoes": [row._asdict() for row in transactions],
    }
