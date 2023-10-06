def my_foo(name: str) -> str:
    return "Привет, {0}".format(name)

name = input("Введите ваше имя: ")
hello_message = my_foo(name)

print(hello_message)