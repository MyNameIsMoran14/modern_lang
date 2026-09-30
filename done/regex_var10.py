# %% [markdown]
# ### Лабораторная работа: регулярные выражения в Python. Вариант 10
#
# **Задача 10.** Извлеките никнейм пользователя, имя домена и суффикс из данных email адресов.

# %%
import re

emails = """zuck26@facebook.com          # Многострочный комментарий
page33@google.com
jeff42@amazon.com"""

# %% [markdown]
# Каждый адрес имеет вид `никнейм@домен.суффикс`. Никнейм и домен состоят из букв/цифр/`_`
# (класс `\w`), поэтому используем три группы захвата, разделённые `@` и `.`:

# %%
pattern = r'(\w+)@(\w+)\.(\w+)'
result = re.findall(pattern, emails)
result

# %% [markdown]
# Ожидаемый ответ:
# ```
# [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
# ```

# %%
expected = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
result == expected
