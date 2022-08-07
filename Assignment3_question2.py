"""
Write a Python program to reverse a string.
Sample String : "1234abcd"
Expected Output : "dcba4321"
"""
def reverse(string):
    rev=""
    for i in string:
        rev= i + rev
    return rev

string=input("enter string:")
print("\n rev string :",reverse(string))