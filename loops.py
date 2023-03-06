
# While - цикл с предусловием
# пока пользователь не введет правильный пароль, ...
import random

password_incorrect = True

while password_incorrect:
    print("Пытаемся войти в систему...")
    password_incorrect = random.randint(0, 1)


# For. Итерируем списки и словари

users = [1, 2, 3, 4, 5]

for user in users:
    print(user)

d = {
    "key": 123,
    "another": 456,
    "third": 789
}

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)


# Break/Continue/Else - прерывание цикла

# for i in range - цикл с итератором

for i in range(10):
    if i % 2 == 0:
        continue

    print(i)
    if i == 7:
        break
else:
    print("Когда я вызываюсь?")

# enumerate - возвращает пары (индекс, значение)

cities = ["Екатеринбург", "Moscow", "Sochi"]

for i, city in enumerate(cities, start=1):
    print(i, city)
