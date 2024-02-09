from sqlalchemy.orm import Session
import models, schemas


def get_client(db: Session, client_name: str):
    return db.query(models.Client).filter(models.Client.nome == client_name).first()


def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(nome=client.nome, limite=client.limite, saldo=0)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client
