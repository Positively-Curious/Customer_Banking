# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account 

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    
    # Prompt the user to enter the savings accounts details 
    savings_account_number = input('Enter the savings account number: ')
    savings_account_holder_name = input ('Enter the savings account name: ')

    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input('Enter the savings account balance: '))
    savings_interest_rate = float(input('Enter the savings account interest rate (in decimal form): '))
    savings_maturity = int(input('Enter the number of months for the savings account: '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest earned on savings account: ${interest_earned:.2f}")
    print(f"Updated savings account balance with interest earned: ${updated_savings_balance:.2f}")

    # Prompt the user to enter the CD accounts details:
    CD_account_number = input('Enter the savings account number: ')
    CD_account_holder_name = input ('Enter the savings account name: ')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    CD_balance = float(input('Enter the CD account balance: '))
    CD_interest_rate = float(input('Enter the CD account interest rate (in decimal form): '))
    CD_maturity = int(input('Enter the number of months for the CD account: '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_CD_balance, interest_earned = create_cd_account(CD_balance, CD_interest_rate, CD_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Interest earned on CD account: ${interest_earned:.2f}")
    print(f"Updated CD account balance with interest earned: ${updated_CD_balance:.2f}")

    # Call the main function.
    if __name__ == "main__":
        main()
