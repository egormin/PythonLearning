# 1) Any way ('' or "")
string1 = 'string1'
string2 = "string2"
print(string1, string2)

# 2) Perenos stroki \
string1= "first line of text. " \
         "second line of text"  # first line of text second line of text
string2 = "first line of text.  \
          second line of text"  # first line of text.            second line of text (save all spaces in text)
string3 = "First line of text. \nSecond line of text"  # Perenos texta na novuyu stroku
print(string1)
print(string2)
print(string3)

# 3) Ekranirovanie
string4 = "First line of text. \\ Second line of text"  # ekranirovanie (First line of text. \ Second line of text)
string5 = 'First line \"<tr>\"of text.  Second line of text'  # ekranirovanie ("<tr>")
print(string4)
print(string5)

# 4) Multiple strings
multiple_string="""
Select operation type:
  1. Umnozhenie
  2. Delenie
  3. Slozhenie
  4. Vychitanie"""
print(multiple_string)

# 5) Operations with strings
string1='one,'
string2='two'
result=string1+string2
print(result)  # one,two
print(string1 + string2)  # one,two
print(string1[0])  # o
print(string1[0], string1[1], string1[2]) # o n e

# C formatting
res = 'number = %d' % 17  # for decimal value (17)
print(res)
res = 'number = %f' % 17  # for float value (17.000000)
print(res)
res = 'number = %4.2f' % 17  # for float value (17.00). 4-number of all symbols, 2-number of symbols after ,
print(res)
res = '%s = %d' % ('number', 42)  # number = 42
print(res)

# C# formatting
res = 'number={}'.format(17)  # number=17
print(res)
res = 'number1={},number2={},number3={}'.format(17, 21, 77)  # number1=17,number2=21,number3=77
print(res)
res = 'number1={2},number2={1},number3={0}'.format(17, 21, 77)  # number1=77,number2=21,number3=17
print(res)
res = 'number={:5.2f}'.format(17)  # number=17.00
print(res)
res = 'number={:f}'.format(17)  # number=17.000000
print(res)

# 6) Print format
print(2, 3, 5)  # 2 3 5 (space by default)
print(2, 3, 5, sep=":")  # 2:3:5
print(2, 3, 5, sep="")   # 235
print("hello!", end=" ")
print("Nigga", end="\n\n")  # hello! Nigga and 2 perenosa na sled. stroku

# 7) Input
string = input("Enter your name: ")
print("You have entered", string)  # You have entered egor
string = input("Enter your name: ")
print("You have entered \"", string, "\"", sep="")  # You have entered "sdg"
string = input("Enter your name: ")
print('You have entered "', string, '"', sep="")  # You have entered "sdg". To zhe samoe
string = input("Enter your name: ")
print('You have entered "{}"'.format(string))  # You have entered "sdg". To zhe samoe
#input() - waits for Enter button

val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))
print("{} + {} = {}".format(val1, val2, val1 + val2))


