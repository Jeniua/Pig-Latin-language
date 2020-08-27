while True:
    sentence = input('Eneter sentence to translate: ')
    if not sentence:
        print('Bye bye')
        break
    new = ''
    for element in sentence.split():
            if element[0] in 'aeiou':
                new += element + 'way '
            else:
                new += element[1:] + element[0] + 'ay '
    print(new)
