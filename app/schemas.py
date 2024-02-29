from pydantic import BaseModel, TypeAdapter
from typing import List

from typing_extensions import TypedDict


class TransactioBase(BaseModel):
    pass


class CreateTransaction(TransactioBase):
    valor: int
    tipo: str
    descricao: str


class Transaction(TransactioBase):
    linite: int
    saldo: int

    class Config:
        orm_mode = True


class Balance(TypedDict):
    total: int
    data_extrato: str
    limite: int


class LastTransactions(TypedDict):
    valor: int
    tipo: str
    descricao: str
    realizada_em: str


class Client(BaseModel):
    saldo: Balance
    ultimas_transacoes: list[LastTransactions]
