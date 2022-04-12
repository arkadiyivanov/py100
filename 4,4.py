#Задано натуральные числа от 10 до N. Вывести нечетные кратные пяти числа.


n = int(input("Введите Число N:"))
num = 0
for num in range(10, n):
        if num % 2 ==1 and num % 5 == 0:
                print(num)







