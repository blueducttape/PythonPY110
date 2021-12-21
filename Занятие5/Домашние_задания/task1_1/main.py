import random


def fab(n):
    def decorator(fn):
        def decorated2(*x):
            y = 0
            for i in range(n):
                y += fn(*x)
                print(y)
            return y / n
        return decorated2
    return decorator


@fab(5)
def rand():
    x = random.randint(1, 10)
    return x


print(rand())
