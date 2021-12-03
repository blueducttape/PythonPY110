
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


if __name__ == "__main__":
    get_text("Hello, World!!!")
    get_text("fhgnk")
    get_text("Hello, World!!!")