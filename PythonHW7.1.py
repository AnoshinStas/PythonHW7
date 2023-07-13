def vowel_count(str):
    vowel_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    count = 0
    for i in str:
        if i in vowel_list: count +=1
    return count

poem = input('введите стих: ')
poem = poem.split()
if len(set(map(vowel_count,poem))) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам') 