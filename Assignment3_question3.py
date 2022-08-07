"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""
#fxn take string and return no. lowercase & uppercase char respectively
def upperlower(string):
    lowercase=uppercase=0
    for i in string:
        if i.islower():
            lowercase+=1
        elif i.isupper():
            uppercase+=1
    return lowercase,uppercase

#Main body
string=input("input the string:")
lowercase,uppercase=upperlower(string)
print(f"No. of Upper case characters :{uppercase}\n No. of Lower case character:{lowercase}")
