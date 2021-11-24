def check_iterable(func):
    def wrapper(arg):
        if not iter(nums):
            raise TypeError("Объект <название или номер позиционного аргумента> <значение аргумента> не является итерируемым")

        result = func(arg)
        return result

    return wrapper


@check_iterable
def func(nums: list):
    print(*nums)



if __name__ == "__main__":
    nums = [1, 2, -3]
    func(nums)
    nums = 1
    func(nums)
    pass
