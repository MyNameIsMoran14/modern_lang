# %% [markdown]
# ### Контрольная работа по дисциплине "Методы ....." ФИО группа. Вариант 10

# %%
from sympy import *
init_printing(use_latex=True)

# %% [markdown]
# ## Задание 1. Найти предел функции
# $$\lim_{x\to\infty}\left(\dfrac{2x^2+3}{2x^2+5}\right)^{8x^2+3}$$

# %%
x = symbols('x')
y = Limit(((2*x**2 + 3) / (2*x**2 + 5)) ** (8*x**2 + 3), x, oo)
Eq(y, y.doit())

# %% [markdown]
# ## Задание 2. Вычислить неопределённый интеграл
# $$\int \arccos x \, dx$$

# %%
Fx = Integral(acos(x), x)
Eq(Fx, Fx.doit())

# %% [markdown]
# Проверим результат дифференцированием:

# %%
Fx.diff(x)

# %% [markdown]
# ## Задание 3. Решить систему линейных уравнений
# $$
# \begin{cases}
# x_1+2x_2+3x_3+4x_4=11,\\
# 2x_1+3x_2+4x_3+x_4=12,\\
# 3x_1+4x_2+x_3+2x_4=13,\\
# 4x_1+x_2+2x_3+3x_4=14.
# \end{cases}
# $$

# %%
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
eq1 = Eq(x1 + 2*x2 + 3*x3 + 4*x4, 11)
eq2 = Eq(2*x1 + 3*x2 + 4*x3 + x4, 12)
eq3 = Eq(3*x1 + 4*x2 + x3 + 2*x4, 13)
eq4 = Eq(4*x1 + x2 + 2*x3 + 3*x4, 14)
eq1, eq2, eq3, eq4

# %%
linsolve([eq1, eq2, eq3, eq4], [x1, x2, x3, x4])

# %% [markdown]
# Система имеет единственное решение: $x_1=2,\ x_2=1,\ x_3=1,\ x_4=1$.

# %% [markdown]
# ## Задание 4. Исследовать функцию и построить график
# $$y=\dfrac{x}{1+x^2}$$
#
# Функция определена на всей вещественной оси (знаменатель не обращается в нуль), нечётная: $y(-x)=-y(x)$, график симметричен относительно начала координат. Горизонтальная асимптота $y=0$, вертикальных асимптот нет.

# %%
def y(x):
    return x / (1 + x**2)

x = symbols('x', real=True)

# %% [markdown]
# Точки пересечения с осями координат:

# %%
rt = solve(y(x), x)
print('Решение уравнения y(x)=0:')
rt

# %%
vx = [rt[0]]
vy = [0]
vx.append(0)
vy.append(y(0))
print('Точки пересечения с осями координат:')
vx, vy

# %% [markdown]
# Находим производные:

# %%
y1 = diff(y(x), x)
print('Первая производная:')
y1 = simplify(y1)
y1

# %%
y2 = diff(y1, x)
print('Вторая производная:')
y2 = simplify(y2)
y2

# %% [markdown]
# #### Исследование на экстремум

# %%
ext = solve(y1, x)
print('Стационарные точки: ')
ext

# %%
y2.subs(x, ext[0])
# важен знак второй производной в первой стационарной точке

# %%
y2.subs(x, ext[1])
# важен знак второй производной во второй стационарной точке

# %% [markdown]
# В точке $x=-1$ вторая производная положительна — локальный минимум, $y(-1)=-1/2$.
# В точке $x=1$ вторая производная отрицательна — локальный максимум, $y(1)=1/2$.

# %% [markdown]
# #### Исследование на перегиб

# %%
per = solve(y2, x)
print('Точки перегиба: ')
per

# %% [markdown]
# Итак, собираем координаты всех характерных точек графика исследуемой функции:

# %%
for p in ext:
    vx.append(p)
    vy.append(y(p))
for p in per:
    vx.append(p)
    vy.append(y(p))
print(vx, vy)

# %% [markdown]
# Строим график:

# %%
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-6, 6, 200)
Y = [float(y(xi)) for xi in X]

vx_f = [float(v) for v in vx]
vy_f = [float(v) for v in vy]

fig = plt.figure(figsize=(8, 4), dpi=100)
plt.plot(X, Y, color='red', linewidth=1.5)
plt.scatter(vx_f, vy_f, marker='*', c='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'График функции $y = x/(1+x^2)$')
plt.axhline(0, color='black', linewidth=0.7)
plt.axvline(0, color='black', linewidth=0.7)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()

# %% [markdown]
# ## Задание 5. Найти общее решение дифференциального уравнения
# $$\frac{y}{x}\,y' = e^{x-y}$$

# %%
x = symbols('x')
f = Function('y')
deq = Eq(f(x) / x * f(x).diff(x), exp(x - f(x)))
deq

# %% [markdown]
# Уравнение с разделяющимися переменными. Решение по умолчанию:

# %%
dsolve(deq, f(x))

# %% [markdown]
# Результат выражен через неэлементарную функцию LambertW() и неудобен для практики. Посмотрим, какими ещё методами можно решить уравнение:

# %%
classify_ode(deq, f(x))

# %%
dsolve(deq, f(x), hint='separable_Integral')

# %% [markdown]
# Разделяем переменные явно: $y\,e^{y}\,dy = x\,e^{x}\,dx$ и вычисляем интегралы по отдельности:

# %%
yv = symbols('y')
F1 = Integral(yv * exp(yv), yv)
F2 = Integral(x * exp(x), x)
Eq(F1.doit(), F2.doit())

# %% [markdown]
# Таким образом, общее решение (с точностью до произвольной постоянной $C$):
# $$(y-1)e^{y} = (x-1)e^{x} + C$$
