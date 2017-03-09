# About standart functions (in file Builtins.py)

# 1) abs (absolutnoe znachenie. iz -5 delaet 5)
abs(-5)  # 5

# 2) dir (pokazivaet, kakie ob'ekty est' v module)
import PyQt5
print(dir(PyQt5))   # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__'.....

# 2) divmod (pervoe chislo - eto celochislennoe delenie, vtoroe - ostatok ot deleniya)
x, y = divmod(5, 3)
print(x, y)  # 1 2 (5//3=1, 5%3=2)

# 3) len (dlina posledovatel'nosti)
ss = "hello"
print(len(ss))  # 5
spis = [1, 2, 3]
print(len(spis)) # 3

# 4) Max (Max znachenie)
print(max(2, 5, 7)) # 7
print(max('a', 'e', 'u')) # u

# 5) Min (Min znachenie)
print(min(2, 5, 7))  # 2
print(min('a', 'e', 'u'))  # a

# 6) Pow (stepen)
print(pow(2, 8))  # 256

# 7) Reversed (posledovatelnost' v obratnom poryadke) #######################
for i in reversed(range(50, 55)):  # 54, 53, 52, 51, 50
    print(i)

for i in reversed('hello'):
    print(i, end="")  # olleh
print()


# 8) round (Okruglenie chisla)
print((round(3.444, 2)))  # Do 2 znakov posle zapyatoi

# 9) sorted (sortiruet spiski)
strinn = ['b', 'a', 'c']
print(sorted(strinn))  # ['a', 'b', 'c']

# 10) sum (Summa chisel posledovatel'nosti) ###################################
lisst = [1, 2, 30]
print(sum(lisst))  # 33

# 11) Bin, oct, hex
number = 10
print("Binary:      ", bin(number))
print("Octal:       ", oct(number))
print("Hexadecimal: ", hex(number))

