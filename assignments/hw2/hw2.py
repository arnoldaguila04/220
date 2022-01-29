"""
Name: Arnold Aguila
hw2.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""
import math




def sum_of_threes():
    print("This function add the sum of three to the upper limit.")
    x = eval(input("Enter the upper limit: "))
    y = 0
    for i in range(3, x+1, 3):
        y = y + i
    print("The sum of threes is: ", y)


def multiplication_table():
    for i in range(1, 10+1):
        print()
        for j in range(1, 10+1):
            print(i * j, end="   ")

def triangle_area():
    a = eval(input("Enter side 1: "))
    b = eval(input("Enter side 2: "))
    c = eval(input("Enter side 3: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("area is: ", area)


def sum_squares():
    up = eval(input("Enter the starting range: "))
    down = eval(input("Enter the ending range: "))
    y = 0
    for i in range(up, down+1):
        y = (i * i) + y
    print(y)


def power():
    base = eval(input("Enter base: "))
    exponent = eval(input("Enter exponent: "))
    ans = 1
    for i in range(1, exponent + 1):
        ans = ans * base
    print(base, "^", exponent, "=", ans)

if __name__ == '__main__':
    pass
