# mr Miyagi trainee

# make a mr miyagi virtual assistant

# as a user I should be able to speak with mr miyagi and get appropriate response s as I go

# Ask for user input and depending on the response, mr Miyagi will respond.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# every time you ask a question --> Mr. Miyagi responde with
# --> 'questions are wise, but for now. Wax on, and Wax off!'
# every statement/question must start with Sensei, otherwise:
# --> 'You are smart, but not wise - address me as Sensei please'
# every time you mention 'block' or 'blocking' --> Mr. Miyagi responde with
# --> 'Remember, best block, not to be there..'
# anything else you say:
# --> 'do not lose focus. Wax on. Wax off.'


# Make it so you keep playing until we say: 'Sensei, I am at peace'
# --> 'Sometimes, what heart know, head forget'

# your_response = input('(MR.Miyagi)... -.-')

#  EXTRA:
#  make it run continuously
#  consider best practices of functions - make this functional

while True:
    user = input('What question do you have for mr Miyagi? \n').lower()

    if user.split()[0] == 'sensei' or user.split()[0] == 'sensei,':
        if user == 'sensei i am at peace' or user == 'sensei, i am at peace':
            print('Sometimes, what heart know, head forget')
            break
        elif user.count('?') >= 1 and (user.count('block') or user.count('block')):
            print('Remember, best block, not to be there..')

        elif user.count('?') >= 1:
            print('questions are wise, but for now. Wax on, and Wax off!')
        else:
            print('do not lose focus. Wax on. Wax off.')

    else:
        print('You are smart, but not wise - address me as Sensei please')

