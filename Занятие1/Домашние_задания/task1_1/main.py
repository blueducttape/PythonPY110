def enumerate(iterable, start=0):
    return zip(range(start, start + len(iterable)), iterable)


if __name__ == "__main__":
    print(enumerate())
    pass
