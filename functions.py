import functools

# Объявляем функцию


def my_awesome_func():
    a = 5
    b = 10
    print(a + b)


my_awesome_func()

# Функция с позиционными аргументами


def sum_numbers(a, b):
    print(a + b)


sum_numbers(10, 15)
sum_numbers(50, 100)

# Функция с именованными аргументами

sum_numbers(a=10, b=15)
sum_numbers(b=50, a=15)

# Функция с аргументами по умолчанию

print(1, 2, 3, 4, 5, sep="\n")


def multiply(a, b=10):
    print(a * b)


multiply(5)
multiply(5, b=5)


day = "monday"


def my_func():
    def another_func():
        another_var = 123
        print(func_day)

    day = "saturday"
    func_day = "saturday"
    print(day, func_day)

my_func()
print(day)

# Возвращаем значение


def sum_numbers(a, b):
    return a + b


result = sum_numbers(10, 15)
print(result)

# Переменное количество аргументов на примере print

print(2, 3, 5, 10, 51521, "fasfas", "fasfasf")


def sum_numbers(*args):
    result = 0
    for number in args:
        result += number

    print(sum(args))
    print(result)


sum_numbers(10, 15, 20, 25)


def func_with_kwargs(**kwargs):
    print(kwargs)


def combined(*args, **kwargs):
    print(args)
    print(kwargs)


func_with_kwargs(arg1=123, arg2="some arg")

combined(1, 2, 3, 4, 5, arg1=123)

t, *tt = (1, 2, 3, 4)
print(t, tt)


l = [1, 2, 3]
ll = [4, 5, 6]

print(l + ll)
print([*l, *ll])

d = {"a": 10, "b": 20}

multiply(**d)

# Возвращаем несколько значений


def login_password():
    return "login", "password"


l_p = login_password()
login, password = login_password()
print(l_p)
print(login, password)


# Функция - тоже объект

p = print

p(1, 2, 3, 4)

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]


def get_user_age(user):
    return user["age"]


print(get_user_age(users[0]))

# Сортируем по возрасту

users.sort(key=get_user_age, reverse=True)
print(users)

users.sort(key=lambda user: user["age"], reverse=True)
print(users)
