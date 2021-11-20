import time


def time_decorator(fn):
    print("Этот код будет выведен в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print("Этот код будет выполняться перед каждым вызовом функции")
        start = time.perf_counter()
        # TODO зафиксировать время до начала выполнения функции
        result = fn(*args, **kwargs)
        # TODO зафиксировать время после выполнения
        finish = time.perf_counter()
        print("Этот код будет выполняться после каждого вызова функции")
        print(finish-start)
        return result
    return wrapper


@time_decorator
def pow_(a, n):
    return pow(a, n)


if __name__ == "__main__":
    print(pow_)
    print("=" * 25)

    print(pow_(5, 2))
    print("=" * 25)

    print(pow_(4, 4))
