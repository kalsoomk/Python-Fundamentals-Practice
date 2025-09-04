#Quotient of two numbers with zero check

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if num_2 != 0:
    quotient = num_1 / num_2
    print(f"The quotient of both numbers is: {quotient}")
else:
    print("Error: Cannot divide by zero!")
