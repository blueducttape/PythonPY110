def fabric_decorators(arg_decorator):
    print(f"Я аргумент фабрики декораторов {arg_decorator}")

    def decorator(fn):
        print(f"Я вызываюсь на момент декорирования с аргументом фабрики декораторов {arg_decorator}")

        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@fabric_decorators(123)  # fabric_decorators(123) -> decorator(test2) -> wrapper
def test_1(arg1):  # test_1 = decorator(test_1)
    return arg1


@fabric_decorators("test")  # fabric_decorators(123) -> decorator(test2) -> wrapper
def test_2(arg1):  # test_1 = decorator(test_1)
    return arg1


if __name__ == "__main__":
    test_1(5)
    pass
