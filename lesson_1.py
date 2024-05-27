from datetime import datetime

#in lesson:
def myDecorator(func):
    def wrapper():
        time1 = datetime.now().microsecond
        print(f"time1 = {time1}")
        func()
        time2 = datetime.now().microsecond
        print(f"time2 = {time2}")
        time = time2 - time1
        print(f"the space between start to end: {time}")

    return wrapper

@myDecorator
def func1():
    num = 0
    for i in range(1, 10000000):
        num += i
    return

#to homwork:
cache = dict()

def decorator(Fibonacci):
    def fib(*args):
        n = args[0]
        if n not in cache:
            cache[n] = Fibonacci(n)
            print("it is not in memory cache!")
        return cache[n]
    return fib

@decorator
def Fibonacci(n, ret=[], i=0, num1=0, num2=1, next_number=1, count=1):
    while count <= n:
        ret.append(next_number)
        count += 1
        num1 = num2
        num2 = next_number
        next_number = num1 + num2
    return ret


if __name__ == '__main__':
    a = datetime.now()
    ret1 = Fibonacci(10000)
    b = datetime.now()
    print(b-a)
    a = datetime.now()
    ret2 = Fibonacci(10000)
    b = datetime.now()
    print(b-a)
