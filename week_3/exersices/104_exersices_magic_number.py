# Magic number game!

# I want you to use operators
# equate something
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# We should define/assign number to a variable called magic_number

magic_number = 4
while True:
    # I need to ask user for input
    user = input('I am thinking of a number, \n'
                 'its between 1 and 10\n'
                 'can you guess what it is? \n').strip().lower()
    # I need to check if this input matches a magic_number
    # I need to let the user know if the response was write or not
    if user == '4' or user == 'four':
        print('OMG, how did you do that \n '
              'you read my mind \n'
              'you deserve a self five \n')
        break
    else:
        print('That\'s wrong, ill give you another try')

#self five












