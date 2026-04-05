# Python Finance Tracker Backend

## Overview
This project is a backend system built using FastAPI to manage and analyze financial records. It allows users to create, view, update, and delete transactions, apply filters, and generate financial summaries.

---

## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

---

## Features

### 1. User Management
- Create user
- View users
- Role-based structure (admin, analyst, viewer)

---

### 2. Transaction Management
- Create transactions (income/expense)
- View transactions
- Update transactions
- Delete transactions

---

### 3. Filtering
- Filter by category
- Filter by transaction type
- Filter by date range

---

### 4. Financial Summary
- Total income
- Total expense
- Balance calculation

---

### 5. Role-Based Access Control
- Admin → full access (create, update, delete)
- Analyst → can update
- Viewer → read-only (cannot modify/delete)

---

### 6. Error Handling
- 404 for missing resources
- 403 for unauthorized actions
- Input validation using Pydantic

---

## API Endpoints

### Users
- POST /users/
- GET /users/

### Transactions
- POST /transactions/
- GET /transactions/
- PUT /transactions/{id}
- DELETE /transactions/{id}
- GET /transactions/filter/

### Summary
- GET /summary/

---

## How to Run

```bash
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload