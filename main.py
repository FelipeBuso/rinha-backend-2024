from typing import Union
from fastapi import FastAPI, HTTPException, Depends
from service import create_client, get_client
import schemas, models
from sqlalchemy.orm import Session

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post("/client/", response_model=schemas.Client)
def create_client_db(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    exist_client = get_client(client_name=client.nome, db=db)
    print("exist_client", exist_client)
    if exist_client:
        raise HTTPException(status_code=400, detail="Cliente já cadastrado")
    return create_client(client=client, db=db)
