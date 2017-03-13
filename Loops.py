# In Python used next types of loops:
# While
# FOR
# Not used DO-WHILE

# 1) Loops
count = 0
while count < 10:
    print(count)
    count += 1

# 2) Loops
a = 1
while a > 0:
    a = int(input("Enter cipher: "))
print("You have entered negative cipher {}".format(a))


# 3) Loops
response = ""
while response != 'exit':
    response = input("Enter command: ")

# 4) Beskonechnyi cikl
# n = 2
# while True:
     # print(n)
     # n = n ** 2

# 5) Break
stroka = ""
while True:
    a = input("Enter command: ")
    if a == 'exit':
        break

# 6) Continue
counter = 0
while counter <= 10:
  counter += 1
  if counter == 5 or counter == 6:
     continue
  print(counter)

# 7) As variant
  name = ""

  while True:
      print("""MENU
   1. Enter your name
   2. Enter greetings
   3. Exit
  """)

      choice = input("Make your choose: ")

      if choice == "1" or choice == 1:
          name = input("Enter your name, patsan: ")
      elif choice == "2":
          if name:
              print("Nice to meet you,", name, "!!!")
          else:
              print("You did not enter the name")
      elif choice == "3":
          break
      else:
          print("Wrong input, mother fucker")


# 8) ELSE with WHILE. (Esli byl ispolzovan brake, to else vypolnyatsya ne budet)
a = 0
while a < 5:
    print(a)
    a += 1
else:
    print("Finish")


# 9) ELSE with WHILE.
print()

attempts = 3

while attempts > 0:
    attempts -= 1
    passw = input("Enter your password:  ")
    if passw == "xxx":
        print("Access Granted")
        break
    else:
        print("Password is wrong, you have", attempts, "attempts")
else:
    print("Access Denied")


# 10) FOR
print("***** FOR *****")
for i in range(5):
    print(i)

for i in range(5, 10):
        print(i)

for i in range(5, 10, 2):  #2 - step
        print(i)

for i in range(10, 0, -1):
        print(i)

print("#####")
for _ in range(1, 7, 2):
            print(_)

#In Python 2 xrange   !!!!!!!!

# 11) Break, Continue and Else in FOR
for i in range(0, 10):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
else:
    print("Finished")

# 12) Eschyo odin variant cikla
l = [i for i in range(10)]
print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 12)ENUMERATE
sequence = ["a", "b", "c", "d"]
for idx, item in enumerate(sequence):
    print(item, idx)
  #  a 0
  #  b 1
  #  c 2
  #  d 3


sequence = ["a", "b", "c", "d"]
print(list(enumerate(sequence)))  #  [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
