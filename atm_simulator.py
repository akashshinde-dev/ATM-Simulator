# ATM simulator program 
import random
import os
import csv
import logging
from datetime import datetime


logging.basicConfig(
        filename="atm-simulation.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(pathname)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("obito")

password = random.randint(1,9999)
print(f"password : {password:04}")


account_money = float(random.randint(10000,50000))
account_bal = float(random.choice([0,account_money,100]))

try :
        passcode = int(input("Enter password : "))
except:
        logger.error("user enered worng password")
        ValueError

if passcode != password :
        logger.error("user enterd wrong password")
        raise ValueError("you entered worng password")

if account_bal <=100 :
        pass
        # create account 
        # withdraw not available
print(f"Your Account Balance is ${account_bal}")    # Show account balance to user 
logger.info("showing account balance")

all_trans = []
current_trans=[]

filename = "account-transactions.csv"

if os.path.exists(filename):

        logger.info("open transaction file ")

        with open (filename,"r",encoding="utf-8")as f:

                filesize = os.path.getsize(filename)

                if filesize > 0:
                        all_trans = list(csv.DictReader(f))

while True :

        # Get input for tansaction from user & save transacion in csv file
        
        if not account_bal:
                # creat account 
                pass

        user_input = input("\n_Enter Deposit for Deposit money \n_Enter Withdraw for Withdraw money \n_Enter seetrans for transactions \n_Enter Quit for stop program \n Enter Here : ")
        valid_inputs =["withdraw","deposit","seetrans","changeinfo","delaccount","quit"]

        if user_input not in valid_inputs:

                logger.warning("User inputed invalid value")
                print("You ented invalid value try again !! ")

        else:
                
                if user_input.lower().strip() == "withdraw":  # loop for withdraw money 
                        try:
                                withdraw=float(input("Enter amount : "))
                        except:
                                logger.error("invalid input by user")
                                ValueError
                                withdraw = 0
                        
                        if account_bal - withdraw >= 100: # minumum balance required for account
                                account_bal -= withdraw  #accouting money
                        else:
                                print("minimum 100$ requierd in account")


                        if withdraw > 0:  

                                print(f"Your Account Balance is ${account_bal}") 

                                current_trans.append({"type-trans":"withdraw","amount":withdraw,"Date":datetime.now().strftime("%d-%m-%Y"),"Total_balance":account_bal})
                                
                                logger.info(f"user inputed {withdraw} for withdraw money")

                
                
                elif user_input.lower().strip() == "deposit": # Loop for deposit money
                        try:
                                deposit=float(input("Enter amount : "))
                        except:
                                logger.error("invalid input by user")
                                ValueError
                                deposit = 0
                        
                        account_bal += deposit #accounting money  
                        
                        if deposit > 0:

                                print(f"Your Account Balance is ${account_bal}")

                                current_trans.append({"type-trans":"deposit","amount":deposit,"Date":datetime.now().strftime("%d-%m-%Y"),"Total_balance":account_bal})

                                logger.info(f"user inputed {deposit} for deposit money")


                elif user_input.lower().strip() == "seetrans":
                        
                        if os.path.getsize(filename)== 0:
                                print("_You did not had any transaction yet")
                                continue

                        all_data =all_trans+current_trans
                        print(len(all_data))

                        try:
                                line = int(input("Eentr num of line to see :"))
                        except:
                                ValueError
                                line = len(all_data)

                        if line == 0:
                                for t in all_data:
                                        trans = " - ".join(map(str,t.values()))
                                        print(trans)

                        elif line > 0:
                                for t in all_data[line-1:]:
                                        trans = " - ".join(map(str,t.values()))
                                        print(trans) 

                        logger.info("user transacions shows on screen")       
                elif user_input.lower().strip() == "changeinfo":
                        # change account details
                        pass
                elif user_input.lower().strip() == "delaccount":
                        # delete account permanently
                        pass
                elif user_input.lower().strip() == "quit":
                        logger.info("user quited ATM ")
                        break
              
                else:
                        print("Server is bussy try after 5 minutes")
                        break

with open(filename,"a",encoding="utf-8",newline="")as f:

        fieldnames = ["type-trans","amount","Date","Total_balance"]

        writer = csv.DictWriter(f,fieldnames=fieldnames)

        if os.path.getsize(filename) == 0:
                writer.writeheader()

        if len(current_trans) > 0:
                
                writer.writerows(current_trans)
print("Your all transactions saved successfuly")
logger.info(f"script ended successfuly and new {len(current_trans)} are saved in {filename}")
                 