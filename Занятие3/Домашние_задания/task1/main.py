
if __name__ == "__main__":
    list_= []
    with open('list1.txt') as f:
        list_ = f.read().splitlines()
        print(list_)
    list_ = []
    with open('list2.txt') as f:
        list_1 = f.read().splitlines()
        print(list_1)

    pass
