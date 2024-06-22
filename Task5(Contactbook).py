Contact_book = {}    

#This function takes input of contact details and add to the dictionary.
def add():
    a=input("Enter Name:-")
    b=input("Enter Phone number(10 digit):-")
    c=input("Enter Email:-")
    d=input("Enter Address:-")

    if(a in Contact_book):
        print("Contact already exists!")
    
    Contact_book[a]={
        "Phone no":b,
        "Email":c,
        "Address":d
    }
    print("Contact details added.")

#This function views every details of Contactbook.
def view():
    if(not Contact_book):
        print("Contact Not found!")
    else:
        for name, Details in Contact_book.items():
            print("Details of",name,":-")
            print("Phone no:-",Details["Phone no"])
            print("Email:-",Details["Email"])
            print("Address:-",Details["Address"])

#This function views the details of a specific person's details acording to the user input(by searching phone number or name).
def search():
    Choice=input("Do you want to search by phone number?(yes or no):-").lower()
    if(Choice=="yes"):
        Search_phone=input("Enter the phone number to search:-")
        found = False
        for name, Details in Contact_book.items():
            if Details["Phone no"] == Search_phone :
                print("Details for",name,":-")
                print("Phone no:-",Details["Phone no"])
                print("Email:-",Details["Email"])
                print("Address:-",Details["Address"])
                found = True
                break
        if not found:
            print("Contact not found!")
    else:
        Choice=input("Do you want to search by name?(yes or no):-").lower()
        if(Choice=="yes"):
            Search_name=input("Enter the name to search:-")
            if(Search_name in Contact_book):
                print("Name:-",Search_name)
                print("Details:-")
                print("Phone no:-",Contact_book[Search_name]["Phone no"])
                print("Email:-",Contact_book[Search_name]["Email"])
                print("Address:-",Contact_book[Search_name]["Address"])
            else:
                print("Contact not found.")

#This function updates contact details.
def update():
    Name=input("Enter the contact name whose details you want to update:-")

    if(Name in Contact_book):
        choose=input("Want to change name? phone no.? or email? or address?:-").lower()

        if(choose=="name"):
            New_name=input("Enter new name:-").strip()
            Contact_book[New_name]=Contact_book.pop(Name)
            print("Updated!")

        elif(choose=="phone"):
            New_no=input("Enter new phone no.:-")
            Contact_book[Name]["Phone no"]=New_no
            print("Updated!")

        elif(choose=="email"):
            New_email=input("Enter new email:-")
            Contact_book[Name]["Email"]=New_email
            print("Updated!")

        elif(choose=="address"):
            New_address=input("Enter new address:-")
            Contact_book[Name]["Address"]=New_address
            print("Updated!")
    
    else:
        print("Contact not found.")

#This function deletes contact acording to user input.
def delete():
    Name = input("Enter the name of the contact you want to delete: ")
    if Name in Contact_book:
        del Contact_book[Name]
        print("Contact of", Name, "has been deleted.")
    else:
        print("Contact not found.")

#This function does work acording to user choice.
def do(option):
    if(option=="A"):
         add()
    if(option=="B"):
         view()
    if(option=="C"):
         search()
    if(option=="D"):
         update()
    if(option=="E"):
         delete()

#Opening statement.
print("Hi it is a Contactbook!")
print("It supports:-")
print("A)Add contact details")
print("B)Show contact details")
print("C)Search contact details")
print("D)Update contact details")
print("E)Delete contact details")

options_list=["A","B","C","D","E"]

#This loop takes user input and runs the code till user says no.
while True:
    option=input("Please enter the option from above options which you want to do:-").upper()
    if(option not in options_list):
        print("Invalid option! please write the option it support.")
        continue
    else:
        do(option)
    e=input("Want to see or update another detail?:-").lower()
    if(e=="no"):
        print("Thank you for using Contactbook!")
        break

    