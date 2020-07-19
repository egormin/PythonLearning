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

# 8) New feature from python 3.5: types of input and putput params  (just for programmer, not interpreter)
def new_style(i: int, s:str) -> bool:   # first param should be int, second string, output - bool.
    return s[i] == 'a'

print(new_style(0, 'abc'))  # is 0 element of string a?

# 9) Various params number:  
# args - returns lists
# kwargs - returns kwargs
def fun1(x, y, *args, **kwargs):
    print(x, y, args, kwargs)
    if args:
        print("args[0]: {}".format(args[0]))  # args[0]: 3
    if kwargs:
        print("kwargs ['parameter']: {}".format(kwargs.get('parameter')))  # kwargs ['parameter']: 1

fun1(1, 2)                      # 5 10 () {}
fun1(1, 2, 3, 4)                # 1 2 (3, 4) {}
fun1(1, 2, 3, 4, parameter=1)   # 1 2 (3, 4) {'param': 1}
fun1(1, 2, 3, 4, param=1)       # kwargs ['parameter']: None

# 10) Named params:
fun(a=3, d=4):
    
# 11) Parameters packing and unpacking
def sum(*args):
    print(args)

sum(1, 2, 3)  # (1, 2, 3)

# another example. The list will be unpacked to separate parameters
def xy(x, y):
    print(x)
    print(y)

nums = [2, 4]
xy(*nums)
# 2
# 4

# another example. In this case "x" in dict should be named the same as param in function xy
def xy(x, y):
    print(x)
    print(y)
 
xxx = {"x": 1, "y": 2}
xy(**xxx)
# 1
# 2

# another example
def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    print(total)

multiply(1, 2, 3, 5) # 30

# another example
def fun2(a, *args):
    print(a, args)
    if args:
        print("args[0]: {}".format(args[0]))

l = [1, 2, 3]

fun2(1, 2)              # 1 (2,)
fun2(1, 2, l)           # 1 (2, [1, 2, 3])
fun2(1, 2, *l)          # 1 (2, 1, 2, 3)

def fun3(a, b, c):
    print(a, b, c)
    
fun3(*l)                # 1 2 3

####
def f1(l):
    l.append(3)

def f2(l):
    l = 2   # defines as local 

arg = [2]
f1(arg)
print(arg)  # [2, 3]

arg = 1
f2(arg)
print(arg)  # 1

# 12) Closures (замыкания)
def outer(a):
    def inner(b):
        return a + b
    return inner

closure = outer(1)
print(closure(2))    # 3





