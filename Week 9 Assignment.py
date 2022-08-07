import os

os.getcwd()

import json

name = input("Please enter your first and last name: ")
name = name.title()

address = input("\nPlease enter your address: ")
address = address.title()

phone = input("\nPlease enter your phone number: ")

commas = name.split(), address.split(), phone.split()

filename = 'test.json'
with open(filename, 'w') as f:
    json.dump(commas, f)

print(f"\nYou have entered the following information: \n{commas}")