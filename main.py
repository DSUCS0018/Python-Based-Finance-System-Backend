from fastapi import FastAPI
from database import engine, Base
import models
from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas
from fastapi import HTTPException

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Finance Tracker API is running"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.get("/users/", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post("/transactions/", response_model=schemas.TransactionResponse)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, transaction)


@app.get("/transactions/", response_model=list[schemas.TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@app.get("/transactions/filter/")
def filter_transactions(
    category: str = None,
    transaction_type: str = None,
    db: Session = Depends(get_db)
):
    return crud.filter_transactions(db, category, transaction_type)

@app.get("/summary/")
def get_summary(db: Session = Depends(get_db)):
    return crud.get_summary(db)

@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = crud.delete_transaction(db, transaction_id)
    
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    return {"message": "Transaction deleted successfully"}



@app.put("/transactions/{transaction_id}")
def update_transaction(transaction_id: int, updated_data: schemas.TransactionCreate, db: Session = Depends(get_db)):
    transaction = crud.update_transaction(db, transaction_id, updated_data)
    
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    return transaction