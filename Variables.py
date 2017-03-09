# 1)How to define variable type
a = 55
type(a)
type("efsf")
#<class 'str'>, <class 'int'>

# 2)Convert binary to decimal
0b11111111

# 3)Convert oct to decimal
0o45466

# 4)Convert oct to decimal
print(0x45466FA)

# 5)Output variable
number=546346
print(number)

# 6)Result of previous operation (available only in console)
#type(_)

# 7)Convert string to int
string_value="15"
result=int(string_value)
print(result)

# 8)Convert string to int and add 5
string_value="15"
result=int(string_value)
print(result + 5)

# 9)True is 1, False is 0
bool1=True
bool2=False
print(bool1,bool2)
print(bool1+bool2)
print(bool1+7)

# 10)Float values
a=0.5
print(type(a)) #<class 'float'>

# 10)Also float values
a=1.0
b=4.
print(type(a),type(b)) #<class 'float'><class 'float'>

# 11)Exponential (3.2 - mantissa, e5 - exponenta
a=3.2e5 #this equal 320000.0
print(a)
b=3.7e-3 #this equal 0.0037
print(b)

# 12)Convert int to float, float to int
a=10; print(type(a)) #int
b=float(a);print(type(b)) #float
c=int(b);print(type(c)) #and again int
d=int(5.4); print(d) #will be 5 (rounded)

# 13)Dynamic typing
a="String value"
print(type(a))  #<class 'str'>
a=10
print(type(a)) #<class 'int'>

# 13)Strong typing
a='5' #string
b=10
#print(a+b) #error

# 13)Operations
a=2+3*5-1
print(a)
a=6//4 #celochislennoe delenie
print(a) #1
a=6%4 #ostatok ot deleniya
print(a) #2

# 14)Another operations
a=-6
print(abs(a)) #po moduliu (menyaet - na +
a=2**4 # 2 v stepeni 4
print(a) #16
a=pow(2,4)# 2 v stepeni 4
print(a) #16
b=3.444
print(round(b)) #=3, okruglenie
print(round(b,2)) #=3.44, okruglenie lj 2 znakov posle zapyatoi

# 14)Python2 and Python3 differs
print(2/8) #in Python2 = 0 (because result is int)
print(2/8) #in Python3 = 0.25 (because result is float)
print(float(2)/8) #Wright way for Python2

# 15)Arithmetic operations
import math
x = 3.265
print('x=', x)
print('trunc x =', math.trunc(x)) #otbrasivaet drobnuyu chast
print('floor x =', math.floor(x)) #round to lower value
print('ceil x =', math.ceil(x)) #round to higher value
print(math.pi) #Pi value
print(math.sin(math.pi/4)) #Pi value
print(math.cos(10))
print(math.sqrt(16))

# 15)Logic Operations
print(True and False) #false
print(True or False) #true
print(not True and(True or False))#false
print(2>3)#false
print(5 == 5)#true (Equal)
print(5 != 5)#false (Not equal)
print(2 is 2) #True The same place in memory
print(id(a)) #Show place in memory(for ex. 18668160)
print(2<5<=8) #true
print(2==5==6)#false


# 16) Mnozhestvennye prisvoeniya
a = b = c = 1
print("{}, {}, {}".format(a, b, c))

# 17) Mnozhestvennye prisvoeniya (eschio sposob)
a, b, c = 1, 5, 'stringos'
print("{}, {}, {}".format(a, b, c))

# 18) Udalenie peremennyh
del a
# print("{}, {}, {}".format(a, b, c))  ERROR: NameError: name 'a' is not defined

# 19) Preobrazovaniee peremennyh
x = 5
base = 6
#int(x [,base]), float(x), str(x) chr(x), unichr(x), ord(x), hex(x), oct(x)








