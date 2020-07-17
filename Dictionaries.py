# 1) Sozdanie slovarya (klyuch - znachenie)
print("\nSozdanie slovarya (klyuch - znachenie)", end="\n")
dict0 = {}
dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}
dict3 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

mulist = [1, 2, 3, 4, 5]
dictx = {1: mulist, 2: 5}
print(dictx)  # [1, 2, 3, 4, 5]


#dict4 = {'Alice': '2341', 'Alice': '2341'}  # Duplicate keys


# 2) Prosmotr slovarya
print("\nProsmotr slovarya", end="\n")
print(dict0)  # {}
print(dict1)  # {'abc': 456}
print(dict2)  # {'abc': 123, 98.6: 37}
print(dict3)  # {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dict3['Alice'])  # 2341

#print(dict3['No'])  # KeyError: 'No' T.k. takogo klyucha net
print(dict3.get('No'))  # None - Chtobi ne bylo oshibki
print(dict3.get('No', 'No such key'))  # No such key  - with default value

print(list(dict3.keys()))  # ['Alice', 'Cecil', 'Beth']
print(list(dict3.values()))  # ['9102', '3258', '2341']
print(list(dict3.items()))  # [('Beth', '9102'), ('Cecil', '3258'), ('Alice', '2341')]



# 3)Izmenenie slovarya
print("\nIzmenenie slovarya", end="\n")
print(dict3)
dict3['Alice'] = '500$, 6, Hello'
print(dict3)  # {'Alice': '500$, 6, Hello', 'Beth': '9102', 'Cecil': '3258'}
del dict3['Alice']
print(dict3)  # {'Beth': '9102', 'Cecil': '3258'}
dict.clear(dict3)
print(dict3)  # {}
del dict3
#print(dict3)  # NameError: name 'dict3' is not defined

dict3 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(dict3)
dict3.pop('Alice')  # removes key
print(dict3)  # {'Beth': '9102', 'Cecil': '3258'}
dict3.popitem()
print(dict3)  # randomno udalyaet paru klyuch-znachenie iz slovarya
dict3.update({'one': 1, 'two':2})
print(dict3)  # {'one': 1, 'two': 2, 'Beth': '9102'}
dict3.update(dict2)
print(dict3)  # {98.6: 37, 'Cecil': '3258', 'abc': 123, 'one': 1, 'two': 2}

# 4)Dictionary functions
print("\nDictionary functions", end="\n")
mydict = {'Alice': 2341, 'Beth': 9102, 'Cecil': 3258}
print(mydict)
print(len(mydict))  # 3
print(type(mydict))  # <class 'dict'>
print(type(mydict['Alice']))  # <class 'int'>

#copying the dictionary
dictNew = mydict.copy()
print(dictNew)

#create dict from array
seq = ('name', 'age', 'sex')
dictNew1 = dict.fromkeys(seq)
print(dictNew1)  # {'age': None, 'sex': None, 'name': None}

dictNew1 = dict.fromkeys(seq, "not set val")  # without default None
print(dictNew1)  # {'sex': 'not set val', 'age': 'not set val', 'name': 'not set val'}

# 5) Iterations
students = {"Mike": 19, "Nick": 35, "Shane": 21}

for student in students:
    print(f"student: {student}: {students[student]}")

# The same
for student, age in students.items():
    print(f"student: {student}, {age}")
    
# Summ of values
print(sum(students.values()))
