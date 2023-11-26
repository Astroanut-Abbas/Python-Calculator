# Taking input from user
num1 = float(input("Enter Your first No.: "))
opr = (input("+,-,*,/"))
num2 = float(input("Enter Your Second No.: "))
# Applying Conditions
if (opr == +):
  print(num1 + num2)
elif (opr == -):
  print(num1 - num2)
elif (opr == *):
  print(num1 * num2)
else :
  print("Invalid Input")
