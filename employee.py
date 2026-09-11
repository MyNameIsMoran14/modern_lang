# %% [markdown]
# ### Лабораторная работа: атрибуты экземпляра и атрибуты класса
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
