# Module 3 Challenge - Creating a customer banking system that allows users to calculate and 
# track interest earned.
#
# Source Code - XPert Learning Assistant from: 
# https://bootcampspot.instructure.com/courses/6302/external_tools/313.

# The starter files consist of the following files: Accounts.py, savings_account.py, 
# cd_account.py, and customer_banking.py. The Accounts.py file contains the Account class with 
# methods to set the balance and interest.
# 
# IN THE savings account savings_account.py file: 
#
# Line 2: Import the Account class from the Accounts.py file.
# 
# Lines 5 to 16: The function definition for the Savings Account is already given by the syntax # # Args that defines the variable arguments of balance, interest rate and month, in values of 
# decimal places ("floats") and for months as whole numbers without decimal places (integers 
# "int"), respectively, that must be passed ("Argued") through codes, in order to output results # ("Returns") of decimal values ("Floats"), for the updated savings account balance after adding # the interest earned, and also returning the float value of the interest earned: 
# Args:
#   balance (float): The initial savings account balance.
#   interest_rate (float): The APR interest rate for the savings account.
#   months (int): The length of months to determine the amount of interest.
# Returns:
#   Float: 
#   The updated savings account balance after adding the interest earned;
#   And returns the interest earned.
# 
# Line 18: Based on the definition of the savings account by the arguments (what you need) and 
# returns (results) required, using the import of the Account Class which contains the accounts 
# attributes and methods of calculations for balance, interest rates and months, create an 
# instance of the savings account, i.e., an event to address the arguments and achieve the
# Returns (results/output) as defined.  
# 
# Line 20: Interest is "set" at "0" value to ensures the interest on the balances and the updated # balance are correctly calculated.
# 
# Hence:   
# 
# Line 23: Calculate the interest earned.
# 
# Line 26: Update the savings account balance by adding interest earned. 
# 
# Line 29: I am updating the balance attribute of the SavingsAccount instance with the newly 
# calculated balance, which ensures that after changes are made, the correct balance is stored 
# and tracked in the instance of the SavingsAccount class.
# 
# Line 32: I am updating the interest attribute of the SavingsAccount instance with the newly 
# calculated interest earned, which ensures that after changes are made, the correct interest 
# earned is stored and tracked in the instance of the SavingsAccount class.
# 
# Line 35: The "return" of the "arguments" are achieved.
# 
# IN THE certificate of deposit(CD) CD_account.py file:
# Repeat the same steps in the same Lines used for the above mentioned savings file, using "CD" 
# in place of "savings".
# 
# IN THE customer_banking.py file:
#
# Lines 6 to 10: The account functions from the savings_account.py file and cd_account.py file 
# are imported into the customer_banking.py file to define arguments and returns(results) to:
# allow the user to enter the savings and cd account balance, interest rate, and the length of 
# months to determine the interest gained, and display the interest earned on the savings and CD # accounts and update the balances of the savings and CD accounts.  
#
# Lines 13 & 14 and 29 & 30: The user is prompted to enter savings and cd account details 
# (account number and name), respectively.
# 
# Lines (17, 18, 19) and (33, 34, 35): The user is prompted to input for each of the savings and # cd accounts, the initial balance, the interest # rate, and the number of months the account 
# will be held to maturity, respectively.
# 
# Lines 22 and 38: This code is instructing the program to create a CD and savings account 
# respectively, by using the account functions from the savings_account.py and cd_account.py 
# files imported into customer_banking.py # file, to put into effect, i.e.using the user provided # variables of balance, interest rate and months to maturity, as input parameters, to "call" the 
# create_savings_account function and create_cd_account function to create a savings and CD 
# account, respectively. 
# 
# Lines (25,26) and (41,42): this the function to print out the interest earned and updated 
# savings and CD account balance with interest earned for the given months, respectively. 
# 
# Line 45: To "Call the main function" is to activate the primary code to execute the "main" 
# function, i.e activating the main logic or entry point of the program in order for the program # to commence its main function.  