try:
  a=float (input("enter first number:"))
  b=float(input("enter secound number:"))
  print (f"addition:{a+b}")
  print(f"subtraction:{a-b}")
except valueError:
  print("please enter valid number.")
