# [SIG Python Task 1] 

"""
Tasks to performs: 
a) Print 'Hello, World! From SIG Python - <your name>' to the screen
b) Calculate Volume of a Sphere
c) Create a customised email template for all students, 
   informing them about a workshop.

PS: This is called a docstring... and it will not be interepreted
    So leave these instructions here.. no problems.
    The first line having '#' is called a comment. It will be ignored too.
    You can write your own comments and docstrings to make your code clear
    and documented.
"""

# a) Print 'Hello, World! From SIG Python - <your name>' to the screen
# Write you code here
print("Hello, World! From SIG Python-Aditi Garg")
print("\n")                                                                                                 #for leaving extra lines .

# b) Calculate Volume of a Sphere
# Take the radius as input from the user and use the math module
a=int(input("enter the radius= "))
import math                                                                                             #importing math module.
formula=(4/3*math.pi*(a**2))                                                        #use of math module.
print("Volume of Sphere=",formula)
print("\n")

#c) Create a customised email template for all students, informing them about a workshop that the student applied for earlier.
# Take the student's name, workshop, Time, Date, writer's name, organization's name 
# as input from the program's user 
 
# Use the given string as your template [This is a multi-line string]
email_msg = '''Dear {student_name},
We have received your request to register for the Workshop event and the 
workshop you applied for {workshop} has been scheduled at {Time}
on {Date}.

We will be seeing you there! Thanks for participating.

Regards,
{writer_name}
{organization_name}
'''
# Format using .format() or f-strings
student_name=input("enter your student_name :")
workshop=input("enter workshop:")
Time=str(input("enter time:"))
Date=str(input("enter dd/mm/yyyy:"))
writer_name=input("enter writer_name:")
organization_name=input("enter organization_name:")
      
print(f'\n\nDear {student_name},')
print(f'We have received your request to register for the Workshop event and the ')
print(f'workshop you applied for {workshop} has been scheduled at {Time}')
print(f'on {Date}.\n')
print(f'We will be seeing you there! Thanks for participating.\n')
print(f'Regards,')
print(writer_name)
print(organization_name)

# NOTE: Make sure to print few empty lines after each task
