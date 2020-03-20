balance = 999999 # the outstanding balance on the credit card
annualInterestRate = 0.18 # annual interest rate as a decimal

lowerMonthlyPayment = balance / 12
upperMonthlyPayment = (balance * (1 + annualInterestRate / 12)**12) / 12.0

while True:
  midMonthlyPayment = (lowerMonthlyPayment + upperMonthlyPayment) / 2
  prevBalance = balance

  for month in range(12):
    prevBalance -= midMonthlyPayment
    interest = prevBalance * annualInterestRate / 12
    prevBalance += interest
  prevBalance = round(prevBalance, 2)  

  if prevBalance == 0:
    break
  elif prevBalance < 0:
    upperMonthlyPayment = midMonthlyPayment
  elif prevBalance > 0:
    lowerMonthlyPayment = midMonthlyPayment
print("Lowest Payment:", round(midMonthlyPayment, 2))