# %% [markdown]
# ### Лабораторная работа: ООП и словари в Python

# %% [markdown]
# ## Задание 1. Кнопка Button
#
# Класс, считающий число нажатий: `click()`, `click_count()`, `reset()`.

# %%
class Button:
    def __init__(self):
        self._count = 0

    def click(self):
        self._count += 1

    def click_count(self):
        return self._count

    def reset(self):
        self._count = 0

# %%
button = Button()
button.click()
print(button.click_count())

button = Button()
button.click()
button.click()
print(button.click_count())
button.click()
print(button.click_count())

button = Button()
button.click()
button.click()
print(button.click_count())
button.reset()
button.click()
print(button.click_count())

# %% [markdown]
# ## Задание 2. Весы Balance
#
# `add_right`/`add_left` кладут груз на чашу, `result()` возвращает `=`, `R` или `L`.

# %%
class Balance:
    def __init__(self):
        self._left = 0
        self._right = 0

    def add_right(self, weight):
        self._right += weight

    def add_left(self, weight):
        self._left += weight

    def result(self):
        if self._left == self._right:
            return "="
        return "R" if self._right > self._left else "L"

# %%
balance = Balance()
balance.add_right(10)
balance.add_left(9)
balance.add_left(2)
print(balance.result())

balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())

# %% [markdown]
# ## Задание 3. BoundingRectangle
#
# Минимальный прямоугольник, охватывающий все добавленные точки.

# %%
class BoundingRectangle:
    def __init__(self):
        self._xs = []
        self._ys = []

    def add_point(self, x, y):
        self._xs.append(x)
        self._ys.append(y)

    def left_x(self):
        return min(self._xs)

    def right_x(self):
        return max(self._xs)

    def bottom_y(self):
        return min(self._ys)

    def top_y(self):
        return max(self._ys)

    def width(self):
        return self.right_x() - self.left_x()

    def height(self):
        return self.top_y() - self.bottom_y()

# %%
rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())

rect = BoundingRectangle()
rect.add_point(10, 20)
rect.add_point(5, 7)
rect.add_point(6, 3)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())

# %% [markdown]
# ## Задание 4. FoodInfo
#
# Пищевая ценность продукта; сложение двух `FoodInfo` даёт новый объект.

# %%
class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self._proteins = proteins
        self._fats = fats
        self._carbohydrates = carbohydrates

    def get_proteins(self):
        return self._proteins

    def get_fats(self):
        return self._fats

    def get_carbohydrates(self):
        return self._carbohydrates

    def get_kcalories(self):
        return 4 * self._proteins + 9 * self._fats + 4 * self._carbohydrates

    def __add__(self, other):
        return FoodInfo(
            self._proteins + other._proteins,
            self._fats + other._fats,
            self._carbohydrates + other._carbohydrates,
        )

# %%
food1 = FoodInfo(100, 100, 100)
food2 = FoodInfo(50, 60, 70)
food3 = food1 + food2
print(food1.get_proteins(), food1.get_fats(), food1.get_carbohydrates(), food1.get_kcalories())
print(food2.get_proteins(), food2.get_fats(), food2.get_carbohydrates(), food2.get_kcalories())
print(food3.get_proteins(), food3.get_fats(), food3.get_carbohydrates(), food3.get_kcalories())

food1 = FoodInfo(1, 2, 3)
food2 = FoodInfo(10, 20, 30)
food3 = food1 + food2
food4 = food2 + food1
print(food3.get_proteins(), food3.get_fats(), food3.get_carbohydrates(), food3.get_kcalories())
print(food4.get_proteins(), food4.get_fats(), food4.get_carbohydrates(), food4.get_kcalories())

# %% [markdown]
# ## Задание 5. Table (двумерная таблица)

# %%
class Table:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._data = [[0] * cols for _ in range(rows)]

    def get_value(self, row, col):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self._data[row][col]
        return None

    def set_value(self, row, col, value):
        self._data[row][col] = value

    def n_rows(self):
        return self._rows

    def n_cols(self):
        return self._cols

# %%
tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()

# %% [markdown]
# ## Задание 6. UserMail
#
# `__email` — защищённый атрибут; сеттер принимает почту, только если в ней ровно
# один `@` и после него есть точка.

