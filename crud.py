from sqlalchemy.orm import Session
import models
import schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        amount=transaction.amount,
        transaction_type=transaction.transaction_type,
        category=transaction.category,
        date=transaction.date,
        notes=transaction.notes,
        user_id=transaction.user_id
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(db: Session):
    return db.query(models.Transaction).all()


def filter_transactions(db: Session, category: str = None, transaction_type: str = None):
    query = db.query(models.Transaction)

    if category:
        query = query.filter(models.Transaction.category == category)

    if transaction_type:
        query = query.filter(models.Transaction.transaction_type == transaction_type)

    return query.all()

def get_summary(db: Session):
    transactions = db.query(models.Transaction).all()

    total_income = sum(t.amount for t in transactions if t.transaction_type == "income")
    total_expense = sum(t.amount for t in transactions if t.transaction_type == "expense")

    balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }

def delete_transaction(db: Session, transaction_id: int):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    if transaction:
        db.delete(transaction)
        db.commit()
    return transaction

def update_transaction(db: Session, transaction_id: int, updated_data: schemas.TransactionCreate):
    transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()
    
    if transaction:
        transaction.amount = updated_data.amount
        transaction.transaction_type = updated_data.transaction_type
        transaction.category = updated_data.category
        transaction.date = updated_data.date
        transaction.notes = updated_data.notes
        db.commit()
        db.refresh(transaction)
    
    return transaction