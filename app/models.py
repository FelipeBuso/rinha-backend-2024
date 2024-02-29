from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Client(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    limite = Column(Integer, default=0)
    saldo = Column(Integer, default=0)

    f_transacoes = relationship("Transaction", back_populates="cliente")


class Transaction(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True)
    valor = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Client", back_populates="f_transacoes")
