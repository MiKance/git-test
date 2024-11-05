import config
def hello(name, age):
    print(f'Hello, {name}!')
    print(f'Are you {age} y.o, right?')
    data = input("Input your password: ")
    print(data == config.password)

hello(config.name, config.age)