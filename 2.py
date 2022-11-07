#Landen Dale    
#2.py
#This code will accept students names and Gpa to calculate if they qualify for the honor role or Dean's list

#Creating the opening message
print("Enter the GPA of a students. Make sure the GPA is between 3.25 and 3.5\n")

i=0
tot = 0.0
while(i<1):
    i = i + 1
    #Making the input to enter a students name
    NAME=str(input("enter the name: "))
    
    #Message to enter the GPA
    print("Enter GPA of the student " ": ")
    gpa = float(input())
    
    #Defining the inputs to certain gpas only 
    if gpa<=3.25 or gpa>=3.5:
        print("GPA entered is not in range of 3.25 and 3.5 Please enter again.\n")
        i = i-1
    
    else:
        tot = tot + gpa

    #Making the deans list
    if gpa>=3.5:
        print(NAME, "is on the Dean's list")

    #Making the honor roll
    if gpa<=3.5:
        print(NAME, "is on the Honor roll list")

   
