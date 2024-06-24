#dictionary to store details of task.
Task_list={}

#This function takes input of task details and adds to the dictionary.
def add():
    a=input("Enter task name:-").strip()
    b=input("Please enter details of your task:-").strip()
    if(a in Task_list):
        print("Task already exists!")
    
    Task_list[a]={
        "Details":b
    }
    print("Task is added.")

#This function views every details of Task list.
def view():
    if(not Task_list):
        print("Task not found!")
    else:
        for Task_name, details in Task_list.items():
            print("Name of the task:-",Task_name,"")
            print("Details:-",details["Details"])

#This function updates Task details.
def update():
    Task_Name=input("Enter the task name of the task whose details you want to update:-").strip()

    if(Task_Name in Task_list):
        choose=input("Want to change name?  or details?:-").strip().lower()

        if(choose=="name"):
            New_task_name=input("Enter new  name of the task:-").strip()
            Task_list[ New_task_name]=Task_list.pop(Task_Name)
            print("Updated!")

        elif(choose=="details"):
            New_details=input("Enter new details:-").strip()
            Task_list[Task_Name]["Details"]=New_details
            print("Updated!")
 
    else:
        print("Task not found.")

#This function deletes Task acording to user input.
def delete():
    Task_Name = input("Enter the name of the task you want to delete:- ")
    if Task_Name in Task_list:
        del Task_list[Task_Name]
        print("Details of", Task_Name, "has been deleted.")
    else:
        print("Task not found.")

#This function does work acording to user choice.
def do(option):
    if(option=="A"):
         add()
    if(option=="B"):
         view()
    if(option=="C"):
         update()
    if(option=="D"):
         delete()

#Opening statement.
print("Hi it is a TO-DO-LIST application!")
print("It supports:-")
print("A)Add task details")
print("B)Show task details")
print("C)Update task details")
print("D)Delete task details")

options_list=["A","B","C","D"]

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
        print("Thank you for using TO-DO-LIST application!")
        break
