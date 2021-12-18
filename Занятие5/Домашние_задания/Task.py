

#task_1
def bin_dec(bin_list):
    bin_str = ''.join(str(x) for x in bin_list)
    return int(bin_str, 2)

print (bin_dec([0,1,1,0,0,0]))
print (bin_dec([0,1,0,0,0,1]))
#lst = [0, 1, 0, 1, 0, 0, 1]
#x = ''.join(map(str, lst))
#print(int(str(x), base=2))


#task_2
str_ = 'hello'
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
#for elem in [f"{my_str[:i]}{my_str[i].upper()}{my_str[i+1:]}
#task_4
#rus_alphabet = ''.join([chr(i) for i in range(ord('a'), (ord('a')+32))])
#print(rus_alphabet)
#weight_dict = {}
#for weight, elem in enumerate(rus_alphabet, start=1):
    #weight_dict.update({elem: weight})
#print(weight_dict)


#def get_word():
    #word_weight_list = []
    #alphabet_weight = get_rus_alphabet_with_weight()


#word_list = input(str.split(" "))
#for word in word_list:
    #word_weight = 0
    #for char_ in word:
        #word_weight+=alphabet_weight.get(char, 0)

#task_5


def reverse(word='example'):
    center = len(word//2)
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

print(romanToInt('MDCLXVI'))
print(romanToInt('DLIII'))


#task_7


