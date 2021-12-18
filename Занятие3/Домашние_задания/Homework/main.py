"""Написать декоратор, сохраняющий результат в файл output.txt помимо возвращения."""


def save_result(fn):
    def wrapper(arg):
        result = fn(arg)
        f = open('input.txt', 'w')
        f.write(result)
        return result
    return wrapper


@save_result
def get_text(string):
    return string

"""Написать генератор, 
возвращающий по 3 символа из текстового файла,
 при этом не загружая в память весь файл."""
def sym(fn):
    f = open("sample.txt", "r")
    data = f.read(3)
    print(data)


if __name__ == "__main__":
    get_text("Hello, World!!!")
    get_text("fhgnk")
    get_text("Hello, World!!!")