#Записать условие, которое является истинным, когда каждое из чисел А и В нечетное.

A = int(input("Введите число А"))
B = int(input("Введите число B"))
if A % 2 !=0 and B % 2 != 0:
    print("А и B нечётные")
else:
    print("одно из чисел чётное")

