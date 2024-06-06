#This function does addition operation.
def add(number1,number2): 
    summation=number1+number2
    print("Summation of the given inputs", number1 ,"and", number2 ,"is:-", summation)

#This function does subtract operation.
def subtract(number1,number2):
    substraction=number1-number2
    print("Substraction of the given inputs", number1 ,"and", number2 ,"is:-", substraction)

#This function does multiplication operation.
def multiply(number1,number2):
    multiplication=number1*number2
    print("Multiplication of the given inputs", number1 ,"and", number2 ,"is:-", multiplication)

#This function does floor division operation.
def floor_division(number1,number2):
    if(number2==0):
        print("Undefined (division by zero)")
    else:
        quotient , remainder = divmod(number1,number2)
        print("quotient of the given inputs for floor division", number1 ,"and", number2 ,"is:-", quotient)
        print("remainder of the given inputs for floor division", number1 ,"and", number2 ,"is:-", remainder)

#This function does true division operation.
def true_division(number1,number2):
    if(number2==0):
        print("Undefined (division by zero)")
    else:
        quotient = number1/number2
        print("quotient of the given inputs for floor division", number1 ,"and", number2 ,"is:-", quotient)

#This function does exponentiation operation.
def exponent(number1,number2):
    exponentiation=number1**number2
    print("exponentiation of the given inputs", number1 ,"and", number2 ,"is:-", exponentiation)

#This function calculates after taking user choice and numbers.
def calculate(a,number1,number2):
    if(a == "A"):
        add(number1,number2)
    elif(a == "B"):
        subtract(number1,number2)
    elif(a == "C"):
        multiply(number1,number2) 
    elif(a == "D"):
        floor_division(number1,number2)
    elif(a == "E"):
        true_division(number1,number2)
    elif(a == "F"):
        exponent(number1,number2)

#Opening statement.
print("Hello!.This is a simple CALCULATOR for basic mathematical operetion.")
list_operations=[print("Please select operation it support -\n" \
        "A) Add\n" \
        "B) Subtract\n" \
        "C) Multiply\n" \
        "D) Floor Division\n" \
        "E) True Division\n" \
        "F) Exponent\n ")]
operation_options=["A","B","C","D","E","F"]

#This function prints result after checking the validity of given user inputs for both choice and numbers.
#Also repeats it , asking user if user want to do farther calculation or not , till user says no.
while (True):
    a=input("Choose what you want to do from the list operations,only write:-(A/B/C/D/E/F):-").upper()
    if(a not in operation_options):
        print("Unsuported operation!.Please see the valid operation from the list of operations and then choose,for the next calculation.")
        continue
    else:
        while(True):
            try:
                number1=float(input("Enter the 1st number:-"))
                break
            except ValueError:
                print("Invalid input!. Please enter valid 1st number.")
        while(True):
            try:
                number2=float(input("Enter the 2nd number:-"))
                break
            except ValueError:
                print("Invalid input!.Please enter valid 2nd number.")
        calculate(a,number1,number2)
    b=input("Do you want to do any calculation further?only:-(yes or no):-").lower()
    if(b!="yes"):
        print("Thank you for using this CALCULATOR.")
        break
