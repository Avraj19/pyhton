
# Write a bizz and zzuu game ##project

# as a user I should be prompted for a number, as the program will print all the number up to and including said
# number while following the constraints / specs. (bizz and buzz for multiples or 3 and 5)

# As a user I should be able to keep giving the program different numbers and it will calculate appropriately until
# you use the key word: 'penpinapplespen'

# count_num = 0
# while True:
#
#     user_input = int(input('what is the next number? \n'))
#     count_num += 1
#     if user_input == count_num:
#         if user_input % 15 == 0:
#             print('bizzzzuu')
#
#         elif user_input % 3 == 0:
#             print('bizz')
#
#         elif user_input % 5 == 0:
#             print('zzuuu')
#
#         elif user_input == 'penpinapplespen':
#             print('zzuuu')
#
#         else:
#             print(user_input)
#
#     else:
#         print('')


def bizzzzuuugame(user_input):
    for num in range(1, user_input + 1):

        if num % 15 == 0:
            print('bizzzzuuu')
        elif num % 3 == 0:
            print('bizz')

        elif num % 5 == 0:
            print('zzuuu')

        else:
            print(num)

def check15(num):
    if num % 15 == 0:
        print('bizzzzuu')

def check3(num):
    if num % 3 == 0:
        print('bizz')

def check5(num):
    if num % 5 == 0:
        print('zzuu')


while True:
    print('If you want to play the game type Y\n '
          'to exit game type N')
    play = input('Do you want to play BIZZZZUU?\n').lower().strip()
    if play == 'y':
        user_input = int(input('what number do you want to play till? \n'))
        bizzzzuuugame(user_input)
        # for num in range(1, user_input + 1):
        #     check15(num)
        #     check3(num)
        #     check5(num)
    elif play == 'n':
        break

# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu


#  EXTRA:
#  Make it functional
#  make it so I can it so it can work with 4 and 9 insted of 3 and 5.
    #      make it so it can work with any number!

# while True:
#     user_input2 =input('fghnm')
#
#     for num in range(1, user_input2 +1):
#         if num % 3 == 0:
#             print('asdf')

        # user_input = int(input('what number do you want to play till? \n'))
        # for num in range(1, user_input + 1):
        #     print(num)
        #
        #     if num % 15 == 0:
        #         print('bizzzzuuu')
        #     elif num % 3 == 0:
        #             print('bizz')
        #
        #     elif num % 5 == 0:
        #         print('zzuuu')
        #
        #     else:
        #         print(num) ## all you need is these 2 lines of code