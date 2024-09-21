n= int(input("Введите количество школьников: "))
k= int(input("Введите количество яблок: "))
for_one=(k//n)
print(f'{for_one} яблоко каждому  из лиц')
ostatok=k%n
if k%n !=0:
    print(f'{ostatok} яблок осталось в корзине')
else:
    print('Яблок в корзине не осталось')
if n>k:
    print('На всех яблок не хватит')
