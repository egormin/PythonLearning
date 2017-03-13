##Mnozhestva - ih otlichie v tom, chto oni ne soderzhat povtoryzyuschihsya elementov
#elementy v nem ne uporyadochena i k elementu nelzya obratitsya po imeni. Tol'ko pereborom

# 1) Sozdanie mnozhestv
print("\nSozdanie mnozhestv")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # {'banana', 'pear', 'orange', 'apple'}

a = set('abracadabra')  # {'b', 'd', 'a', 'r', 'c'}
b = set('alacazam')     # {'l', 'm', 'a', 'z', 'c'}
print(a)
print(b)


# 2) Rabota s mnozhestvami
print("\nRabota s mnozhestvami")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('orange' in basket)
print('crabgrass' in basket)

# 2) Operacii s mnozhestvami
print("\nOperacii s mnozhestvami")
mnozh1 = {1, 2, 3}
mnozh2 = {2, 3, 4}
print(mnozh1-mnozh2)  # 1  (to chto est v mnozh1 chego net v mnozh2)
print(mnozh2-mnozh1)  # 4  (to chto est v mnozh1 chego net v mnozh2)
print(mnozh2 & mnozh1)  #  2,3  (cifri, obschie v mnozh1 i mnozh2)
print(mnozh2 | mnozh1)  #  1, 2, 3, 4 (obyedinenie mnozh1 i mnozh2)
print(mnozh2 ^ mnozh1)  # 1, 4  (vse krome obschih)


# Preobrazovanie spiska v mnozhestvo
spisok = [1, 2, 5, 6]
mnozhestvo = set(spisok)