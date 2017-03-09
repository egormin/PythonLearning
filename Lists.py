# 1) Zadanie spiskov
print("\n***** Zadanie Spiskov (sposob 1) *****")

# Spisok tsifr
int_list = [1, 2, 3, 4]
print(type(int_list))
print("int list:", int_list)

# Spisok srok
str_list = ['a', 'vdd', 'efg', 'q']
print("str list:", str_list)

# Pustoy spisok
empty_list = []
print("Empty list:", empty_list)


print("\n***** Zadanie Spiskov (sposob 2) *****")
list_from_range = list(range(5))  # Preobrazuem diapazon v spisok
print(list_from_range)  # [0, 1, 2, 3, 4]

list_from_string = list('this string')  # Preobrazuem stroku v spisok
print(list_from_string)  # ['t', 'h', 'i', 's', ' ', 's', 't', 'r', 'i', 'n', 'g']


# 2) Ispol'zovanie spiskov
print("\n***** Ispol'zovanie spiskov *****")
chr_list = ['h', 'e', 'l', 'l', 'o']
print(chr_list[0])  # h
print(chr_list[-1])  # o
print(chr_list[-2])  # l


# 3) Srez spiskov
# srez spiska - eto guppa elementov spiska po ih indeksam
# new_list = my_list[start:end:step]
chr_list = ['h', 'e', 'l', 'l', 'o']
print(chr_list[1:5:1])  # ['e', 'l', 'l', 'o']
print(chr_list[0:5:2])  # ['h', 'l', 'o']
# po umolchaniyu nachal'nyi =0, konechniy = dlina spiska
print(chr_list[::2])  # ['h', 'l', 'o']
print(chr_list[0:2])  # ['h', 'e']
print(chr_list[0:-2])  # ['h', 'e', 'l']
print(chr_list[-1:0:-1])  # ['o', 'l', 'l', 'e']
print(chr_list[::-1])  # ['o', 'l', 'l', 'e', 'h']
print(chr_list[:])  # ['h', 'e', 'l', 'l', 'o']
print(chr_list[2:])  # ['l', 'l', 'o']
print(chr_list[2::2])  # ['l', 'o']

# 4) Is value in list
print("\n***** Is value in list *****")
int_list = [1, 2, 3, 4]
str_list = ['a', 'vdd', 'efg', 'q']

value = 3
if value in int_list:
    print("value {} is in list {}".format(value, int_list))

value = 'q'
if value in str_list:
    print("value {} is in list {}".format(value, str_list))

stroka = 'zhopa'
if 'zh' in stroka:
    print("Simvol zh est' v stroke", stroka)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in "AEIOU":
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")

#5) Dlina spiska
print("\n***** Dlina spiska *****")
int_list = [1, 2, 3, 4]
print("dlina spiska {0} ravna {1} simvolov".format(int_list, len(int_list)))

stroka = 'zhopa'
print(stroka[2])
print(len(stroka))
print(stroka[2::])
print(stroka[0] + stroka[-2:])  # zpa (0 + 2-й с конца и до конца)


# 6) Modifikaciya spiskov
print("\n***** Dobavlenie znacheniya *****")
int_list = [1, 2, 3, 4]
print(int_list)  # [1, 2, 3, 4]
int_list.append(99)  # [1, 2, 3, 4, 99]
print(int_list)
int_list += [88, 33, 55]  # [1, 2, 3, 4, 99, 88, 33, 55]
print(int_list)

str_list = ['a', 'vdd', 'efg', 'q']
print(str_list)  # ['a', 'vdd', 'efg', 'q']
str_list += ['add', 'values']
print(str_list)  # ['a', 'vdd', 'efg', 'q', 'add', 'values']
str_list += ['add', 'values', 7, 99]
print(str_list)  # ['a', 'vdd', 'efg', 'q', 'add', 'values', 'add', 'values', 7, 99]

print("\n***** Izmenenie znacheniya *****")
int_list = [1, 2, 3, 4]
print(int_list)
int_list[0] = 100
print(int_list)  # [100, 2, 3, 4]
int_list[0], int_list[2] = 99, 22
print(int_list)  # [99, 2, 22, 4]

print("\n***** Udalenie znacheniya *****")
int_list = [1, 2, 3, 4]
print(int_list)  # [1, 2, 3, 4]
del int_list[2]
print(int_list)  # # [1, 2, 4]


# 7) Obhod elementov spiska
print("\n***** Obhod elementov spiska *****")
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in "AEIOU":
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")


int_list = [1, 2, 3, 4]
for _ in int_list:
    print(_)  # 1,2,3,4


str_list = ['a', 'vdd', 'efg', 'q']
for _ in str_list:
    print(_)  # a, vdd, efg, q


print("\n***** Chisla fibonacci *****")
n = 10
fibs = [1, 1]
for i in range(n - 2):
    fibs.append(fibs[i] + fibs[i + 1])  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(fibs)


