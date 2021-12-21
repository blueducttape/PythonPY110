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


"""
Написать генератор, возвращающий по одному слову текстового файла,
при этом не загружая в память весь файл.
В качестве разделителя слов использовать символ пробела.
"""


def get_words_from_file(file_name: str, separator=' ') -> str:
    with open("words.txt" ,'r') as f:
        while f:
            line = str.split(f.readline(), sep=separator)
            iter_line = iter(line)
            i = 0
            while i < len(line):
                yield next(iter_line)
                i += 1


"""
Написать генератор, возвращающий по одной
строке из текстового файла. Символом окончания строки является символ “\n”.
Встроенной реализацией пользоваться нельзя.
"""

def get_lines_from_file(file_name: str) -> str:
    with open(file_name,'r') as f:
        while f:
            yield f.readline()



if __name__ == "__main__":
    print(get_text("Hello, World!!!"))
    print(get_text("fhgnk"))
    print(get_text("Hello, World!!!"))
    print(get_words_from_file("words.txt", separator = ' '))