#!/usr/bin/python3
string = input("Enter a string: ").lower()
vowels = "aeiou"

i = 0
while i < len(string):
    if string[i] not in vowels and string[i] != "y" and string[i].isalpha():
        print(string[i], end=", ")
    i += 1
