# 1) Dlina peremennoy
string = "Hello world"
print(len(string))  # 11

# 2) Upper/Lower
a = "HelLo"
print(a.lower())  # "hello"
print(a.upper())  # "HELLO"

# 3) Replace(old, new [, max])
a = "HelLo"
print(a.replace('H', 'B'))  # BelLo

b = "cucumber"
print(b.replace('u', 'O', 1))  # cOcumber  1 - zamenit tolko 1 raz, hot i 2 bukvy u

# 4) Split/Join (join(seq), split(str="", num=string.count(str)))
str = "hello, world, !"
newstr = str.split(",")
print(newstr)   # ['hello', ' world', ' !']
newstr1 = str.split(",", 1)
print(newstr1)   # ['hello', ' world, !'] # razbivaet tolko po 1 sovpadeniyu

seq = ("a", "b", "c")  # This is sequence of strings.
print('-'.join(seq))   # a-b-c
# OR
dev = ""
print(dev.join(seq))   # abc

# 5) Ends wits /Starts with (endswith(suffix, beg=0, end=len(string)), startswith(str, beg=0,end=len(string))
#Nachinaetsya/zakanchivaetsya li stroka s shablona 'string'
text = "Low Level Programming Department"
print(text.startswith('Low'))    # True
print(text.startswith('Level'))  # False
print(text.startswith(('Disc', 'Lo')))  # True

print(text.endswith('Department'))    # True
print(text.endswith('ming'))          # False


# 6) Trim (rstrip(), lstrip(), strip([chars]))
text = "  Low Level Programming Department         "
print(text.lstrip())    # 'Low Level Programming Department       '
print(text.rstrip())    # '  Low Level Programming Department'
print(text.strip())     # 'Low Level Programming Department'

# 7) Find / Count (find(str, beg=0 end=len(string)), count(str, beg= 0,end=len(string)))
text = "Low Level Programming Department"
print(text.find('Pr'))   # 10 10-ya bukva
print(text.find('e'))    # 5 5-ya bukva (nomer pervogo vhozhdeniya)

mass = ('odin', 'dva', 'tri', 'dva', 'dva')
print(mass.count('dva'))   # 3 vhozhdeniya
print(text.count('e'))   # 4 4-e bukvi e v tekste

















