balance = 3926 # the outstanding balance on the credit card
annualInterestRate = 0.2 # annual interest rate as a decimal

monthlyInterestRate = annualInterestRate / 12
prevBalance = balance
iter = 0
monthlyMinPayment = 10

while prevBalance > 0:
    prevBalance -= monthlyMinPayment
    interest = prevBalance * monthlyInterestRate
    prevBalance += interest
    iter += 1
    if iter > 12:
        prevBalance = balance
        monthlyMinPayment += 10
        iter = 0
print("Lowest Payment:", round(monthlyMinPayment, 2)) # balance at year end
