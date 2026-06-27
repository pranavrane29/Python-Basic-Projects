print ("Welcome to calculator!")  

print("Enter two numbers to perform the arithmetic calculations -")


number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
aritmetic_operator = input("Select an aritmetic operation(+,-,*,/) to perform -")

if aritmetic_operator == "+":
    result = number_1 + number_2
elif aritmetic_operator == "-":
     result = number_1 - number_2
elif aritmetic_operator == "*":
     result = number_1 * number_2
elif aritmetic_operator == "/":
     result = number_1 / number_2
else :
     print("Invalid operator selected!!")

print("You have selected to do " + aritmetic_operator + " therefore, it's result is -")

print(result)



