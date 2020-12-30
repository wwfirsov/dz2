stroka = input('Введите строку из нескольких слов: ')
stroka = list(stroka.split(" "))

for ind, el in enumerate(stroka):
    print(ind, el[:10])

# for ind, el in stroka:
#     print(ind, el)