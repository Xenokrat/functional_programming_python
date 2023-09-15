# 2.3.1
@curry(2)
def say_thing_thing(thing1: str, thing2: str) -> str:
    return thing1 + ", " + thing2

hello_thing = say_thing_thing("Hello")
hello_thing("World")  # "Hello, World"


# 2.3.2
@curry(4)
def curry_greetings(greet: str, punc1: str, punc_end: str, name: str) -> str:
    return f"{greet}{punc1} {name}{punc_end}"

# Сделаем параметр "name" последним аргументом, чтобы на основе функции curry_greetings
# можно было получить функцию для применения только имени
curry_greetings_name = curry_greetings("Hello")(",")("!")
curry_greetings_name("Pavel")  # 'Hello, Pavel!'