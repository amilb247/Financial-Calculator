import math

# Step1: I need two statements explaining the definition of "bond" and "investment"

# Step2: I need to use input boxes that seperate into two if statments depending on user input

# Step3 All user input must be casted to an integer and stored in a variable.

# Step4: Use the varibles to exceute the necessary math operations and print final answer.
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

user_finance_options = input(
    "Enter either 'investment' or 'bond' from the menu above to proceed: "
).lower()
# An input box that will allow the user to choose a bond or investment this will turn any input to lowercase
if user_finance_options == "investment":
    deposit_amount = int(input("Enter the amount you are depositing: "))
    interest_rate = float(input("Enter the interest rate: ").strip("%"))
    years_of_investment = int(input("Enter the number of years for investment: "))
    interest_type = input(
        "Enter 'simple' or 'compound' to select your interest type: "
    ).lower()

    simple_interest_amount = int(
        deposit_amount * (1 + interest_rate / 100 * years_of_investment)
    )
    # Ensure all () are in the right place for all math operator calcualtions

    simple_interest_amount = format(simple_interest_amount, ".2f")
    """ Using the format function I set the answer to two deciamls places preventing it from reoccuring as this would be the incorrect display for currency."""
    print(f"Simple Interest Total: £{simple_interest_amount}")

    compound_interest_amount = int(
        deposit_amount * math.pow((1 + interest_rate / 100), years_of_investment)
    )

    compound_interest_amount = format(compound_interest_amount, ".2f")

    print(f"Compound Interest Total: £{compound_interest_amount}")

# This if statement will be printed when the user chooses "bond" in the "user_finance_options" input
if user_finance_options == "bond":
    house_value = int(input("Enter the value of your house: "))
    annual_interest = int(input("Enter the interest rate: ").strip("%"))
    months_of_repayment = int(input("Enter the number of months for repayment: "))

    monthly_interest = (annual_interest / 100) / 12

    monthly_bond_payment = float(
        (monthly_interest * house_value)
        / (1 - (1 + monthly_interest) ** (-months_of_repayment))
    )

    monthly_bond_payment = format(monthly_bond_payment, ".2f")

    print(f"Bond Monthly Installments: £{monthly_bond_payment}")
