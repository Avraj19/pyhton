# section 7
hero_name = input('Enter the name of your hero: ').strip().capitalize()
# section 1
story_line_vol1 = {
    'Hero': hero_name,
    'Beginning': 'In the beginning there was our god',
    'Middle': 'Then came the universe with all its glory',
    'End': 'After millions of years of peace there was war, that threaten the universe.'
}

story_line_vol2 = {
    'Beginning': 'The war raged on',
    'Middle': 'God was captured by and week by his sister the darkness ',
    'End': hero_name + ', Sam, the devil, the angels and some witch teamed up to free god and defeated the darkness'
}

story_collection = {
    'vol1': story_line_vol1,
    'vol2': story_line_vol2
}
# setion 3
#print(story_collection)

# section 4
print(story_line_vol1.keys())

# section 5
print(story_line_vol2.values())

# setion 6
print(story_line_vol1['Beginning'])
print(story_line_vol1['Middle'])
print(story_line_vol1['End'])


