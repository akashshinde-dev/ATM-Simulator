

# ATM Simulator (Python CLI Project)

## Description
This is a simple **ATM simulation system** built using Python.  
It allows users to deposit, withdraw, and view transaction history via a command-line interface (CLI).  
All transactions are logged and stored in a CSV file for record-keeping.

---

## Features
- Password-protected login
- Deposit and Withdraw money
- Transaction history stored in CSV
- Logging of user actions for debugging
- Planned future features:  
  - Change account info (with OTP verification)  
  - Delete account permanently  

---

can this fine 
## How to Run
1. Make sure you have Python installed (Python 3.8+ recommended)
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

