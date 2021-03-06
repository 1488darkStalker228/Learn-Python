import os
import time

# свап значений с помощью оператора присвоения;
# var = 1
# var1 = 2
# var, var1 = var1, var
# print(var, var1)

# прибавление к переменной какого-либо числа;
# var11 = 1
# var11 += var
# print(var11)

# типа деструктурирующее присваивание;
# a, b, *c = [1, 2, 4, 5]
# print(a, b, c)

# Возврат типа;
# print(type([1, 2]))

# input - окно для ввода данных с клавиатуры;
# int - перевод строки в число;
# str - перевод числа в строку, есть так же float;
# a = input('Введите сообщение:')
# b = int(a) + 5
# print(b)

# Переводит булево значение условия в противоположное аналог "!" в JS;
# a = False
# if not a:
#   print('!')

# Поиск подстроки;
# print('22' in '3322322') - возвращает True, если подстрока присутствует
# print('228' not in '322') - возвращает True, если подстрока отсутствует


# Открыть двач;
# Задержка перед исполнением программы;
# site = input('Введите сайт: ')
# time.sleep(5)
# os.system('start ' + 'https://' + site)

# Факториал;
# def factorial(n):
#   counter = n - 1
#
#   while counter > 1:
#     n *= counter
#     counter -= 1
#   return n
#
# print(factorial(7))

# Цикл for;
# for i in [1, 2, 4]:
#   print(i)
# else:
#   print('залупа')

# word = input('Введите слово: ')
# letters = 'йфяцычувскамепинртгоьшлбщдюзжхэъё'
#
# for i in letters:
#   count = 0
#
#   for j in word:
#     if i == j:
#       count += 1
#
#   print(i, count)


# чтобы посчитать количество каждых букв в слове, нужно разделять искомое слово на буквы
# и сравнивать каждую букву из искомого слова с существующими буквами алфавита, при совпадении записывать в переменную
# совпавшую букву, при дальнейших итерациях, проверять, есть ли ещё совпадения

# Например, есть слово из 3-х букв "хуу". Перебираем в первом цикле само слово посимвольно(можно перебирать в первом цикле и алфавит).
# Во втором цикле перебираем алфавит. Во время итераций начинаем сравнивать символ из первого цикла с символами из второго цикла,
# совпадение будет.
# (Если в какой либо переменной уже присутствует буква, то увеличиваем счётчик на +1)
# (Что если сохранять i в отдельной переменной? Например )

# Аналог for i в JS. Обычный и обратный циклы;
# for i in range(0, 10, 2):
#   print(i)

# for i in range(10, -1, -1):
#   print(i)

# list = [1, 2, 4]
# list[0], list[1] = list[-1], list[-1]
# print(list[len(list) - 1])

# Превращаем строку в массив;
# print(list('llll'))


# lst = list(range(1, 21))
# lst1 = []
#
# for i in lst:
#   if i % 2 == 0:
#     lst1.append(i)
#     lst.remove(i)
#     # Заполнение массива
#     # lst += [i]
# else:
#   print(lst)
#   print(lst1)

# Тип данных кортеж. Кортеж - перечисление данных через запятую;
# x = (1, 2, 3, [1, 2])
# print(type(x[3]))
# print(tuple(range(11)))
# Берём срез;
# print(x[1:5])

# # Заполняем список названием файла + его путем. Таким образом просматриваем всё содержимое папки;
# list = []
# for address, dirs, files in os.walk('C:\\Users\Админ\OneDrive\Documents\ShareX\Screenshots'):
#    for file in files:
#      list.append(os.path.join(address, file))
#
# print(list)

########################################################################################################################

# # Изучение функций
# lst = [1, 2, 3]
# def calc_len(lst, count=0, val=False):
#     if val:
#         tmp = type(lst[0])
#         for i in lst:
#             count += 1
#         return count, tmp
#
#     for i in lst:
#         count += 1
#     return count
# # При вызове функции, можно передавать в неё аргументы не по порядку
# # Распаковывае кортеж в переменные
# a, b = calc_len(lst, val=True)
# print(a, b)

