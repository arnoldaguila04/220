"""
Name: Arnold Aguila
hw6.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

def cash_converter():
    number = eval(input("Enter an integer: "))
    print("That is ${}.00".format(number))
cash_converter()

def encode():
    message = input("Enter a message: ")
    list("{}".format(message))
    key = eval(input("Enter a Key: "))
    for i in message:
        print(chr(ord("{}".format(i)) + key), end="")
encode()

def sphere_area(r):
    return 4 * math.pi * r**2
sphere_area()

def sphere_volume(r):
    return (4/3) * math.pi * r**3
sphere_volume()

def sum_n(n):
    x = 0
    for i in range(1, n+1):
        x += i
    return x
sum_n()

def sum_n_cubes(n):
    x = 0
    for i in range(1, n+1):
        x += i**3
    return x
sum_n_cubes()

def encode_better():
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"
        ,"S","T","U","V","W","X","Y","Z","[",chr(92),"]","^"
        ,"-","`","a","b","c","d","e","f","g","h"
        ,"i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    message = input("Enter a message: ")
    key = input("Enter a key: ")
    list("{}".format(message))
    list("{}".format(key))
    new_list_message = []
    new_list_key = []
    for i in message:
        new_list_message.append(((ord(i) - 65) % 57))
    for j in key:
        new_list_key.append(((ord(j) - 65) % 57))
    for k in range(len(message)):
        ans = ((new_list_message[k] + new_list_key[(k % len(key))]) % 57)
        print(alphabet[ans - 1], end="")
encode_better()

