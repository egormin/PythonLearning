# 1) Conditions
print("\n***** IF *****")
a = 10
if a > 5:
    print("a > 5")
    print("Hello")

# 2) Conditions (Not recommended way)
a = 10
if a > 5:  print("a > 5");  print("Hello")

# 3) Proverka na nalichie znacheniya peremennoy
if a is not None:
   print("Not none")

# 4) Pass - no any actions. And special comment TODO
if a is not None:
 pass   # TODO: add some logic later

# 5) IF ELSE
print("\n***** IF ELSE *****")

x = 5
if x > 10:
    y = "more than 10"
else:
    y = "less than 10"
print(y)

# 5)Mozhno i tak
x = 5
if 0 < x < 7:
    print("ok")


# 6)Vlozhennie usloviya
print()
x = int(input("Enter any cipher: "))
if x > 10:
    if x > 20:
        print("X > 20")
    else:
        print("X from 10 to 20")
else:
    if x > 5:
        print("X from 5 to 10")
    else:
        print("X from 0 to 5")

# 7)ELSE IF (SWITCH CASE) (ELSE ne obyazatelno)
print("\n***** IF ELSE *****")
print()
x = int(input("Enter any cipher: "))
if 0 < x < 5:
    print("0 < X < 5")
elif 5 <= x < 10:
    print(" 5 <= X  < 10")
elif 10 <= x < 15:
    print(" 10 <= X  < 15")
else:
    print("  X > 15")

# 8)ELSE IF (SWITCH CASE)
print("\n***** AS SWITCH CASE *****")
print("""MENU:
  1. Drink
  2. Eat
  3. Exit
""")
choice = str(input("Make your choice, bro: "))
if choice == "1":
    print("You have entered Drink")
elif choice == "2":
    print("You have entered Eat")
elif choice == "3":
    print("Bye!!!")
else:
    print("Incorrect choice")

# 9)TERNARY
print("\n***** TERNARY OPERATORS *****")
x = 75
res = "x less than 100" if x < 100 else "x more than 100"
print(res)
# OR print("x less than 100" if x <100 else "x more than 100")
res = ("x less than 50" if x < 50 else "x more than 50") if x < 100 else "x more than 100"  # Mozhno i bez ()
print(res)

# 10)Examples
print("\n***** EXAMPLES *****")
val = 0
if val is not None and val != "":
    print("val Exist")
# Similar with (but it defines 0)
if val:
    print("val Exist")
else:
    print("val equal 0")

# 11)Also examples
False or 5  # 5
True or 5   # True
False and 5  # False
True and 5  # 5
5 or 3   # 5
5 and 3  # 3
is_ready = False
is_ready and "Ready" or "Not Ready yet"  # 'Not Ready yet'
is_ready = True
is_ready and "Ready" or "Not Ready yet"  # 'Ready'

# 12)Also examples
# Two different objects
a = ["text", "also"]
b = ["text", "also"]
>>> id (a)
2115912146504
>>> id (b)
2115912146632
>>>a is b #false

# Same objects
>>> a = b
>>> id (a)
2115912146632
>>> id (b)
2115912146632
>>> a is b
True

# Operator chlenstva
p = (4, "frog", 9, -33, 9, 2)
>>> 2 in p #True


>>> phrase = "Peace is no longer permitted during Winterval"
>>> "v" in phrase
True
>>> "ring" in phrase
True









