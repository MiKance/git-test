import config
def hello(name, age):
    print(f'Hello, {name}!')
    print(f'Are you {age} y.o, right?')

hello(config.name, config.age)