from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

from typing_extensions import TypedDict


class TransactioBase(BaseModel):
    pass


class CreateTransaction(TransactioBase):
    valor: int = Field(gt=0)
    tipo: str = Field(
        ..., description="O campo 'tipo' deve ser 'c' ou 'd'", pattern="^[cd]$"
    )
    descricao: str = Field(..., min_length=1, max_length=10)


class Transaction(TransactioBase):
    limite: int
    saldo: int

    class Config:
        orm_mode = True


class Balance(TypedDict):
    total: int
    data_extrato: datetime
    limite: int


class LastTransactions(TypedDict):
    valor: int
    tipo: str
    descricao: str
    realizada_em: datetime


class Client(BaseModel):
    saldo: Balance
    ultimas_transacoes: list[LastTransactions]
