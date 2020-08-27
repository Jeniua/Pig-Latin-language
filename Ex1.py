def pig_latin():
    word = input('Enter word for translate: ')
    if word[0] in 'aeiou':
        return word + 'way'

    else:
        return f'{word[1:]}{word[0]}ay'

print(pig_latin())
