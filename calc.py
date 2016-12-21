a = input("Input first value: ")
print(type(a))
if type(a) != "<class 'str'>":
    val1 = int(a)
else:
    print("Wrong input. Please, enter cipher!")

b = int(input("Input second value: "))
if type(b) != 'str':
    val2 = int(b)
else:
    print("Wrong input. Please, enter cipher!")

c = input("Input operation: ")


if c == "+":
    result = val1 + val2
elif c == "-":
    result = val1 - val2
elif c == "*":
    result = val1 * val2
elif c == "/":
    result = val1 / val2
else:
    result = ""

if result:
    print("a + b = ", result)
else:
    print("Wrong operation!")
