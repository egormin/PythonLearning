##spiski, mnozhestva, kortezhi, cikli, faily podderzhivayut interfeis generatore
# 1) Iteratory
#f = open('file.txt')
#f.readline()
L = [1, 2, 3]
LI = iter(L)  # Budem vityagivat' elementy odin za odnim
print(LI.__next__())  # 1
print(LI.__next__())  # 2
print(LI.__next__())  # 3
#print(LI.__next__())  # Error

#tsikli sai ispolz iteratori

# 2) Generatory
L = [i for i in range(5)]
print(L)  # [0, 1, 2, 3, 4]

#eto to zhe samoe, zapisannoe v prostom vide:
L = []
for i in range(5):
    L.append(i)
print(L)   # [0, 1, 2, 3, 4]

g = (i*2 for i in range(10))
for i in g:
    print(i)
  #  0
  #  2
  #  4
  #  6
  #  8
  #  10

#Spisok nechetnyh chisel
L = [i for i in range(10) if i % 2 ]
print(L)  #  [1, 3, 5, 7, 9]

#eto to zhe samoe, zapisannoe v prostom vide:
L = []
for i in range(10):
    if i % 2:
        L.append(i)
print(L)  # [1, 3, 5, 7, 9]

#Generator kortezha:
#kort = (i for i in range(5))  Ne rabotaet ???
#print(kort, type(kort))

#Generator spiska:
spis = [i for i in range(5)]
print(spis, type(spis))  # [0, 1, 2, 3, 4] <class 'list'>

#Generator slovarya:
dict = {i: i +5 for i in range(5)}
print(dict, type(dict))   # {0: 5, 1: 6, 2: 7, 3: 8, 4: 9} <class 'dict'>


# 3) Funkcii-generatory
def power(start):
    print("Power is called the first time")
    for i in range(start, start + 5):
        yield i ** 2
    print("Power is called the last time")

p1 = power(5)
print(type(p1))  # <class 'generator'>
for i in p1:
    print(i)
#25
#36
#49
#64
#81

# 4) Funkciya MAP  (ona primenyaet funkciyu(naprimer ord) k kazhdomu chlenu posled-ti('spam' )
m = map(ord, 'spam')
print(list(m))  #  poluchaem chislovie kody bazhdoi bukvy

# 4) Funkciya filter
L = [1, 0, None, 5, True]  # Nam nado vernut' znacheniya ne 0 i ne None
print(list(filter(bool, L)))  # [1, 5, True]

#to zhe samoe
print([i for i in L if i])  # [1, 5, True]

# 4) Funkcii ANY/ALL
L = [1, 0, None, 5, True]
print(any(L))  # True  (hotya by odin iz elementov imeet znachenie True (suschestvuet) )
print(all(L))  # False  Vse znacheniya elementov imeyut znachenie True (suschestvuyut) )


