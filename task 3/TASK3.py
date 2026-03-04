import random
import string

# asking user about the desired length of the password

length = int(input("Enter the length of the password: "))

characters = string.ascii_letters + string.digits + string.punctuation
 
password = ""
 # Generating the password
for i in range(length):
   password += random.choice(characters) 

# Display the password
print("Generated password:  ",password)
