# Practice strings

# Welcome to Sparta - exercise
# Version 1 specs - with concatenation

# define a variable name, and assign a string
name = ''
# prompt the user for input and ask the user for his/her name
user = input('What is your name? \n').strip().capitalize()
# re assign the original variable this this input
name = user
# use concatenation to print a welcome message and use methods to format the name/input (remove white spaces)
print('Hi '+name)
# Version 2 - with interpolation
# ask the user for a first name, save it in a variable
f_name = input('What is your first name? \n').strip().capitalize()
# ask the user for a last name, save it in a variable
l_name = input('What is your last name? \n').strip().capitalize()
# use interpolation to print the message
print(f"Hello {f_name} {l_name}")

# Calculate year of birth
# gather details on age and name
user_name = input('What is your name? \n').strip().capitalize()
user_age = input('How old will you be this year? \n').strip().capitalize()
# print something like
user_DOB = 2020 - int(user_age)
# OMG <person>, you are <age> years old so you were born in <year>
print('OMG '+user_name+', you are '+user_age+' years old so you were born in ' + str(user_DOB))
