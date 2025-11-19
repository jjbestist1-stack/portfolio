USD = 1.4
EUR = 1.14
BRL = 4.77
TRY = 151.05
JPY = 5.68
feeH3 = 0.035
feeH2 = 0.03
feeH1 = 0.025
feeL1 = 0.02
feeL2 = 0.015
GBP_Convert = float(input("Please input the amount of pounds you want to convert: "))
while GBP_Convert > 2500 or GBP_Convert < 1:
    print("Invalid amount. Please enter an amount between 1 and 2500.")
    GBP_Convert = float(input("Please input the amount of pounds you want to convert: "))
Emm_disc = str(input("does the client have an employee discount? (yes/no): ")).lower()
if Emm_disc != "yes" and Emm_disc != "no":
    print("Invalid input. Please enter 'yes' or 'no'.")
    Emm_disc = str(input("does the client have an employee discount? (yes/no): ")).lower()
if GBP_Convert < 301:
    fee = GBP_Convert * feeH3
elif GBP_Convert < 701:
    fee = GBP_Convert * feeH2
elif GBP_Convert < 1501:
    fee = GBP_Convert * feeH1
elif GBP_Convert < 2001:
    fee = GBP_Convert * feeL1
else:
    fee = GBP_Convert * feeL2
if Emm_disc == "yes":
    fee = fee * 0.95
    print("An employee discount has been applied, and the final fee is £",round(fee, 2))
else:
    print("The final fee is £",round(fee, 2))
Convert_to = str(input("Please enter the currency you want to convert to (USD, EUR, BRL, TRY, JPY): ")).upper()
while Convert_to not in ["USD", "EUR", "BRL", "TRY", "JPY"]:
    print("Invalid currency. Please enter one of the following: USD, EUR, BRL, TRY, JPY.")
    Convert_to = str(input("Please enter the currency you want to convert to (USD, EUR, BRL, TRY, JPY): ")).upper()
if Convert_to == "USD":
    converted_amount = GBP_Convert * USD
    print("The converted amount is $", round(converted_amount, 2))
elif Convert_to == "EUR":
    converted_amount = GBP_Convert * EUR
    print("The converted amount is €", round(converted_amount, 2))
elif Convert_to == "BRL":
    converted_amount = GBP_Convert * BRL
    print("The converted amount is R$", round(converted_amount, 2))
elif Convert_to == "TRY":
    converted_amount = GBP_Convert * TRY
    print("The converted amount is ₺", round(converted_amount, 2))
elif Convert_to == "JPY":
    converted_amount = GBP_Convert * JPY
    print("The converted amount is ¥", round(converted_amount, 2))
TotalCharge = GBP_Convert + fee
print("The total charge including fees is £", round(TotalCharge, 2))
print("You now have", converted_amount, Convert_to, "after conversion.")
print("Thank you for using our currency exchange service!")