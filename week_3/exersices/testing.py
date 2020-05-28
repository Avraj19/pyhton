# Testing functions


def check_if_digit_div_num(digit, num_div):
    return digit % num_div == 0




print(  __name__  )
#  __name__ is a special feature in python that allows us to track where files re called from
# When called directly or 'double clicked on', therefore NOT imported, __name__ = __main__
# when called from an import, __name__ = path.to.file.py
# this concepts is not use a lot, but you can make cool demos of your file :D
# meaning you can make your file behave differently when clicked on vs when imported from another program









# # tests for digit 3 div 3
three_div_three = 3 % 3 == 0
print('manual check if 3 is divisible by 3 = ' + str(three_div_three))
print('Function check = ' + str(check_if_digit_div_num(3, 3)))
print('Checking if function and manual are the same = ' + str(check_if_digit_div_num(3, 3) == three_div_three))

#tests for digit 4 div 3
four_div_three = 4 % 3 == 0
print('manual check if 4 is divisible by 3 = ' + str(four_div_three))
print('Function check = ' + str(check_if_digit_div_num(4, 3)))
print('Checking if function and manual are the same = ' + str(check_if_digit_div_num(4, 3) == four_div_three))



# tests for digit 5 div 5
five_div_five = 5 % 5 == 0
print('manual check if 5 is divisible by 5 = ' + str(five_div_five))
print('Function check = ' + str(check_if_digit_div_num(5, 5)))
print('Checking if function and manual are the same = ' + str(check_if_digit_div_num(5, 5) == five_div_five))


# # tests for digit 6 div 5
six_div_five = 6 % 5 == 0
print('manual check if 6 is divisible by 5 = ' + str(six_div_five))
print('Function check = ' + str(check_if_digit_div_num(6, 5)))
print('Checking if function and manual are the same = ' + str(check_if_digit_div_num(6, 5) == six_div_five))


# tests for digit 15 div 3
fifteen_div_three = 15 % 3 == 0
print('manual check if 15 is divisible by 3 = ' + str(fifteen_div_three))
print('Function check = ' + str(check_if_digit_div_num(15, 3)))
print('Checking if function and manual are the same = ' + str(check_if_digit_div_num(15, 3) == fifteen_div_three))

# tests for digit 15 div 5
fifteen_div_five = 15 % 5 == 0
print('manual check if 15 is divisible by 5 = ' + str(fifteen_div_five))
print('Function check = ' + str(check_if_digit_div_num(15, 5)))
print('Checking if function and manual are the same = ' + str(check_if_digit_div_num(15, 5) == fifteen_div_five))



if __name__ == '__main__':
    print('I was called directly')
    ## checking if num1 can be divide by num2
    print('We want to check if function "check_if_digit_div_num" works.\n'
          'To do this we try it manually then compare it with function')
    num1 = int(input('First number you want to check \n'))
    num2 = int(input('What number you want to divide by? \n'))

    manual_div = num1 % num2 == 0
    print('Manual check: \n' + str(manual_div))
    print('Function check: \n' + str(check_if_digit_div_num(num1, num2)))
    print('Checking if function and manual are the same: \n'
          + str(check_if_digit_div_num(num1, num2) == manual_div))