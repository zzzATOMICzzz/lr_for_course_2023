"""
Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и
вызвав описанный метод.
"""
from abc import abstractmethod, ABC
from time import sleep
from datetime import datetime as dt


class TrafficLight:
    _states = {"красный": 7, "желтый": 2, "зеленый": 5}
    _color = ""

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color
            start_state_time = dt.now()

            print(f"Состояние светофора: '{self._color}' в течении {sw_time} секунд")

            sleep(sw_time)

            print(
                f"Остановка состояние светофора: '{self._color}' после {(dt.now() - start_state_time).seconds} секунд")


tl = TrafficLight()
tl.running()
print()

"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _weight: float = 0.02

    def __init__(self, length: [int, float], width: [int, float]):
        self._length = float(length)
        self._width = float(width)

    def get_weight(self, depth: float) -> [float, None]:
        return self._length * self._width * depth * self._weight


road = Road(5000, 20)
print(f"Масса дорожного покрытия составит: {road.get_weight(5)} тонн")
print()

"""
Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}. Создать класс Position (должность) на базе класса
Worker. В классе Position реализовать методы получения полного имени
сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).
"""


class Worker:
    def __init__(
            self,
            name: str,
            surname: str,
            pos: str,
            wage: float = 0,
            bonus: float = 0
    ):
        self.name = name
        self.surname = surname
        self.pos = pos
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


data = [
    {
        'name': 'Alexander',
        'surname': 'Ivanov',
        'pos': 'Dev',
        'wage': 40000,
        'bonus': 5000
    },
    {
        'name': 'Ivan',
        'surname': 'Petrov',
        'pos': 'Tester',
        'wage': 90000,
        'bonus': 15000
    },
    {
        'name': 'Denis',
        'surname': 'Killer',
        'pos': 'SMM',
        'wage': 60000,
        'bonus': 30000
    },
]

for row_data in data:
    temp = Position(**row_data)

    print(f"Имя: {temp.name}")
    print(f"Фамилия: {temp.surname}")
    print(f"ФИО: {temp.get_full_name()}")
    print(f"Позиция: {temp.pos}")
    print(f"Доход: {temp.get_total_income()}")
    print('#######################################')
print()

"""
Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go,
stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
show_speed, который должен показывать текущую скорость автомобиля. Для
классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните
доступ к атрибутам, выведите результат. Выполните вызов методов и также
покажите результат.
"""


class Car:
    _direction = None

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True if is_police else False

    def go(self, speed):
        self.speed = float(speed)

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        if direction.upper() not in ('ВЛЕВО', 'ВПРАВО'):
            print(f"Неверное направление: {direction}")
            return

        if not self.speed:
            print(f"Невозможно определить направление, т.к. {self.name} стоит на месте")
            return

        self._direction = direction

    def show_speed(self):
        print(f"Текущая скорость автомобилья {self.name}: {self.speed} км/ч")


class TownCar(Car):
    MAX_SPEED = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f"Превышение скорости автомобилем {self.name}!")
        print(f"Текущая скорость автомобилья {self.name}: {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    MAX_SPEED = 105

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > self.MAX_SPEED:
            print(f"Превышение скорости автомобилем {self.name}!")
        print(f"Текущая скорость автомобилья {self.name}: {self.speed} км/ч")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


pc = PoliceCar(100, 'Синий', 'Audi X8')
wc1 = WorkCar(50, 'Зеленый', 'BMW X5')
wc2 = WorkCar(120, 'Красный', 'VAZ 2101')
sc = SportCar(110, 'Желтый', 'ZAZ 2600')
tc1 = TownCar(90, 'Серый', 'ZIL 2111')
tc2 = TownCar(65, 'Серый', 'MERS SL550')
pc.show_speed()
pc.go(95)
pc.show_speed()
pc.stop()
print(pc.color)
pc.go(90)
print(pc.name)
pc.show_speed()
wc1.go(80)
sc.go(70)
tc1.go(65)
tc2.go(55)
wc1.show_speed()
wc2.show_speed()
sc.show_speed()
tc1.show_speed()
tc2.show_speed()
print()

"""
Реализовать класс Stationery (канцелярская принадлежность). Определить
в нем атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
переопределение метода draw. Для каждого из классов методы должен
выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery(ABC):
    def __init__(self, title):
        self._title = title

    @abstractmethod
    def draw(self):
        pass


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self._title} пишет")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self._title} чертит")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"{self._title} штрихует")

pen = Pen("Ручка")
pen.draw()

pencil = Pencil("Карандаш")
pencil.draw()

handle = Handle("Маркер")
handle.draw()
