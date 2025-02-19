class Book:
    def __init__(self, name: str, author: str):
        """
        Инициализация базового класса книги.

        :param name: Название книги.
        :param author: Автор книги.
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """
        Возвращает название книги.

        :return: Название книги.
        """
        return self._name

    @property
    def author(self) -> str:
        """
        Возвращает автора книги.

        :return: Автор книги.
        """
        return self._author

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка формата "Книга 'название' автор: автор".
        """
        return f'Книга "{self.name}" автор: {self.author}'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать объект.

        :return: Строка формата "Book(name='...', author='...')".
        """
        return f"Book(name='{self.name}', author='{self.author}')"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация класса бумажной книги.

        :param name: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц (целое число, больше 0).
        """
        super().__init__(name, author)
        self.pages = pages  # Используем setter для проверки

    @property
    def pages(self) -> int:
        """
        Возвращает количество страниц.

        :return: Количество страниц.
        """
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """
        Устанавливает количество страниц с проверкой.

        :param value: Количество страниц (целое число, больше 0).
        :raises ValueError: Если количество страниц меньше или равно 0.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть целым числом больше 0.")
        self._pages = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление бумажной книги.

        :return: Строка формата "Бумажная книга 'название' автор: автор, страниц: pages".
        """
        return f'Бумажная книга "{self.name}" автор: {self.author}, страниц: {self.pages}'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать объект.

        :return: Строка формата "PaperBook(name='...', author='...', pages=...)".
        """
        return f"PaperBook(name='{self.name}', author='{self.author}', pages={self.pages})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация класса аудиокниги.

        :param name: Название книги.
        :param author: Автор книги.
        :param duration: Продолжительность аудиокниги (число с плавающей точкой, больше 0).
        """
        super().__init__(name, author)
        self.duration = duration  # Используем setter для проверки

    @property
    def duration(self) -> float:
        """
        Возвращает продолжительность аудиокниги.

        :return: Продолжительность аудиокниги.
        """
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """
        Устанавливает продолжительность аудиокниги с проверкой.

        :param value: Продолжительность аудиокниги (число с плавающей точкой, больше 0).
        :raises ValueError: Если продолжительность меньше или равна 0.
        """
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Продолжительность должна быть числом больше 0.")
        self._duration = float(value)

    def __str__(self) -> str:
        """
        Возвращает строковое представление аудиокниги.

        :return: Строка формата "Аудиокнига 'название' автор: автор, продолжительность: duration".
        """
        return f'Аудиокнига "{self.name}" автор: {self.author}, продолжительность: {self.duration} ч.'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать объект.

        :return: Строка формата "AudioBook(name='...', author='...', duration=...)".
        """
        return f"AudioBook(name='{self.name}', author='{self.author}', duration={self.duration})"

# Создаем объекты
paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 12.5)

# Выводим строковое представление
print(paper_book)  # Бумажная книга "1984" автор: Джордж Оруэлл, страниц: 328
print(audio_book)  # Аудиокнига "Мастер и Маргарита" автор: Михаил Булгаков, продолжительность: 12.5 ч.

# Выводим repr
print(repr(paper_book))  # PaperBook(name='1984', author='Джордж Оруэлл', pages=328)
print(repr(audio_book))  # AudioBook(name='Мастер и Маргарита', author='Михаил Булгаков', duration=12.5)

# Попытка изменить name или author вызовет ошибку
try:
    paper_book.name = "Новое название"
except AttributeError as e:
    print(e)  # can't set attribute

# Попытка задать некорректное значение pages или duration
try:
    paper_book.pages = -10
except ValueError as e:
    print(e)  # Количество страниц должно быть целым числом больше 0.

try:
    audio_book.duration = 0
except ValueError as e:
    print(e)  # Продолжительность должна быть числом больше 0.