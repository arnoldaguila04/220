"""
Name: Arnold Aguila
hw5.py
Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def name_reverse():
    fl = input("Enter First and Last Name seperated by a space: ")
    fll = fl.split()
    print(fll[1] + ",", fll[0])
name_reverse()

def company_name():
    domain = input("Enter domain name: ")
    splitDomain = domain.split(".")
    print(splitDomain[1])
company_name()

def initials():
    nos = eval(input("How many students are in the class: "))
    for i in range(nos):
        name = input("What is the name of the student: ")
        nameSplit = name.split()
        firstName = nameSplit[0]
        lastName = nameSplit[1]
        print(firstName[0] + lastName[0])
initials()

def names():
    nOs = eval(input("How many students are in the class: "))
    nL = input("Enter list of names: ")
    nLs = nL.split(", ")
    for i in range(len(nLs)):
        name = nLs[i]
        nS = name.split()
        fI = nS[0]
        lS = nS[1]
        print(fI[0] + lS[0], end=" ")
names()

def third():
    num = eval(input("Enter the number of sentences: "))
    third_list = []
    for i in range(num):
        sentence = input("enter sentence " + str(i + 1) + ": ")
        x = sentence[0: len(sentence): 3]
        third_list.append(x)
    for item in third_list:
        print(item)
third()

def word_average():
    x = 0
    sentence = input("Enter a sentence: ")
    sentence = sentence.split(" ")
    for i in range(len(sentence)):
        x = x + len(sentence[i])
    ans = x/len(sentence)
    print(ans)

word_average()

def pig_latin():
    x = 0
    sentence = input("Enter a sentence you want to convert to pig latin: ")
    sentence = sentence.split(" ")
    for i in range(len(sentence)):
        x = sentence[i]
        print(x[1: ] + x[0] + "ay", end=" ")
pig_latin()