"""import random
# print("hello world")
#
# # victor buelna
# # (This is python 2.7)
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print  # this makes a new line. In python 3.6, it looks like: print()
# print("see if you can figure this out")
# print(14 % 5)
#
# car
# name = "victor buelna"
# car_type = "GTR"
# car_cylinders = 8
# car_mpg = 1000
#
# # Inline printing
# print("I have a car called")
#
# # Asking for input
# name = input("Whats is your name?") # In python 3, it is just called input
# print("hello %s." % name)
#
# age=input("How old are you?") #in ptyhon 3, is just called input
# print("%s?! wow your so young!"% age)

#functions


def print_hw():
    print("hello world")



print_hw()
print_hw()
print_hw()


def say_hi(name):
    print("hello %s." % name)
    print("enjoy you day.")


say_hi("john")


def print_age(name,age):
    print("%s is %d years old."% (name, age))
    age += 1 # age = age + 1
    print("Next year, they will be %d" % age)


print_age("John", 15)

def f(x):
    return x**3 + 4 * x**2 * x - 4


print (f(3))
print (f(4))
print (f(5))


# If statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >=80 :
        return "B"
    elif percentage >= 70:
        return "c"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "F"


'''write a function called "happy_bday"
that "sings" (print) Happy birthday

It must take one parameter called "name"
'''

def happy_bday(name):
    print("Happy birthday to you" + ",")
    print("Happy birthday to you" + ",")
    print("Happy birthday to " + name + ",")
    print("Happy birthday to you" + ",")

happy_bday("John")


# Loops

for num in range(10):
    print(num + 1)

# DO NOT RUN!!!
a = 1
while a < 10:
    print(a)
    a += 1


# Random Numbers
    
print(random.randint(0,100))
"""
'''

# Lists
the_count = (1,
# Going through the list
for item in shopping_list:
    print(item)

for num in the_count:
    print(num * 2)

len(shopping_list)  # Gives me the length of the list
range(3)  # Gives a list of the number 0 through 2
range(len(shopping_list)) # A list of EVERY index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item of index %d is %s" % (num, item))

# Turn things into a list
str1 = "Hello Class!"
listOne = list(str1)2, 3, 4, 5)
shopping_list = ["Noodles", "Eggrolls", "Milk", "Rice", "Soda", "Chips"]

print(shopping_list[2])

print(len(shopping_list))

print(listOne)
listOne[11]= '.'
print(listOne)
print("".join(listOne))

# Add things to a list
shopping_list.append("cereal")
print(shopping_list)


# Removing things from a list
shopping_list.remove("Soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

# the string class
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

# Dealing with strings
strTwo = "ThIs Is A vErY oDd SeNtEnCe"
lowercase = strTwo.lower()
print(lowercase)
'''

largest_dictionary = {
    'CA': {
        'NAME': 'California',
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    'AZ': {
        'NAME': 'Arizona',
        'POPULATION': 6931000,
        'BORDER ST': [
            'California',
            'Utah',
            'Nevada',
            'New Mexico'
        ]
    },
    'NY': {
        'NAME': "New York",
        'POPULATION': 19750000,
        'BORDER ST': [
            'Vermont',
            'Massachusetts',
            'Connecticut',
            'Pennsylvania',
            'New Jersey'
        ]
    }
}

print(largest_dictionary['NY']['POPULATION'])

print(largest_dictionary['NY']['NAME'])



