#Variables
op1 = input()
op2 = input()
x = op1 + op2

#Functions
def say_hello():
    print("Hello from a method")

def sum(op1, op2):
    x = op1 + op2
    return op1 + op2

def sub(op1, op2):
    y = op1 - op2
    return op1 - op2

def multi(op1, op2):
    z = op1 * op2
    return op1 * op2

def divi(op1, op2):
    a = op1 / op2
    return op1 / op2

def menu():
    print("  Menu  ")
    print("[1] - Add")
    print("[2] - Subtract")
    print("[3] - Multiply")
    print("[4] - Divide")
    print("[x] - Exit")

#Intro
print("--" * 15)
print("Welcome to DragonStone")
print("-" * 30)


#Meat and Potatoes
opc = ""
while(opc != "x"):
    menu()
    opc = input("Select an option")
    if(opc == x):
        break

    num1 = float(input("First Number: "))
    num2 = float(input("Second Number: "))

    if(opc == '1'):
        sum_res = sum(num1,num2)
        print("Sum = " + str(sum_res))
    input("Press Enter to go back")

    if(opc == '2'):
        sub_res = sub(num1,num2)
        print("sub: " + str(sub_res))


    if(opc == '3'):
        multi_res = multi(num1,num2)
        print("multiply: " + str(multi_res))


    if(opc == '4'):
        divi_res = divi(num1,num2)
        print("divide: " + str(divi_res))


#Outro
print("Thank you for using PyCalc, goot Byte!")
print("lol, yeah. I can use punny puns too! It's in my programming")
