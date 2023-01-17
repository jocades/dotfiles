

def hello():
    for i in range(0, 10):
        print(f'Hello {i}')


def reciever(fn):
    fn()


reciever(hello)
