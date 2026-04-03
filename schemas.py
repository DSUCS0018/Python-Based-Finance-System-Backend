from pydantic import BaseModel
from datetime import date

class UserBase(BaseModel):
    name: str
    role: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    amount: float
    transaction_type: str
    category: str
    date: date
    notes: str
    user_id: int

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        orm_mode = True