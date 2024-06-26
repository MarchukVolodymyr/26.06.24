import random
import string
length = int(input("Enter a length: "))
symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
mystr = ""
for i in range(length):
    mystr += random.choice(symbols)
print(mystr)
