🏧 ATM Simulator System

A Python-based ATM Simulator that mimics real-world banking operations such as account login, balance inquiry, deposit, and withdrawal. This project demonstrates core programming concepts like object-oriented design, file handling, and user interaction.

---

🚀 Features

* User authentication (PIN-based login)
* Balance inquiry
* Cash deposit functionality
* Cash withdrawal with validation
* Transaction handling with basic error checks
* Simple and interactive command-line interface

---

🛠️ Tech Stack

* **Language:** Python
* **Concepts Used:** OOP (Object-Oriented Programming), File Handling, Conditionals, Loops

---

📂 Project Structure
ATM-Simulator/
│── atm.py
│── users.txt (or data file if used)
│── README.md

---

▶️ How to Run

1. Clone the Repository

```
git clone https://github.com/akashshinde-dev/ATM-Simulator
```

2. Navigate to Project Folder

```
cd ATM-Simulator
```

3. Run the Program

```
python atm.py
```

---

💡 How It Works

* User logs in using a PIN
* System verifies credentials
* After login, user can:

  * Check balance
  * Deposit money
  * Withdraw money
* Updates are reflected immediately

---

📊 Example Operations

* Login with PIN
* Select operation (Deposit / Withdraw / Check Balance)
* Enter amount
* View updated balance

---

⚠️ Disclaimer
This is a simulation project for educational purposes only. It does not connect to real banking systems or handle real transactions.

---

🔧 Future Improvements

* Add GUI using Tkinter or PyQt
* Implement database (SQLite/MySQL) instead of file storage
* Add transaction history feature
* Improve authentication system (multiple users, encryption)
* Add card number & OTP verification

---

👨‍💻 Author
**Akash Shinde**
GitHub: https://github.com/akashshinde-dev

---

✅ Copy and paste this directly into your README.md — it's clean and recruiter-ready.
2. Clone this repository:
```bash
   git clone <repo-url>
   cd <repo-folder>
````

3. Run the ATM simulator:

```bash
   python atm_simulator.py
```


## Usage

* `Deposit` : Add money to your account
* `Withdraw` : Withdraw money (minimum $100 balance required)
* `seetrans` : See past transactions
* `changeinfo` : Placeholder for changing account info (future feature)
* `delaccount` : Placeholder for deleting account (future feature)
* `quit` : Exit the program

---

## File Structure

* `atm_simulator.py` → Main program file
* `account-transactions.csv` → Stores all transactions
* `atm-simulation.log` → Logs user activity and errors

---

## Version

* v1: First GitHub release with basic ATM functionality (deposit, withdraw, transaction log)
* v2 (planned): Structure for account features, logging, and CSV storage

---

## Notes

* Minimum balance of $100 is required to withdraw money.
* Currently, `changeinfo` and `delaccount` are placeholders for future features.
* Logging helps track user activity and errors for debugging.

---

## Author

Your Name
GitHub: [akashshinde-dev](https://github.com/akashshinde-dev)
