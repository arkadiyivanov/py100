#Записать логическое выражение определяющее, что натуральное число А является трехзначным

n = int(input("Введите число  "))
if n >= 100 and n <1000:
    print ("Число трёхзначное ")
else:
    print('Число не трёхзначное')