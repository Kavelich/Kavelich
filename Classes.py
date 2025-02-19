import doctest

class Furniture:

    def __init__(self, material: str, weight: float):
        """
        Инициализация объекта мебели.

        :param material: material, из которого сделана мебель.
        :param weight: weight мебели в килограммах.
        :raises ValueError: Если weight меньше или равен 0.
        """
        if weight <= 0:
            raise ValueError("weight должен быть положительным числом.")
        self.material = material
        self.weight = weight


    def assemble(self) -> str:
        """
        Собрать мебель.

        :return: Сообщение о том, что мебель собрана.
        """
        ...

    def move(self, new_place: str) -> str:
        """
        Переместить мебель в новое место.

        :param новое_место: Название нового места.
        :return: Сообщение о перемещении.
        """

class Tree:
    """
    Абстрактный класс, описывающий дерево.
    """

    def __init__(self, type: str, height: float):
        """
        Инициализация объекта дерева.

        :param type: Вид дерева.
        :param height: Высота дерева в метрах.
        :raises ValueError: Если высота меньше или равна 0.
        """
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        self.type = type
        self.height = height


    def grow(self, age: int) -> float:
        """
        Вычислить новую высоту дерева через определенное количество лет.

        :param age: Количество лет для роста.
        :return: Новая высота дерева.
        """
     
    def cut(self) -> str:
        """
        Срубить дерево.

        :return: Сообщение о том, что дерево срублено.
        """


class Social_Network:
    """
           Абстрактный класс, описывающий социальную сеть.
           """

    def __init__(self, name: str, count_of_users: int):
        """
        Инициализация объекта социальной сети.

        :param name: Название социальной сети.
        :param количество_пользователей: Количество пользователей в сети.
        :raises ValueError: Если количество пользователей меньше 0.
        """
        if count_of_users < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        self.name = name
        self.count_of_users = count_of_users

    def add_user(self, username: str) -> str:
        """
        Добавить нового пользователя в социальную сеть.

        :param username: Имя нового пользователя.
        :return: Сообщение о добавлении пользователя.
        """


    def delete_user(self, username: str) -> str:
        """
        Удалить пользователя из социальной сети.

        :param имя: Имя пользователя для удаления.
        :return: Сообщение об удалении пользователя.
        """

# Пример использования класса Мебель
class Table(Furniture):
    def assemble(self) -> str:
        return "Стол собран."

    def move(self, new_place: str) -> str:
        return f"Стол перемещен в {new_place}."


Table = Table("дерево", 15)
print(Table.assemble())
print(Table.move("кухня"))

# Пример doctest для метода собрать класса Стол
"""
>>> стол = Стол("дерево", 15)
>>> стол.собрать()
'Стол собран.'
"""


# Пример использования класса Дерево
class Oak(Tree):
    def grow(self, age: int) -> float:
        return self.height + age * 0.5

    def cut(self) -> str:
        return "Дуб срублен."


Oak = Oak("дуб", 10)
print(Oak.grow(5))
print(Oak.cut())

# Пример doctest для метода расти класса Дуб
"""
>>> дуб = Дуб("дуб", 10)
>>> дуб.расти(5)
12.5
"""

# Пример использования класса СоциальнаяСеть
class Facebook(Social_Network):
    def add_user(self, name: str) -> str:
        self.count_of_users += 1
        return f"Пользователь {name} добавлен в Facebook."

    def delete_user(self, name: str) -> str:
        self.count_of_users -= 1
        return f"Пользователь {name} удален из Facebook."

fb = Facebook("Facebook", 2000000000)
print(fb.add_user("Иван"))
print(fb.delete_user("Иван"))


# Пример doctest для метода добавить_пользователя класса Facebook
"""
>>> fb = Facebook("Facebook", 2000000000)
>>> fb.добавить_пользователя("Иван")
'Пользователь Иван добавлен в Facebook.'
"""

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации