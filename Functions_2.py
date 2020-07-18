# 1) Dokumentirovanie funkciy
# Poluchenie spravok po funkciyam, modulyam, klassam

print("\n***** Help for print *****")
print(help(print))  # for help output - help(print) or input.__doc__  (input - interested function)
print("\n***** Help for input *****")
print(input.__doc__)

# 2) Dokumentirovanie funkciy
# Sozdanie spravok

print("\n***** Sozdanie spravok *****")

def repeat(num):
    """
    repeat function repeats numbers from 0 to num  # Kratkoe opisanie, chto delaet funkciya

    num - argument  # ostal'naya infa
    """
    for _ in range(num):
        print(_)

numb = 5
repeat(numb)
print("Vyvod spravki (variant 1):***", repeat.__doc__, "***")
print("Vyvod spravki (variant 2):***", help(repeat), "***")


# 3) Vlozhennye funkcii

def outer_func():

    def inner_func():
        print("inner_func")

    print("outer_func")
    inner_func()

outer_func()

# 4) Oblasti vidimosti
print("\n***** Oblasti vidimosti *****")
# Oblast' vidimosti peremennyh vnutrenney funkcii - tolko vnutr funkciya, t.e. za ee predelami eti peremennye ne vidny
# Oblast' vidimosti peremennyh vneshney funkcii - vnesh i vnutr funkciya
# Peremennye byvayut lokal'nye i global'nye
# Globalnye - obyavlyayutsya vne funkciy i dostupny otovsyudu
# Lokalnye - sozdayutsya vnutri funkcii i ne dostupny snaruzhi

var = "global variable"
print("\n***** Znachenie beryutsya iz vneshney funkcii")
def pr_var():
    print(var)  # t.k. peremen var netu vnutri dannoy funkcii, to beryotsya znachenie iz vneshney funkcii
# global variable
pr_var()

print("\n***** Znachenie beryutsya iz vnutrenney funkcii")
var = "global variable"
def pr_var():
    var = "local variable"
    print(var)  # t.k. peremen var est' vnutri dannoy funkcii, to beryotsya znachenie iz vnutrenney funkcii
# local variable
pr_var()
print(var)

print("\n***** Menyaem znachenie vneshney funkcii vnutri vnutrenney s pomoschyu GLOBAL")
# Esli my hotim izmenit' znachenie imenno vneshney peremennoy, to nado ispol'zovat global
var = "global variable"
def pr_var():
    global var
    var = "local variable"
    print(var)  # t.k. peremen var est' vnutri dannoy funkcii, to beryotsya znachenie iz vnutrenney funkcii
# local variable
pr_var()
print(var)  # uzhe stala local

print("\n***** Menyaem znachenie funkcii na odin uroven' vverh s pomoschyu GLOBAL")
# Esli my hotim izmenit' znachenie imenno vneshney peremennoy, to nado ispol'zovat global
var = "global variable"
def vnesh_var():
    var = "verh uroven"
    def vnutr_var():
        nonlocal var
        var = "local variable"
    vnutr_var()
    print(var)  # local variable'
# local variable
print(var)
vnesh_var()
print(var)  # uzhe stala local


# 5) Recursion
# Vichislenie factoriala chisla

chislo = 5
print("\n***** Factorial *****")
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


print("Faktorial chisla {} = {}".format(chislo, factorial(chislo)))

# Vichislenie chisel fibonacci (summa chisel: 1+1=2 1+2 =3, 2+5 = 5...)
print("\n***** Chisla fibonacci *****")
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = 100
for i in range(1, n+1):
    #print("Chisla fibonacci ot {} = {}".format(i, fib(i)))  # tak vypolnyaetsya ochen dolgo, t.k na kazhdoy iteracii
#dannye ne sohranyayutsya, a vychislyayutsya zanovo
    pass


# Vot tak budet bystro (memorizaciya znacheniy funkcii):
import functools
print("\n***** Chisla fibonacci Bistro*****")
@functools.lru_cache(maxsize = None)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = 100
for i in range(1, n+1):
    print("Chisla fibonacci ot {} = {}".format(i, fib(i)))


# Vichislenie factoriala chisla
print("\n***** Hanoyskaya bashnya *****")
def hanoi(n, a, b, c):  # perenosim s A na A c pomosc'yu C n kolets
    if n != 0:
        hanoi(n - 1, a, c, b)
        print("Transfer A ring from", a, "to", c)
        hanoi(n - 1, b, a, c)
hanoi(3, 'A', 'B', 'C')




var = 5
def function():
    var += 1
function()

print(var)

# Lambda functions:
print((lambda x, y: x + y)(5, 7))

lambda x, y: x + y
# The same
def add(x, y)
  return x + y

# List comprehensions
sequence = [1, 2, 3]
doubled = [double(x) for x in sequence]
# The same
doubled1 = [(lambda x: x * 2)(x)for x in sequence]
# The same
doubled2 = list(map(lambda x: x * 2, sequence))
# The same
doubled3 = list(map(double, sequence))

print(doubled)
print(doubled1)
print(doubled2)
print(doubled3)
# [2, 4, 6]







