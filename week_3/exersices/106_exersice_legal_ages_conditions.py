age = 12

driver_lisence = True


# - You can vote and drivre

# - You can vote

# - You can driver

# - you can't leagally drink but your mates/uncles might have your back (bigger 16)

# - Your too young, go back to school!

#  as a user I should be able to keep being prompted for input until I say 'exit'
while True:
    if age > 18:
        print('You can drive and vote, sound like your an adult')
    elif age > 17:
        print('You can driver')
    elif age > 16:
        print('you can\'t leagally drink but your mates/uncles might have your back (bigger 16)')
    else:
        print('your to young, get the hell back to school')
