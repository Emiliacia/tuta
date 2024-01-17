#1.Creating variables as in the initial template:
import math

investment = "to calculate the amount of interest you'll earn on your investment"
bond = "to calculate the amount you'll have to pay on a home loan"

#Printing the variables.
print("investment" "-" + investment)
print("bond" "-" + bond)

#Preparing the program by defining which inputs are valid.
user_input = input("Enter bond or investment: ").lower()

#2.Asking the user to choose between investment and bond+ lower command to convert inputs hence readable_inputs variable.
readable_inputs = ["bond", "investment"]

#3. If the user selects 'investment' preparing the text to be readable:
readable_inputs = ["bond", "investment"]

if user_input in readable_inputs:
    print(user_input)
else:
    print("Error, choose between bond and investment: ")

#4. Preparing the next question in case the answer is investment.
if user_input == "investment":
    deposit = float(input("How much would you like to deposit: "))
    print("You want to deposit: ", deposit)

#5. Preparing the next answer regarding the interest rate.
    interest_rate = float(input("How much is the interest rate: "))
    print("Interest rate:", interest_rate)

#6. Preparing the next answer regarding the years of investment.
    years_deposit = float(input("For how many years: "))
    print("For years:",years_deposit)
    print("Deposit:", deposit)
    print("Interest rate:", interest_rate)
    print("Years of deposit:", years_deposit)
#7. Preparing the next question regarding the type of invesment 'simple or 'compound'.
    interest = input("What kind of interest: simple or compound: ")
    if interest == "simple":
#8. If simple folows the formula: A = P *(1 + r*t)
#‘r’ is the interest entered above divided by 100, e.g. if 8% is entered,
#then r is 0.08.
# ‘P’ is the amount that the user deposits.
# ‘t’ is the number of years that the money is being invested.
# ‘A’ is the total amount once the interest has been applied.
        total_amount_simple = deposit * (1 + (interest_rate /100) * years_deposit)
        print("With simple type of interest you will get: ", total_amount_simple)

#9. If compound follows the formula: A = P * math.pow((1+r),t)
    elif interest == "compound":
        total_amount_compound = deposit * (math.pow((1 + interest_rate/100) ,years_deposit))
        print("With compound type of interest you will get: ",total_amount_compound)
    else:
        print("Error, select simple or compound: ")

#10. If the user selects ‘bond’ is better to separate the two parts investment and bond.
if user_input == "bond":
#11. Preparing the next question regarding the house value.
    house_value = float(input("How much would you like to deposit?: \n"))
    P=float                          
    r=float(input("How much is the interest rate?: \n"))
    t=int(input("For how many years?: \n"))
    interest_choice= input("What kind of interest: simple or compound?: \n").lower()

    print("Your house value: ", house_value)
#12. Preparing the next question regarding the interest rate.
    interest_rate_house = float(input("How much is the annual interest rate: "))
    print("Interest rate:", interest_rate_house)
#13. Preparing the next question regarding the amount of months of bond repayment.
    bond_repayment_months = float(input("How many months would it take to repay the bond: "))
    print("Interest rate:", bond_repayment_months)
#14. Applying the formula to calculate monthly interest
    monthly_interest_rate =(interest_rate_house/100)/12
#15. Applying the formula to calculate repayment amount
    repayment = (monthly_interest_rate* house_value)/( 1 - math.pow(( 1 + monthly_interest_rate),- bond_repayment_months))
    print(f"Monthly bond repayment amount:{repayment:.2f}")



