import random
import string 

#This function generates password according to user choice.
def generate(a,pass_length):
    if(a==1):
        Password=""
        for i in range(1,pass_length+1):
            Password=Password+random.choice(Char)
        print("Your strong or complex password is:-",Password)
    
    elif(a==2):
        Password=""
        for i in range(1,pass_length+1):
            Password=Password+random.choice(Char2)
        print("Your random password is:-",Password)

#Giving variables to the string digits,ascii latters and punctuation.
#making combination for strong or complex and random passwords.
Int = string.digits
Str = string.ascii_letters
Symbol = string.punctuation
Char = Int + Str + Symbol 
Char2 = Int + Str

#Opening statement.
print("HI! friend,it is a PASSWORD GENERATOR.")
print("This PASSWORD GENERATOR is able to create 2 type of password.")
print("So the 2 type of password is:-")
print("1)Strong or complex")
print("2)Random")

#Asking user for inputs for generating the passward.
#It checks the validity of given user inputs.
#loop will run continuously until user says no.
while (True):
    a=int(input("Please enter the type of the password from above options,only write(1/2):-"))
    if(a>2):
        print("Invalid choice!.Please see the valid options for the type of the password and then choose for getting next password.")
        continue
    while(True):
        try:
            pass_length=int(input("Please enter the length of the Password(EXCEPT 0):-"))
            break
        except ValueError:
            print("Invalid input!.Please enter a valid input.")
            continue
    generate(a,pass_length)
    b=input("Do you want to create another password? write only(yes/no):-")
    if(b=="no"):
        print("Thank you for using PASSWORD GENERATOR.")
        break



