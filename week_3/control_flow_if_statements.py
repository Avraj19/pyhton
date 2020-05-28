import time

# Control Flow
#
# Control flow dictates where the code will run
# Much like dams in real life
# if function
# if function works with booleans (True or False
# We usually use comparision operators to equate and compare objects, and results in true or false
#
# syntax if function
# if <condition>:
#   block of code  ## block of code is the section that runs
# elif <second condition>:
#   another block of code
# else:
#   last block of code
#
# Logical and syntax
# <condition> and <condition>
# both side must be true for result tio be true
#
# logical or syntax
# <condition> or <condition>
# Only one side will need to be true for the result to be true
#
# is_rainy = True
#
# if is_rainy == True:
#     # time.sleep(2)
#     print('Bring umbrella')

weather = input('What is the weather like? \n').strip().lower()

if weather == 'natural disaster':
    print('lol, were fucked')
