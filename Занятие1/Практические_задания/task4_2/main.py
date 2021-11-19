from itertools import count


def task():
    iterator_numbers = count(1, 1)
    numbers = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, iterator_numbers))  # TODO заменить на map и filter

    for _ in range(10):
        print(next(numbers))
    # TODO напечатать первые 10 чисел
    # TODO с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
