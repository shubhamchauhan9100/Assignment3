"""
Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""

#sumation fxn take list as parameter and return the sum of the no. in list.
def sumation(lst):
    total=0
    for i in lst:
        total+=i
    return total

#Fxn values is take element of the list
def values():
    lst=[]
    entermore="y"
    while(entermore=="y"):
        num=int(input("enter a no. in lst\n"))
        lst.append(num)
        entermore=input("Do you want to enter more no. in list?  y/n \n")
    return lst

#main Fxn or Fxn call in main body
lst=values()
print("sum of no. in list :",sumation(lst))
