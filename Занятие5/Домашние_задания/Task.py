import json
import re
import datetime
import random
from mimesis import Person


#task_1
def bin_dec(bin_list):
    bin_str = ''.join(str(x) for x in bin_list)
    return int(bin_str, 2)
#lst = [0, 1, 0, 1, 0, 0, 1]
#x = ''.join(map(str, lst))
#print(int(str(x), base=2))


#task_2

def task_2(str_):
    lst = []
    for index, s in enumerate(str_):
        if s == ' ':
            continue
        if s.isalpha():
            a = str_[:index]
            b = str_[index + 1:]
            lst.append(''.join((a, s.upper(), b)))
    print(*lst, sep = "\n")

#task_3


def wave(string: str):
    while True:
        n = len(string)
        for i in range(n-1):
            yield string[:i] + string[i].upper() + string[i+1:]
        revers = string[::-1]
        for i in range(n):
            if i != n-1:
                yield (revers[:i] + revers[i].upper() + revers[i+1:])[::-1]


#task_4

def get_rus_alphabet_with_weight():
    alphabet_weight = {}
    rus_alphabet = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])
    for weight, char in enumerate(rus_alphabet, 1):
        alphabet_weight.update({char: weight})

    return alphabet_weight


def get_word_with_max_weight(input_string):

     word_weight_list = []
     alphabet_weight = get_rus_alphabet_with_weight()

     word_list = input_string.split(" ")

     for word in word_list:
         word_weight = 0
         for char in word:
             word_weight += alphabet_weight.get(char, 0)
         word_weight_list.append(word_weight)

     return word_list[word_weight_list.index(max(word_weight_list))]

print(get_word_with_max_weight("мама мыла раму"))


#task_5


def reverse(word: str) -> str:
    center = len(word)//2
    print(word[center:-center])
    return word[center-1:-center] + word[center:-center] + word[-center:][::-1]


#task_6
def romanToInt(s):
    result = 0
    f = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    while i < len(s) - 1:
        if f[s[i + 1]] > f[s[i]]:
            result += f[s[i + 1]] - f[s[i]]
            i += 2
        else:
            result += f[s[i]]
            i += 1
    if i < len(s):
        result += f[s[len(s) - 1]]
    return result


#task_7

def get_name(length=3, lang='ru') -> str:
    s = ''
    if lang == 'ru':
         alpha = ''.join([chr(i) for i in range(ord('а'), ord('а') + 32)])
    if lang == 'en':
        alpha = ''.join([chr(i) for i in range(ord('a'), ord('a') + 23)])
    for _ in range(length):
        s += alpha[random.randint(0, len(alpha) - 1)]
    return s


def get_phone_num(region = '+7') -> str:
    def get_gr(len: int) -> str:
        s= ''
        for _ in range(len):
            s+= str(random.randint(0,10))
        return s
    number = f'{region}({get_gr(3)}){get_gr(3)}-{get_gr(2)}-{get_gr(2)}'
    return number


def get_datetime() -> str:
    date = datetime.datetime.now()
    return date.isoformat()


dict_ = {'name': get_name(5).capitalize(),
             'surname': get_name(8).capitalize(),
             'login': '@'+get_name(8, 'en'),
             'password': get_name(12, 'en'),
             'email': get_name(6, 'en')+'@'+get_name(4,'en')+'.'+get_name(3, 'en'),
             'phone': get_phone_num(),
             'register_time': get_datetime()
             }


def task7(user_count: int, out_file: str = 'Users.txt'):
    person = Person('ru')
    with open(out_file, 'w') as f:
        for _ in range(user_count):
            dict_ = {'name': person.first_name(),
                     'surename': person.surname(),
                     'login': '@' + person.username(mask='l_l'),
                     'password': person.password(),
                     'email': person.email(),
                     'phone': person.telephone(),
                     'register_time': datetime.datetime.now().isoformat()
                 }
            json.dump(dict_, f, indent=4, ensure_ascii=False)

    return dict_

#task_8


def convert_time(time: datetime = datetime.datetime.now(), mask: str = "YYYY-mm-dd HH:MM:SS") -> str:
    def change_lit(pattern: str, code: str, f_mask: str) -> str:
        return re.sub(pattern, code, f_mask)

    YEAR = r'[yY]{4}'
    SHORT_YEAR = r'[yY]{2}'
    MONTH = r'm{1,2}'
    DAY = r'd{1,2}'
    HOUR = r'H{1,2}'
    MINUTES = r'M{1,2}'
    SECONDS = r'S{1,2}'
    dict_pattern = {YEAR: '%Y',
                        SHORT_YEAR: '%y',
                        MONTH: '%m',
                        DAY: '%d',
                        HOUR: '%H',
                        MINUTES: '%M',
                        SECONDS: '%S'}

    for key, value in dict_pattern.items():
        mask = change_lit(key, value, mask)
    return time.strftime(mask)


if __name__ == "__main__":
    print(bin_dec([0, 1, 1, 0, 0, 0]))
    print(bin_dec([0, 1, 0, 0, 0, 1]))
    print(task_2('hello'))
    str_ = wave('word')
    for _ in range(10):
        print(next(str_))
    print(reverse(word='example'))
    print(romanToInt('MMXVI'))
    print(romanToInt('MDCLXVI'))
    print(romanToInt('DLIII'))
    print(dict_)
    print(task7(user_count=5))
    print(convert_time())
