def outer(func):
    def inner():
        print("Function START")
        func()
        print("Function STOP")
    return inner

@outer
def hello():
    print("Hello")

@hi
def hi():
    print("hi")

# hello = outer(hello)
# hi = outer(hi)

hello()
hi()