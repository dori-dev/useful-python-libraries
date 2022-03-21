"""contextlib library
"""
import contextlib


@contextlib.contextmanager
def show(name):
    # __enter__
    print('Starting Context Manger...', name)
    yield f"name: {name}"
    # __exit__
    print('Ending Context Manger...', name)


with show('salar') as one, show('ali') as two:
    print(one)
    print(two)


class MyContextManager(contextlib.ContextDecorator):
    def __enter__(self):
        print('Starting...')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting...')


with MyContextManager():
    print('OK')


@MyContextManager()
def show():
    print('Hello, there!')


show()
