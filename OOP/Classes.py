### 1) Simple Class:

class MyObj:   # Klassy opisyvayut to, chem budut yavliatsia ego objekty
    pass

obj = MyObj()

### 2) One link to the same object:
print(id(MyObj))
AnotherClass = MyObj
print(id(AnotherClass))
#20129208
#20129208

### 3) Class attributes:
class Class1:
    int_attr = 5
    str_attr = "one"

print("First attribut: {}, second attribut: {}".format(Class1.int_attr, Class1.str_attr))
#First attribut: 5, second attribut: one

obj1 = Class1()
obj2 = Class1()
print("First attribut: {}, second attribut: {}".format(obj1.int_attr, obj2.str_attr))
# The same result
#First attribut: 5, second attribut: one

obj1.int_attr = 10
print(obj1.int_attr)
print(obj2.int_attr)
#10   # Tak on ne menyaetsya, t.k. eto raznye objekty klassa
#5

class2 = Class1()
Class1.int_attr = 50
print(Class1.int_attr)
print(class2.int_attr)
#50   # Menyaetsya, tak kak class2 i Class1 bvt.n odnu i tu zhe ssilku
#50
print("Class1: {}, Class2: {}".format(id(Class1.int_attr), id(class2.int_attr)))
# Class1: 9171104, Class2: 9171104

Class1.int_attr = 77
print("Class1: {}, Class2: {}".format(Class1.int_attr, obj1.int_attr))
#Class1: 77, Class2: 77   #Esli ne izmenyat zaranee znachenie svoistva ekzemplyara


### 4) Class attributes:
class Person:
    pass

john = Person()
john.name = "John"     # Attribut dannyh. On est' tolko u ekzemplyara klassa. Eschio byavet attribut classa. On est' u vseh ekzemplyarov
john.age = 22

lucy = Person()
lucy.name = "Lucy"
lucy.age = 18

print(john.name, "is", john.age)
print(lucy.name, "is", lucy.age)
#John is 22
#Lucy is 18

### 5) Class attributes with self:
class Person2:
    def print_info(self):
        print(self.name, "is", self.age)

john = Person2()
john.name = "John"     # Attribut dannyh. On est' tolko u ekzemplyara klassa. Eschio byavet attribut classa. On est' u vseh ekzemplyarov
john.age = 22

lucy = Person2()
lucy.name = "Lucy"
lucy.age = 18

Person2.print_info(john)
Person2.print_info(lucy)

#John is 22  To zhe samoe
#Lucy is 18

### 6) Class attributes with self (Mozhno i tak):
class Person3:
    def print_info(self):
        print(self.name, "is", self.age)

john = Person3()
john.name = "John"     # Attribut dannyh. On est' tolko u ekzemplyara klassa. Eschio byavet attribut classa. On est' u vseh ekzemplyarov
john.age = 22

lucy = Person3()
lucy.name = "Lucy"
lucy.age = 18

john.print_info()
lucy.print_info()

#John is 22  I eto to zhe samoe
#Lucy is 18


### 6) Class attributes with self (Mozhno i tak):
print("\n*** Example 6 ***")

class Person4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age)

john = Person4("John", 20)
lucy = Person4("Lucy", 17)

john.print_info()
lucy.print_info()

#John is 20  To zhe samoe
#Lucy is 17  To zhe samoe

