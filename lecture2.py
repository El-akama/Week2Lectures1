# from copy import deepcopy
# список это тип данных который хранит в себе последовательность элемнетов(любых элементов)
# nums = [1, [2, 3, 4, [5, 6, 7]], 3, 4,]
# nums.append(6)              # добавляет элемент в лист
# print(nums)
# nums.pop()                  # удаляет элемент в листе
# print(nums[1][3][1])        # можно делать и так(поиск разных элементов(списки внутри списков))

# prod1 = "iphone12"
# prod2 = "samsungs23"
# korzina = [prod1, prod2]

# spisok1 =[1, 2, 3]
# name = "baha"
# spisok2 = list(name)
# print(spisok2)

# spisok = ['name', 'makers', True, 2, [3, 2, 4, 5], 2, 'name', 2]
# spisok2 = [0, 9, 8, 7, 6]
# spisok.clear()                                      # очищает список
# new_spisok = spisok.copy()                              # копирует список поверхностно(копирует только совсем внутренние объекты)
# new_spisok[4][0] = "new word"                         # коприует все, но изменяет только элементы подлистов
# print(spisok)
# print(new_spisok)

# new_spisok = spisok.copy()                          # но не изменяет головные элементы списка
# spisok[3] = 'word'
# print(spisok)
# print(new_spisok)

# new_spisok = deepcopy(spisok)               # полное копирование 
# spisok[4][1] = 'word'
# print(spisok)
# print(new_spisok)

# num = spisok.count(2)               # считает кол-во одинаковых элементов, но не в подлистах       
# print(num)

# spisok.extend(spisok2)              # расширяет один список другим списком ( конкатенация )
# print(spisok)

# spisok3 = spisok + spisok2
# print(spisok3)

# num = spisok.index(2, 7)                # возвращает индекс элемента (первый попавшийся, который ищем)
# print(num)

# spisok.insert(3, 'indexed')             # добавляет элемент
# print(spisok)


# spisok.pop()                            # удаляет элемент из списка(по умолчанию с конца) по индексу                     
# item = spisok.pop(1)                    # если присвоить, то этот элемент идет как переменная
# print(item)
# print(spisok)

# spisok.remove('name')                   # удаляет объекты(по умолчанию первый) по названию
# print(spisok)

# spisok.reverse()                    #  просто реверс
# print(spisok)

# spisok = [4, 2, 7, 9, 6, 1, 3, 5, 0, 8]             # сортировка по умолчанию False
# spisok.sort(reverse=True)
# print(spisok)

# spisok = ['abc', 'bcd', 'dfdf', 'rytghf']
# spisok.sort(key=len, reverse=True)                  # сортирует по длинне 
# print(spisok)

# print(spisok[1:3])        # можно слайсить списки