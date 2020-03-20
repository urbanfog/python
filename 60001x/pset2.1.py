
balance = 484 # the outstanding balance on the credit card at month 0
annualInterestRate = 0.2 # annual interest rate as a decimal
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12

for i in range(12):
  monthlyMinPayment = balance * monthlyPaymentRate
  balance -= monthlyMinPayment
  interest = balance * monthlyInterestRate
  balance += interest

print("Remaining balance:", round(balance, 2)) # balance at year end