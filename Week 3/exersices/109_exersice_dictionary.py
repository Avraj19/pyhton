# Dictionary basics :D

#1 - Define a dictionary call story1, it should have the followign keys:
        # 'start', 'middle' and 'end'

story_line_vol1 = {
    'Hero': 'hero_name',
    'Beginning': 'In the beginning there was our god',
    'Middle': 'Then came the universe with all its glory',
    'End': 'After millions of years of peace there was war, that threaten the universe.'
}

#2 - Print the entire dictionary
print(story_line_vol1)

#3 - Print the type of your dictionary
print(type(story_line_vol1))

#4 - Print only the keys
print(story_line_vol1.keys())

#4 - print only the values
print(story_line_vol1.values())

#5 - print the individual values using the keys (individually, lots of printi commands)
print(story_line_vol1['End'])
#6 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero
story_line_vol1['Hero'] = 'Supermaaan'
print(story_line_vol1)