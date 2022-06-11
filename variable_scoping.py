# from _typeshed import NoneType
import numpy as np

global hello
hello = "Hello World"


def say_hello():
    global hello
    print(hello)
    hello = "Hello No"
    print(hello)


if __name__ == "__main__":
    # say_hello()
    # print(hello)
    a = np.zeros((3, 3), np.uint8)
    if isinstance(a, np.ndarray):
        print('It is an ndarry!!')
    print(type(a))
    a = None
    if a is None:
        print('It is an nonery!!')
    print(type(a))
