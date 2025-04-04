# 💻 Simple Banking System (Python Project)
This project is a simple banking system built using Python with a procedural approach. It allows users to perform essential banking operations such as deposits, withdrawals, viewing account statements, user registration, and account creation.

---

## ✅ Features

### 💰 Deposit
- Accepts **positional-only** arguments.
- Only accepts positive values.
- Updates balance and transaction history.

### 💸 Withdrawal
- Accepts **keyword-only** arguments.
- Checks for:
  - Balance availability
  - Withdrawal limit per operation
  - Maximum daily number of withdrawals
- Updates balance, history, and withdrawal count.

### 📄 Statement (Extrato)
- Shows all transactions and current balance.
- Accepts:
  - Balance as **positional-only**
  - History as **keyword-only**

### 👤 User Registration
- Registers users with:
  - Full name
  - Date of birth
  - CPF (Brazilian ID number)
  - Address
- Prevents duplicate CPFs.

### 🏦 Bank Account Creation
- Accounts have:
  - Fixed agency number: `0001`
  - Sequential account number
  - Linked to a previously registered user

### 📋 List Accounts
- Lists all created accounts with holder and account details.

---

## 🧠 Concepts Applied

- **Function parameters**: positional-only `/`, keyword-only `*`, and mixed
- Use of **lists and dictionaries** to manage users and accounts
- CPF lookup using `next()` and generator expressions
- **Interactive menu** with `while True`
- Clear function separation for readability and reuse

---

## 📁 Structure

This project is written in a single `.py` file for simplicity and ease of testing.

---

✅ Designed as a learning challenge to solidify Python fundamentals related to data structures, function design, and user interaction.