#Valid email ID
#Description
#Consider that email IDs are supposed to be for the following format:
#username@website.extension.
#Here, there are three conditions to keep in mind:
#1. The username can only contain characters 0-9, a-z and A-Z.
#2. The website name can contain only characters a-z
#3. The extension can have 2 or 3 alphabets(a-z).

#Given an email ID, you have to determine if it is valid or not.

#Sample Input:
#prerna@upgrad.com

#Sample Output:
#valid


import re

def checkmail(email):
    #complete the function
    #the function should return the strings "invalid" or "valid" based on the email ID entered
    res = re.search("^\w+[a-zA-Z0-9]+@[a-z]+\.[a-z]{2,3}", email)
    if not res:
        return "invalid"
    
    return "valid"
    
email=input()
print(checkmail(email))
