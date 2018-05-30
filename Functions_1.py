# 1) Functions
print("\n***** Primer funkcii*****")
def my_symbols(chislo):
    for i in range(chislo):
        print(i)

#n = int(input("n = "))
n = 5
my_symbols(n)


# 2) Functions
print("\n***** Pri izmenenii znacheniya argumenta vnutri funkcii ishodyi argument ne menyaetsya*****")
# Tak kak eto raznye oblasti pamyati
def exampl1(chislo):
    print("chislo bylo:", chislo)
    chislo+=1
    print("chislo stalo:", chislo)

n = 10
print("n bylo:", n)

exampl1(n)
print("n stalo:", n)

# 3) Functions
print("\n***** Pri izmenenii znacheniya spiska vnutri funkcii ishodyi spisok menyaetsya *****")
# Tak kak eto odna i ta zhe oblast pamyati. a my_arr i arr prosto ssylki na odnu i tu zhe oblast
def exampl2(my_arr):
    print("my_arr bylo:", my_arr)
    my_arr.append(9)
    print("my_arr stalo:", my_arr)

arr = [1, 2, 3]
print("arr bylo:", arr)
exampl2(arr)
print("arr stalo:", arr)


# 4) Functions
print("\n***** Return *****")
def exampl3(value):
    value += 10
    return value

n = 1
print("n = ", n)
print("n = ", exampl3(n))

# 4) Functions
print("\n***** Return (None) *****")
def exampl4(value):
    value += 10
    return

n = 1
print("n = ", n)
print("n = ", exampl4(n))


# 5) Functions
print("\n***** Function without arguments *****")
def exampl5():
    value = 10
    print("value = ", value)

exampl5()

# 6) Functions
print("\n***** Function in function *****")
def exampl6(first,second):
    return first + second

print(exampl6(6, exampl6(2, 3)))


# 6) Functions (named arguments)
print("\n***** Named arguments *****")
def goods(item, color, price):
    print("\nItem:", item, sep='\t')
    print("Color:", color, sep='\t')
    print("Price:", price, sep='\t')

goods('pen', 'black', '1$')  # Argumenty po poryadku
goods(price='1$', item='pen', color='black')  # Imenovannye argumenty (= bez probelov!!!
goods('pen', price='1$', color='black')  # Argumenty v lyubom poryadke (No nachinayutsya vsegda s pozitsionnyh,
#  esli oni est')


# 7) Functions (default params)
print("\n***** Default params *****")
# Budet ispolzovan defoltovoe znachenie parametra, esli ono ne ukazano pri vyzove
def exampl7(name='Egor'):
    print("hello,", name, "!")

exampl7()

# 8) New feature from python 3.5: types of input and putput params
def new_style(i: int, s:str) -> bool:   # first param should be int, second string, output - bool.
    return s[i] == 'a'

print(new_style(0, 'abc'))  # is 0 element of string a?

print(new_style("s", 3))






