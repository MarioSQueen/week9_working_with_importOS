import os

pick_direct = input("Please type in which directory you would like to save this file: ")

selected_direct = os.path.normpath(pick_direct)

import json

filename = input("\nPlease name the file where you would like the information saved: ")

name = input("\nPlease enter your first and last name: ")
name = name.title()

address = input("\nPlease enter your address: ")
address = address.title()

phone = input("\nPlease enter your phone number: ")

commas = name.split(), address.split(), phone.split()

filename = f"{filename}.json"
with open(filename, 'w') as f:
    json.dump(commas, f)

print(f"\nYou have entered the following information: \n{commas}")