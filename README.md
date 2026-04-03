# Python Finance Tracker Backend

## Overview
This project is a backend system built using FastAPI to manage and analyze financial records. It allows users to create, view, and manage transactions while also providing useful financial summaries.

## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

## Features

### 1. User Management
- Create user
- View users
- Role-based structure (viewer, analyst, admin)

### 2. Transaction Management
- Create transactions (income/expense)
- View transactions
- Filter transactions by category and type
- Delete transactions

### 3. Financial Summary
- Total income
- Total expense
- Balance calculation

### 4. API Endpoints
- POST /users/
- GET /users/
- POST /transactions/
- GET /transactions/
- GET /transactions/filter/
- DELETE /transactions/{transaction_id}
- GET /summary/

## How to Run

```bash
pip install fastapi uvicorn sqlalchemy
python -m uvicorn main:app --reload