import math
print("""\n*** E.G. Calc ***
   Available operations:
 1. Slozhenie  (+)
 2. Vychitaniy (-)
 3. Umnozhenie (*)
 4. Delenie    (/)
 5. Stepen     (step)
 6. Sinus      (sin)
 7. Cosinus    (cos)
 8. Tangens    (tan)
""")

val1 = int(input("Input first value: "))

val2 = int(input("Input second value: "))

c = input("Input operation: ")


if c == "+" or c == "1":
    result = val1 + val2
elif c == "-" or c == "2":
    result = val1 - val2
elif c == "*" or c == "3":
    result = val1 * val2
elif c == "/" or c == "4":
    result = val1 / val2
elif c == "step" or c == "5":
    result = math.pow(val1, val2)
elif c == "sin" or c == "6":
    result = math.sin(val1)
elif c == "cos" or c == "7":
    result = math.cos(val1)
elif c == "cos" or c == "7":
    result = math.tan(val1)
else:
    result = ""

if result:
    print("a + b = ", result)
else:
    print("Wrong operation!")
