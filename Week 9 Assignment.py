# Mario S. Queen
# CIS 245
# August 2022
# Working with import OS; creating program that allows user to navigate to a specified director, create a file, and save information within that file

import os

pick_direct = input("Please type in which directory you would like to save this file: ")

# using os.path command with the input user enters to find directory
os.path.normpath(pick_direct)

import json

filename = input("\nPlease name the file where you would like the information saved: ")

name = input("\nPlease enter your first and last name: ")
name = name.title()

address = input("\nPlease enter your address: ")
address = address.title()

phone = input("\nPlease enter your phone number: ")

# Using split() to add commas as directed in assignment instructions
commas = name.split(), address.split(), phone.split()

filename = f"{filename}.json"
# Using 'with open' and 'json.dump' to save the info entered into the appropriate file and to have Python auto close. 
with open(filename, 'w') as f:
    json.dump(commas, f)

# Was unsure if it was necessary to print in the program but the last instruction in the assignment says to show user for verification
print(f"\nYou have entered the following information: \n{commas}")