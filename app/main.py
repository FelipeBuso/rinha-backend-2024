from fastapi import FastAPI, Depends
from .database import SessionLocal
from .schemas import Client, CreateTransaction
from sqlalchemy.orm import Session
from .services import create_transaction

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


@app.post("/clientes/{id}/transacoes", response_model=Client)
def creat_transaction(
    id: int, transaction: CreateTransaction, db: Session = Depends(get_db)
):
    return create_transaction(client_id=id, transaction=transaction, db=db)
