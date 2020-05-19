# Using and maanging strings
# single_quotes = 'Avraj\'sHello world'
# print(single_quotes)
#
# double_quotes = "Avraj's Hello world"
#
# quotes_in_quotes = 'I said "wow!"'
#
# print(quotes_in_quotes)
#############################
# String slicing
# print(Hw[start:end])
# only works for strings

# h e l l o   w o r l d !
# 0 1 2 3 4 5 6 7 8 9 10 11

# Hw = "Hello World"
# print(Hw[7:])
# print(Hw[0:5])
###################################
white_space = 'Lots\'s of space at the end    '
# Strip
# .strip()
# removes all spaces at the end of a line
#
# print(len(white_space)) # len = 30
# print(len(white_space.strip())) # len = 26
###############################################
example_text = "some text Here"
# More methods
# .count()
# This count the number of time this shows up

# print(example_text.count("text")) # text shows up once
#
# # every thing to lower case
# # .lower()
# print(example_text.lower())
#
# # shout form the roof tops
# # .upper()
# print(example_text.upper())

# make the first word in a str capital
# .capitalize()
# print(example_text.capitalize())

# replace words
# .replace(old_str, new_str)
# print(example_text.replace("Here", "There"))

###################################################
x = 2
y = 5.4
z = " there's now a number " + str(x) + " add it to " + str(y) + "this equals " + str(x + y)
# print(z)

x = "8"
# # find type
# print(type(x))
# # change to int
# print(type(int(x)))
# # change to float
# print(type(float(x)))

#################################################

# Boolean operators
# there are only two types True or False

# a = True
# b = False

greeting = "Hello world"
# print(greeting.startswith("h"))
# print(greeting.endswith("!"))

############################

