class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта книги.

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.

        :return: Строка формата 'Книга "название_книги"'.
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать точно такой же экземпляр.

        :return: Строка формата 'Book(id_=..., name=..., pages=...)'.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books: list[Book] = None):
        """
        Инициализация объекта библиотеки.

        :param books: Список книг. По умолчанию пустой список.
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку.

        :return: Идентификатор последней книги + 1 или 1, если книг нет.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с указанным id не существует.

        В методе get_index_by_book_id используется функция enumerate, которая возвращает пары (индекс, значение) для итерации по списку книг.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")

# Создаем несколько книг
book1 = Book(id_=1, name="1984", pages=328)
book2 = Book(id_=2, name="Мастер и Маргарита", pages=480)

# Создаем библиотеку и добавляем книги
library = Library([book1, book2])

# Проверяем методы
print(book1)  # Вывод: Книга "1984"
print(repr(book2))  # Вывод: Book(id_=2, name='Мастер и Маргарита', pages=480)

print(library.get_next_book_id())  # Вывод: 3 (следующий id для новой книги)

# Получаем индекс книги по id
try:
    index = library.get_index_by_book_id(2)
    print(f"Индекс книги с id=2: {index}")  # Вывод: Индекс книги с id=2: 1
except ValueError as e:
    print(e)

# Попытка получить индекс несуществующей книги
try:
    library.get_index_by_book_id(99)
except ValueError as e:
    print(e)  # Вывод: Книги с запрашиваемым id не существует

# Проверка создания книги
book = Book(id_=1, name="Тестовая книга", pages=100)
assert str(book) == 'Книга "Тестовая книга"'
assert repr(book) == "Book(id_=1, name='Тестовая книга', pages=100)"

# Проверка библиотеки
library = Library()
assert library.get_next_book_id() == 1

library.books.append(book)
assert library.get_next_book_id() == 2

assert library.get_index_by_book_id(1) == 0

try:
    library.get_index_by_book_id(99)
except ValueError as e:
    assert str(e) == "Книги с запрашиваемым id не существует"