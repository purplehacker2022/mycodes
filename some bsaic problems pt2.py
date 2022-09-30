# [SIG Python Task 3] 

"""
TODO: 
a) Calculate the temperature altitude from a list of temperatures
b) Count frequency of every character in a string (using dictionaries)
c) Verify De Morgan Laws (using sets)

NOTE: Have Fun Coding!
"""


# a) Calculate the temperature altitude from a list of temperatures
"""
Given a list of temperatures of one day, calculate the temperature amplitude (difference between highest and lowest temperature). Keep in mind that sometimes there might be a sensor error (represented as 'error').
"""

from copy import error
from ctypes import Union
from re import S, T, X
from tkinter import N, Y


temperatures = [3, -20, -6, -12, 'error', 24, 18, 28, 16, 14]

# Write you code here


temperatures = [3, -20, -6, -12, 'error', 24, 18, 28, 16, 14]
T = temperatures.remove('error')
print(temperatures)
t1 = max(temperatures)
print(t1)
t2 = min(temperatures)
print(t2)
print("the temperature amplitude : ",t2-t1,"\n\n")





# b) Count frequency of every character in a string (using dictionaries)
"""
Take a string as input from the user (for eg: 'abcccedeEEdffaG') and count the frequency each characters occurs in the string.

NOTE: Convert the string to upper or lower case first.
"""
# Write you code here

s1 = input("enter string:")
dict = {}
S = s1.upper()
print(S)
for i in S:
    keys = dict.keys()
    if i in keys:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict,"\n\n")



# c) Verify De Morgan Laws (using sets)
"""
Given a Universal Set 'U', and two of its subsets 'A' and 'B'
Verify the De Morgan laws using sets. 

# De Morgan Laws:
not (A or B) = not A and not B
not (A and B) = not A or not B

NOTE: Use the inbuilt operators/methods for set operations (intersection, union, difference, ...)
NOTE: Complement of a set 'X' is the difference: 'U' - 'X'
"""

U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
A = {0, 2, 4, 6, 8}
B = {3, 6, 9}


# Write your code here



U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
A = {0, 2, 4, 6, 8}
B = {3, 6, 9}
C = A.union(B)      # A or B
D = A.intersection(B)      # A and B
X = U.difference(A)   #not A
Y = U.difference(B)   #not B
N = U-C    #not( A or B)
M = U-D   #not(A and B)
O = X.intersection(Y)       #not A and not B
P = X.union(Y)              #not A or not B
if(N==O):
    print("1st demorgan's law is verified as","\nnot(A or B)",N,"=","not A and not B",O)
print("\n")
if(M==P):
    print("2nd demorgan's law is verified as","\nnot (A and B)",M,"="," not A or not B",P)



# NOTE: Make sure to print few empty lines after each task
