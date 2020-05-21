# section 1
name = input('Enter your name: ').capitalize().strip()
last_name = input('Enter your last name: ').capitalize().strip()
age = int(input('Enter your age: '))
age_of_mother = int(input('Enter your mothers age: '))

# section 2 print out information in format manor
print(name)
print(last_name)
print(age)
print(age_of_mother)

# section 3
age_dif = age_of_mother - age
print('The age difference between you and your mum is ' + str(age_dif))

# section 4
skill_list = []
skill_1 = skill_list.append(input('Enter your first skill: ').capitalize().strip())
skill_2 = skill_list.append(input('Enter your second skill: ').capitalize().strip())
skill_3 = skill_list.append(input('Enter your third skill: ').capitalize().strip())

# section 5
print('You have now received the following skills: ')
print(skill_list[0])
print(skill_list[1])
print(skill_list[2])