# %%
class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str) and new_email.count('@') == 1 and '.' in new_email.split('@')[1]:
            self.__email = new_email
        else:
            print(f"ErrorMail:{new_email}")

    email = property(get_email, set_email)

# %%
k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3]  # ErrorMail:[1, 2, 3]
k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait

# %% [markdown]
# ## Задание 7. Money
#
# Хранит состояние в `total_cents`; `dollars`/`cents` — свойства с валидацией.

# %%
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    def get_dollars(self):
        return self.total_cents // 100

    def set_dollars(self, new_dollars):
        if isinstance(new_dollars, int) and new_dollars >= 0:
            self.total_cents = new_dollars * 100 + self.cents
        else:
            print("Error dollars")

    dollars = property(get_dollars, set_dollars)

    def get_cents(self):
        return self.total_cents % 100

    def set_cents(self, new_cents):
        if isinstance(new_cents, int) and 0 <= new_cents < 100:
            self.total_cents = self.dollars * 100 + new_cents
        else:
            print("Error cents")

    cents = property(get_cents, set_cents)

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"

# %%
Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents)  # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

# %% [markdown]
# ## Задание 8. Date
#
# `date` — `дд/мм/гггг`, `usa_date` — `мм-дд-гггг` (год дополняется нулями до 4 знаков).

# %%
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def date(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"

    @property
    def usa_date(self):
        return f"{self.month:02d}-{self.day:02d}-{self.year:04d}"

# %%
d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date)      # 05/10/2001
print(d1.usa_date)  # 10-05-2001
print(d2.date)      # 15/03/0999
print(d2.usa_date)  # 03-15-0999

# %% [markdown]
# ## Задание 9. Employee (атрибуты экземпляра + атрибуты класса)
#
# Написать класс `Employee` (Сотрудник):
# - атрибут класса `company` со значением `"Stepik"`;
# - `__init__` принимает `name` и `position` и сохраняет их как атрибуты экземпляра;
# - метод `get_info()` возвращает строку `"[name] работает в компании [company] на должности [position]."`,
#   используя и атрибуты экземпляра, и атрибут класса.

# %%
class Employee:
    company = "Stepik"

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} работает в компании {self.company} на должности {self.position}."

# %% [markdown]
# Проверим на примере:

# %%
e = Employee("Иван Иванов", "инженер")
e.get_info()

# %% [markdown]
# Атрибут класса `company` общий для всех экземпляров:

# %%
e2 = Employee("Пётр Петров", "менеджер")
e2.get_info(), Employee.company, e.company is e2.company

# %% [markdown]
# ## Задание 10. Person — сеттер, используемый уже в `__init__`
#
# Возраст устанавливается только через `set_age`, включая первоначальную установку.

# %%
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = 0
        self.set_age(age)

    def set_age(self, new_age):
        if 0 <= new_age <= 120:
            self._age = new_age

    def get_age(self):
        return self._age

# %%
p = Person("Анна", 30)
print(p.name, p.get_age())
p.set_age(200)   # некорректно, возраст не меняется
print(p.get_age())
p2 = Person("Илья", -5)  # некорректный возраст при создании -> остаётся значение по умолчанию 0
print(p2.get_age())

# %% [markdown]
# ## Задание 11. SpaceShip
#
# `agency` и `total_ships` — атрибуты класса; `set_personal_agency` создаёт
# персональный атрибут экземпляра, перекрывающий атрибут класса только для него.

# %%
class SpaceShip:
    agency = "Python Space"
    total_ships = 0

    def __init__(self, name, max_fuel):
        self.name = name
        self.max_fuel = max_fuel
        self.current_fuel = 0
        SpaceShip.total_ships += 1

    def refuel(self, amount):
        if self.current_fuel + amount <= self.max_fuel:
            self.current_fuel += amount
            print(f"{self.name}: заправлено {amount} ед. топлива")
        else:
            print(f"{self.name}: топливный бак переполнен")

    def fly(self, fuel_cost):
        if self.current_fuel >= fuel_cost:
            self.current_fuel -= fuel_cost
            print(f"{self.name}: полет выполнен, потрачено {fuel_cost} ед. топлива")
        else:
            print(f"{self.name}: недостаточно топлива")

    def show_info(self):
        print(f"Корабль {self.name} | Агентство: {self.agency} | Топливо: {self.current_fuel}/{self.max_fuel}")

    def set_personal_agency(self, agency):
        self.agency = agency

