# 1)Otkritie faila
print("\n***** Otkritie faila *****")

#1 sposob
myfile = open('file.txt')
for line in myfile:
    print(line)
myfile.close()

#2 sposob (luchshe, t.k. on sam zakrivaet faily) (S 3 versii)
with open('file.txt') as myfile:
    for line in myfile:
        print(line)