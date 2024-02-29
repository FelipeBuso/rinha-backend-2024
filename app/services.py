from sqlalchemy.orm import Session
from .models import Transaction, Client
from .schemas import CreateTransaction


def create_transaction(client_id: int, transaction: CreateTransaction, db: Session):
    return db.query(Client).filter(Client.id == client_id).with_for_update().first()
