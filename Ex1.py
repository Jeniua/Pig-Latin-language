def pig_latin():
    while True:
        word = input('Enter word for translate: ')
        if not word:
            print('End')
            break
        if word[0] in 'aeiou':
            print(word + 'way')
        else:
            print(f'{word[1:]}{word[0]}ay')

pig_latin()
