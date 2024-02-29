from fastapi import FastAPI, Depends
from .database import SessionLocal
from .schemas import Client, CreateTransaction, Transaction
from sqlalchemy.orm import Session
from .services import create_transaction, get_transactions

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/clientes/{id}/transacoes", response_model=Transaction)
def create(id: int, transaction: CreateTransaction, db: Session = Depends(get_db)):
    return create_transaction(client_id=id, transaction=transaction, db=db)


@app.get("/clientes/{id}/extrato", response_model=Client)
def get(id: int, db: Session = Depends(get_db)):
    return get_transactions(id, db)
