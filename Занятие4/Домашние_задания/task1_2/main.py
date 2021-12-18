import re
pattern = re.compile("""(.|\n)+?""")

if __name__ == "__main__":
    file_name = "input.txt"
    my_file = open(file_name, "r", encoding="utf-8")
    my_text = my_file.read()
    results = re.findall(pattern, my_text)
    print (results)
    #with open("input.txt", "r", encoding="utf-8") as f:
        #quotes_txt = f.readlines()
        #whole_txt = "".join(quotes_txt)
        #matches = re.search(pattern, whole_txt)





#выбрать все цитаты из файла и вывести по отдельности