# C помощью '*' передаём в функцию кортеж
# def f(*args, key):
#     print(args)
#     print(key)
# f(1, 2, 3, key=10)

# Пример применения args и кортежей;
# def exclusive_it(*args, key=False):
#     lst = []
#     # Перебираем кортеж => 3 итерации
#     for i in args:
#         # Перебираем элементы кортежа, то есть списки
#         for j in i:
#             # Если элемент из перебираемого списка уже присутствует в результирующем массиве, то пропускаем итерацию
#             if j in lst:
#                 continue
#             # Пушим в массив уникальные элементы
#             lst.append(j)
#     if key:
#         lst.sort()
#     return lst
#
#
# a = [9, 8, 7]
# b = [8, 8, 9, 7, 6, 5]
# c = [1, 2, 3, 4, 5, 6, 7, 7]
#
# val = exclusive_it(a, b, c, key=True)
#
# print(val)

# 2:57:00

# def n():
#     x = 22
#     # Обращаемся к переменной из глобальной области видимости
#     global x
#     x = 22
#     print(x)
# n()

# x = 5
# def n():
#     x = 10
#     def n1():
#         # Используется только во вложенных функциях, при применении, x берется из родительской функции, а не создаётся по новой
#         nonlocal x
#         x = 100
#         print(x)
#     n1()
#     print(x)
# n()

########################################################################################################################

# # Изучаю словари
# d = {'a': 1, 'b': 2}
# d1 = {}
#
# for key, value in d.items():
#     d1[value] = key
#
# print(d1)

########################################################################################################################

# Тип данных 'Множество', содержит неупорядоченную коллекцию уникальных элементов, они имеют высокую скорость при
# объединении элементов;
# tmp = {1, 2, 4, 1, 'df'}
# tmp1 = list(range(100))
# tmp2 = list(range(50, 200))
# tmp3 = set(tmp1)
# tmp4 = tmp3.union(set(tmp2))
# print(tmp4)

########################################################################################################################

# Добавление в строку значения из переменной;
# enter = input('Введите слово:')
# str = f'{enter} do you love me'
# print(str)

########################################################################################################################

# При возникновении в try ошибки определённого типа, выполнится тот блок except, настройка которого соответствует типу
# случившейся ошибки;
# try:
#     tmp = float(input('Введите число:'))
#     # print(tmp / 0)
#     print(tmp)
# except ValueError:
#     print('Произошла ошибка')
# except ZeroDivisionError:
#     print('На 0 делить нельзя')
#     # Срабатывает, если в блоке try не было ошибок;
# else:
#     print('Сработал блок else')
#     # Выполнится в любом случае
# finally:
#     print('Выполнится в любом случае')

########################################################################################################################

# Декоратор - это функция, которая позволяет обернуть другую функцию в свой код, тем самым модифицировав её поведение;

# def decor(f):
#     def wrapper():
#         print('Код декоратора')
#         f()
#         print('Код декоратора 1')
#     return wrapper

# Это является особым синтаксом (расшифровка: f = decor(f)),
# Здесь мы меняем значение переменной f. До этого данная переменная была функцией, а теперь в ней лежит то, что вернет
# функция-декоратор, а она возвращает функцию, значит логична запись f();
# @decor
# def f():
#     enter = input('Ent smthng: ')
#     print(enter)
# f()

########################################################################################################################

# Генераторы

# def f():
#     list_text = []
#     with open('text.txt', encoding='utf-8') as r:
#         for i in r:
#             list_text.append(i)
#     return list_text

# def f():
#     with open('text.txt', encoding='utf-8') as r:
#         for i in r:
#             # Если прописан оператор yield, то интерпретатор python создаёт из этой функции объект-генератор,
#             # нужно для экономии памяти
#             yield i

########################################################################################################################

# var = lambda x: x * 5
#
# print(var(4))

