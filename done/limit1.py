# %% [markdown]
# ### Контрольная работа по дисциплине "Методы ....." ФИО группа

# %%
from sympy import *
init_printing(use_latex=True)

# %% [markdown]
# ##  1. Вычислить предел: $\lim\limits_{x\to\infty}(1+\frac{5}{x})^{3x}$

# %%
x = symbols('x')
y = Limit((1 + 5 / x) ** (3 * x), x, oo)
Eq(y, y.doit())

# %% [markdown]
# ##  2. Вычислить предел: $\lim\limits_{x\to\infty}\left(\dfrac{2x^2+3}{2x^2+5}\right)^{8x^2+3}$

# %% [markdown]
# Предел имеет вид $1^{\infty}$, так как $\dfrac{2x^2+3}{2x^2+5}\to 1$, а показатель $8x^2+3\to\infty$ при $x\to\infty$.
#
# Используем стандартный приём раскрытия неопределённости $1^{\infty}$:
# $$\lim_{x\to\infty} f(x)^{g(x)} = \exp\Big(\lim_{x\to\infty} \big(f(x)-1\big)\cdot g(x)\Big),\qquad f(x)\to 1,\ g(x)\to\infty$$

# %%
f = (2 * x**2 + 3) / (2 * x**2 + 5)
g = 8 * x**2 + 3

f_1 = simplify(f - 1)
f_1

# %% [markdown]
# Составим произведение $(f(x)-1)\cdot g(x)$ и найдём его предел при $x\to\infty$:

# %%
expr = simplify(f_1 * g)
L = Limit(expr, x, oo)
Eq(L, L.doit())

# %% [markdown]
# Следовательно:
# $$\lim_{x\to\infty}\left(\dfrac{2x^2+3}{2x^2+5}\right)^{8x^2+3} = e^{-8}$$

# %% [markdown]
# **Проверка** прямым вычислением предела в Sympy:

# %%
y2 = Limit(((2 * x**2 + 3) / (2 * x**2 + 5)) ** (8 * x**2 + 3), x, oo)
Eq(y2, y2.doit())
