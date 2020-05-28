# # Functions
#
# Function have one job, becasue it makes it easier to test and understand
#
# # Syntax:
# def function_name():
#   block_of_code
#
# # How do they work?
# definr the function
# call the funtion
# the block_of_code runs as intended
#
# Other functionalists:
# - They can take ing arguments to be dynamic of morph the output
#
# Why functions?
# Because it keeps our code dry
# Don't
# Repeat
# Yourself
#
# Allowing us to call said function to do the action instead
#
# # Best prctices of a function
# - Naming convention in python is like a variable, lower_case_underscore()
# - It does ONE JOB! ONE!
# - Separation of concerns

## Basics of a test

def formated_name(name):
    return name.title().strip()


# test setup
known_input = '    avraj   '
expected_output = 'Avraj'

f_name = formated_name('    avraj   ')
print(formated_name(known_input) == expected_output)
