# 💰 Challenge: Banking System with Object-Oriented Programming (OOP)

This project is a complete solution to a challenge focused on **designing a banking system** using **Object-Oriented Programming** principles in Python. The system simulates banking operations such as creating clients and accounts, depositing, withdrawing, and viewing transaction history.

---

## ✅ Objectives Achieved

- [x] Full implementation of a banking system using classes and objects.
- [x] Application of the 4 pillars of OOP:
  - **Encapsulation**
  - **Abstraction**
  - **Inheritance**
  - **Polymorphism**
- [x] Classes designed according to the provided UML diagram:
  - `Cliente` (abstract representation of users)
  - `PessoaFisica` (inherits from Cliente)
  - `Conta` (base class for accounts)
  - `ContaCorrente` (inherits from Conta)
  - `Historico` (tracks transactions)
  - `Transacao` (abstract class)
  - `Saque` and `Deposito` (inherit from Transacao)
- [x] CPF validation and duplicate checking
- [x] Support for multiple accounts per customer
- [x] Input validation for numeric fields using `try/except`
- [x] Clean output formatting with `__str__()` in key classes

---

## 💡 System Features

- Register users with CPF, name, birth date, and address
- Create accounts linked to users
- Choose from multiple accounts per client
- Perform **deposits** and **withdrawals**
- Generate **transaction history** (statement) showing date, type, and value
- List all registered accounts
- Clear and user-friendly error/success messages

---

## 📚 Key Learnings

This project reinforced several important concepts:

- Structuring code using object-oriented programming
- Using `@property` to protect sensitive attributes
- Reusability and separation of responsibilities
- Good practices like input validation, modularization, and DRY code

---

## 📁 Structure

This project is written in a single `.py` file for simplicity and ease of testing.

---

✅ Designed as a learning challenge to solidify Python fundamentals related to data structures, function design, and user interaction.