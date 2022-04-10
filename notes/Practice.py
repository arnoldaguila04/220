def average_sentinel():
    acc = 0
    count = 0
    num = eval(input("enter a number (enter to exit)>> "))
    while num != '':
        acc = acc + num
        count = count + 1
        num = eval(input("enter a number (enter to exit)>> "))
    print("average: {}".format(acc / count))


average_sentinel()


def average_file():
    acc = 0
    count = 0
    file_name = "file_data.txt"
    file = open(file_name, "r")
    for line in file:
        num = eval(line)
        acc = acc + num
        count = count + 1
    print("average: {}".format(acc/count))


average_file()


def average_file_whileloop():
    acc = 0
    count = 0
    file_name = "file_data.txt"
    file = open(file_name, "r")
    line = file.readline()
    while line != "":
        num = eval(line)
        acc = acc + num
        count = count + 1
        line = file.readline()
    print("average: {}".format(acc/count))


average_file_whileloop()


def average_file_while_nested():
    acc = 0
    count = 0
    file_name = 'nested_data.txt'
    file = open(file_name, "r")
    line = file.readline()
    while line != '':
        # '4,23,2314,234,234,5,6,77'
        nums_string = line.split(',')
        i = 0
        while i < len(nums_string):
            num = nums_string[i]
            acc = acc + eval(num)
            count = count + 1
            i = i + 1


average_file_while_nested()

# class / objects --> instance of a class

# Die.py ----- START
from random import randint
class Die:
    def __init__(self, num_sides):
        self.sides = num_sides
        self.value = 1
    def roll(self):
        new_value = randint(1, self.sides)
        self.value = new_value
    def getvaule(self):
        return self.value
# Die.py ---- END


from Die import Die
def main():
    number_of_sides = eval(input("How many sides"))
    my_die = Die(number_of_sides)
    playing = True
    while playing:
        my_die.roll()
        print(my_die.get_value)
        stopping = input("hit enter to roll again? ")
        playing = not stopping