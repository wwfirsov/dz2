x = 1
while x == 1:
    reyting = [7, 5, 3, 3, 2]
    print("Исходный рейтинг:", reyting)
    for el in reyting:
        element_reyting = int(input('Введите новый элемент рейтинга (Натуральное число): '))
        if element_reyting > el:
            pos = reyting.index(el)
            reyting.insert(pos, element_reyting)
            print("Новый рейтинг:", reyting)
            х = int(input("Если хотите повторить, введите 1, если хотите выйти, введите 0:", ))
            if x != 1:
                print("Программа завершена")
        elif element_reyting == el:
            pos = reyting.index(el) + reyting.count(el)
            reyting.insert(pos, element_reyting)
            print("Новый рейтинг:", reyting)
            х = int(input("Если хотите повторить, введите 1, если хотите выйти, введите 0:", ))
            if x != 1:
                print("Программа завершена")
        else:
            pos = el
            reyting.insert(pos, element_reyting)
            print("Новый рейтинг:", reyting)
            х = int(input("Если хотите повторить, введите 1, если хотите выйти, введите 0:", ))
            if x != 1:
                print("Программа завершена")