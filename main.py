n= int(input("Введите количество школьников: "))
k= int(input("Введите количество яблок: "))
for_one=(k//n)
print(f'{for_one} яблоко каждому  из лиц')
ostatok=k%n
print(f'{ostatok} яблок осталось в корзине')
