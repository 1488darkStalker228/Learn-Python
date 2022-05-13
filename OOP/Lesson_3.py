from datetime import datetime as dt


class Player:
    # Это константы, являются свойствами самого класса;
    __LVL, __HEALTH = 1, 100
    # Разрешённые свойства экземпляра. Добавить экземпляру другие свойства - не получится;
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    # Это геттер, он возвращает значение инкапсулированного свойства. Property может существовать без сеттера,
    # но сеттер без property - нет;
    @property
    def lvl(self):
        return self.__lvl

    # Это сеттер, он изменяет значение инкапсулированных свойств;
    @lvl.setter
    def lvl(self, num):
        self.__lvl += Player.__check_type(num)

    # Декоратор - классметод. Он взаимодействует не с экземплярами, а с методами класса. В параметр cls попадает имя
    # класса, который запускается;
    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = Player.__check_type(lvl)
        cls.__HEALTH = Player.__check_type(health)

    # Например, нам необходима функция, которая будет проверять допустимость присваиваемых значений в классметоде и в
    # сеттере;
    @staticmethod
    def __check_type(val):
        # Данная функция проверяет значение переменной на соответствие какому-либо типу данных;
        if isinstance(val, int):
            return val
        raise TypeError ('Должно быть число')


Player.set_cls_field(10, 3000000000)
x = Player()
print(x.lvl)










