# %% [markdown]
# Программа по условию (10 строк входных данных):

# %%
def run_spaceship_program(lines):
    name1, max_fuel1, name2, max_fuel2, refuel1, refuel2, fly1, fly2, new_agency, personal_agency = lines
    ship1 = SpaceShip(name1, int(max_fuel1))
    ship2 = SpaceShip(name2, int(max_fuel2))
    ship1.refuel(int(refuel1))
    ship2.refuel(int(refuel2))
    SpaceShip.agency = new_agency
    ship1.set_personal_agency(personal_agency)
    ship1.fly(int(fly1))
    ship2.fly(int(fly2))
    ship1.show_info()
    ship2.show_info()
    print(f"Всего кораблей: {SpaceShip.total_ships}")

# %%
sample_input = ["Alpha", "50", "Beta", "40", "50", "40", "50", "10", "Star Alliance", "Alpha Team"]
run_spaceship_program(sample_input)

# %% [markdown]
# ## Задание 12. Наследование классов — проверка "является предком"
#
# По описанию наследования строим для каждого класса множество предков (себя и
# всех классов, от которых он наследуется прямо или косвенно), затем отвечаем на
# запросы `<A> <B>` — является ли `A` предком `B`.

# %%
def is_ancestor_all(class_lines, query_lines):
    parents = {}
    for line in class_lines:
        if ':' in line:
            name, rest = line.split(':', 1)
            parents[name.strip()] = rest.split()
        else:
            parents[line.strip()] = []

    memo = {}

    def ancestors(cls):
        if cls in memo:
            return memo[cls]
        result = {cls}
        for p in parents.get(cls, []):
            result |= ancestors(p)
        memo[cls] = result
        return result

    answers = []
    for line in query_lines:
        a, b = line.split()
        answers.append("Yes" if a in ancestors(b) else "No")
    return answers

# %%
class_lines = ["A", "B : A", "C : A", "D : B C"]
query_lines = ["A B", "B D", "C D", "D A"]
for ans in is_ancestor_all(class_lines, query_lines):
    print(ans)

# %% [markdown]
# ## Задание 13. Частота букв в строке
#
# Подсчитать количество каждой буквы и отсортировать: а) по алфавиту, б) по возрастанию частоты.

# %%
from collections import Counter

def letter_frequency(text):
    counts = Counter(ch for ch in text.lower() if ch.isalpha())
    by_alphabet = sorted(counts.items())
    by_frequency = sorted(counts.items(), key=lambda kv: kv[1])
    return counts, by_alphabet, by_frequency

# %%
counts, by_alphabet, by_frequency = letter_frequency("abracadabra")
print("По алфавиту:", by_alphabet)
print("По возрастанию частоты:", by_frequency)

# %% [markdown]
# ## Задание 14. Англо-русский словарь с вариантами переводов
#
# Каждому слову соответствует список возможных переводов.

# %%
english_russian = {}

def add_translation(word, translation):
    english_russian.setdefault(word, [])
    if translation not in english_russian[word]:
        english_russian[word].append(translation)

def translate(word):
    return english_russian.get(word, [])

# %%
add_translation("bank", "банк")
add_translation("bank", "берег")
add_translation("spring", "весна")
add_translation("spring", "пружина")
add_translation("spring", "родник")

print(translate("bank"))
print(translate("spring"))
print(translate("unknown"))

# %% [markdown]
# ## Задание 15. В какой стране находится город?

# %%
city_to_country = {
    "Paris": "Франция",
    "Berlin": "Германия",
    "Tokyo": "Япония",
    "Moscow": "Россия",
    "Rome": "Италия",
}

def get_country(city):
    return city_to_country.get(city, "Неизвестно")

# %%
for city in ["Paris", "Tokyo", "Atlantis"]:
    print(city, "->", get_country(city))
