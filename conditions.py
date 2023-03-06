
# Boolean - 3 состояния

b = bool

t = True
f = False
n = None

# if/elif/else - на примере кода ответа

if True:
    print("правда!")
else:
    print("ложь")

code = 500


if 200 <= code < 300:
    print("Все хорошо!")
    n = 150
elif 400 <= code < 600:
    print("Все плохо")
else:
    print("Все неопределено")


# Пустые объекты - false

print(bool(10))
print(bool(-10))
print(bool(0))
print(bool("asdfsfasfa"))
print(bool(""))
print(bool("0"))
print(bool([]))
print(bool([1, 2, 3]))
print(bool({}))
print(bool({"key": 123}))
print(bool(None))

users = []

if users:
    print(users)
