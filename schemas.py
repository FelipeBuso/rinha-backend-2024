from pydantic import BaseModel


class ClientBase(BaseModel):
    nome: str
    limite: int
    saldo: int | None = None


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True


class TraqnsactionBase(BaseModel):
    valor: int
    tipo: str
    descricao: str


class TraqnsactionCreate(TraqnsactionBase):
    pass


class Traqnsaction(TraqnsactionBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True
