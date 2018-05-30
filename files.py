# 1)Otkritie faila
print("\n***** Otkritie faila *****")

#1 sposob
myfile = open('file.txt')  # with encodong: myfile = open('file.txt', encoding='cp1251')
for line in myfile:
    print(line)
myfile.close()

#2 sposob (luchshe, t.k. on sam zakrivaet faily) (S 3 versii)
with open('file.txt') as myfile:
    for line in myfile:
        print(line)
        
#3 sposob       
for line in open('file.txt'):
    print(line.strip())
    
myfile = open('file.txt') 
myfile.readline()       # read only one line
myfile.read()           # read all file
myfile.readlines()      # read all lines in 
myfile.seek()           # return to first line
myfile.close()          # close file
    
### Write to file:
#1 sposob
myfile = open('fl.txt', 'w')
myfile.write("first string \n")
myfile.write('second string')
print("text", file=myfile)
myfile.close()

#2 sposob   With context manager
with open('fl.txt', 'w') as file:
    file.write('Hello')
