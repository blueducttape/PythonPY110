def int_check(fn):
    def wrapper(arg):
        if not type(arg) == int:
            raise ValueError("Аргумент функции не является  типом int.")

        result = fn(arg)
        return result

    return wrapper

@int_check
def print_args(*args):
    print(type(args), args)


if __name__ == "__main__":

    print_args(4.6)

    pass
