"""
Name: Arnold Aguila
hw3.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math

def average():
    print("This function finds the average of grades.")
    num_of_grades = eval(input("Enter how many grades you want to input: "))
    sum = 0
    grade = 0
    mean = 0
    for i in range(num_of_grades):
        grade = eval(input("Enter grade: "))
        sum = sum + grade
    mean = sum/num_of_grades
    print("The average is ", mean)


def tip_jar():
    print("This function passes a tip jar around and asks how much a user want to tip \n"
          "then adds all the tips up for a total.")
    sum = 0
    for i in range(5):
        tip = eval(input("How much would you like to donate? "))
        #print(tip)
        sum = sum + tip
    print("Total tips: ", sum)


def newton():
    x = eval(input("Enter the number you want to square root: "))
    approx = x
    times = eval(input("How many times do you want to approximate: "))
    for i in range(times):
        approx = (approx + (x/approx)) / 2
    print("The square root is approximately", approx)


def sequence():
    n = eval(input("Enter how many terms you like? "))
    for i in range(1, n+1):
        print((i - 1) + (i % 2), end=" ")


def pi():
    n = eval(input("How many terms in the series: "))
    total = 1
    num = 0
    denom = 0
    for i in range(n):
        num = i + (2.0 - (i % 2.0))
        denom = i + (1.0 + (i % 2.0))
        total *= num/denom
    ans = total * 2
    print(ans)


if __name__ == '__main__':
    pass
