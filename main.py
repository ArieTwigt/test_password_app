import random
from import_functions import read_users_file
import pandas
import string

users_firstname, users_lastname, user_email = read_users_file("usernames.csv")

letters = string.ascii_uppercase
numbers= "0123456789"


password_len = int(8/2)

# create empty list to store the passwords
passwords_list = []

# define the number of users
num_users = len(users_list)

# generate the passwords
for i in range(0, num_users):
    password = ''
    
    for j in range(0, password_len):
        password_char = random.choice(letters) + random.choice(numbers)

        password += password_char
        # for k in range(0,password_len - 6):
        #     password_char = random.choice(numbers)
            # password = password + password_char
        
    print("Here is your password:", password)
    # append the password to the passwords_list
    passwords_list.append(password)


# create a pandas DataFrame to export the csv
df = pandas.DataFrame(
    {
        "usersname": users_list,
        "password": passwords_list
    }
)

# export to csv
df.to_csv("passwords.csv", index=False)