class Vehicle:
    """
    Базовый класс для транспортных средств.

    Атрибуты:
        name (str): Название транспортного средства.
        max_speed (float): Максимальная скорость (км/ч).
    """

    def __init__(self, name: str, max_speed: float):
        """
        Инициализация транспортного средства.

        :param name: Название транспортного средства.
        :param max_speed: Максимальная скорость (км/ч).
        """
        self.name = name
        self.max_speed = max_speed

    def __str__(self) -> str:
        """
        Возвращает строковое представление транспортного средства.

        :return: Строка формата "Транспортное средство 'название', макс. скорость: max_speed км/ч".
        """
        return f'Транспортное средство "{self.name}", макс. скорость: {self.max_speed} км/ч'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать объект.

        :return: Строка формата "Vehicle(name='...', max_speed=...)".
        """
        return f"Vehicle(name='{self.name}', max_speed={self.max_speed})"

    def move(self) -> str:
        """
        Описывает движение транспортного средства.

        :return: Сообщение о движении.
        """
        return f"{self.name} движется со скоростью до {self.max_speed} км/ч."

class Car(Vehicle):
    """
    Класс для легковых автомобилей. Наследует класс Vehicle.

    Атрибуты:
        name (str): Название автомобиля.
        max_speed (float): Максимальная скорость (км/ч).
        passengers (int): Количество пассажиров.
    """

    def __init__(self, name: str, max_speed: float, passengers: int):
        """
        Инициализация легкового автомобиля.

        :param name: Название автомобиля.
        :param max_speed: Максимальная скорость (км/ч).
        :param passengers: Количество пассажиров.
        """
        super().__init__(name, max_speed)
        self.passengers = passengers

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        :return: Строка формата "Легковой автомобиль 'название', макс. скорость: max_speed км/ч, пассажиров: passengers".
        """
        return f'Легковой автомобиль "{self.name}", макс. скорость: {self.max_speed} км/ч, пассажиров: {self.passengers}'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать объект.

        :return: Строка формата "Car(name='...', max_speed=..., passengers=...)".
        """
        return f"Car(name='{self.name}', max_speed={self.max_speed}, passengers={self.passengers})"

    def honk(self) -> str:
        """
        Сигнал автомобиля.

        :return: Сообщение о сигнале.
        """
        return f"{self.name} подает сигнал: Би-бип!"

class Truck(Vehicle):
    """
    Класс для грузовых автомобилей. Наследует класс Vehicle.

    Атрибуты:
        name (str): Название грузовика.
        max_speed (float): Максимальная скорость (км/ч).
        cargo_capacity (float): Грузоподъемность (тонны).
    """

    def __init__(self, name: str, max_speed: float, cargo_capacity: float):
        """
        Инициализация грузового автомобиля.

        :param name: Название грузовика.
        :param max_speed: Максимальная скорость (км/ч).
        :param cargo_capacity: Грузоподъемность (тонны).
        """
        super().__init__(name, max_speed)
        self.cargo_capacity = cargo_capacity

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузовика.

        :return: Строка формата "Грузовик 'название', макс. скорость: max_speed км/ч, грузоподъемность: cargo_capacity т".
        """
        return f'Грузовик "{self.name}", макс. скорость: {self.max_speed} км/ч, грузоподъемность: {self.cargo_capacity} т'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать объект.

        :return: Строка формата "Truck(name='...', max_speed=..., cargo_capacity=...)".
        """
        return f"Truck(name='{self.name}', max_speed={self.max_speed}, cargo_capacity={self.cargo_capacity})"

    def load_cargo(self, weight: float) -> str:
        """
        Загрузка груза в грузовик.

        :param weight: Вес груза (тонны).
        :return: Сообщение о загрузке.
        :raises ValueError: Если вес груза превышает грузоподъемность.
        """
        if weight > self.cargo_capacity:
            raise ValueError("Вес груза превышает грузоподъемность.")
        return f"{self.name} загружен {weight} т груза."

# Создание объектов
car = Car("Toyota Camry", 220, 4)
truck = Truck("Volvo FH16", 120, 20)

# Вывод строкового представления
print(car)  # Легковой автомобиль "Toyota Camry", макс. скорость: 220 км/ч, пассажиров: 4
print(truck)  # Грузовик "Volvo FH16", макс. скорость: 120 км/ч, грузоподъемность: 20 т

# Вывод repr
print(repr(car))  # Car(name='Toyota Camry', max_speed=220, passengers=5)
print(repr(truck))  # Truck(name='Volvo FH16', max_speed=120, cargo_capacity=20)

# Использование методов
print(car.move())  # Toyota Camry движется со скоростью до 220 км/ч.
print(car.honk())  # Toyota Camry подает сигнал: Би-бип!

print(truck.move())  # Volvo FH16 движется со скоростью до 120 км/ч.
print(truck.load_cargo(15))  # Volvo FH16 загружен 15 т груза.