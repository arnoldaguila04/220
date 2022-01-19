"""
Arnold Aguila
hw1.py

Problem: Calculating the volume of a rectangle, Calculating shooting percentage, Calculating coffee per pound, and
changing KM to Miles.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    print("This function calculates the area of a rectangle.")
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    print("This function calculates the volume of a rectangle.")
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    print("This function calculates your shooting percentage.")
    shots = eval(input("How many shots fired: "))
    hits = eval(input("How many hits on target: "))
    accuracy = (hits / shots ) * 100
    print("Shooting Percentage =", accuracy, "%")



def coffee():
    print("This function calculates coffee cost per lbs.")
    user_input = eval(input("How many pounds of coffee purchased: "))
    x = 10.50 * user_input
    y = 0.86 * user_input
    ans = x + y + 1.50
    print("Your total is:", ans)



def kilometers_to_miles():
    print("This function changes km to miles")
    ans = eval(input("Enter Km: ")) * 0.62137
    round_ans = round(ans, 2)
    print("That's", round_ans, "miles!")



if __name__ == '__main__':
    pass
