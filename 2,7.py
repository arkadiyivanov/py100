#Дано четырехзначное число. Определить: а) равна ли сумма двух первых его цифр сумме двух последних;
# б) кратна ли 7 сумма его цифр

while True:
        a = int(input('Введите четырёхзначное число  '))
        i = [int(i) for i in str(a)]
        if i[0] + i[1] == i[2] + i[3]:
           print('Сумма первых двух чисел равна сумме последних двух чисел')
        else:
           print('Сумма первых двух чисел НЕ равна сумме последних двух чисел')
        if sum(i) % 7 == 0:
           print('сумма цифр кратна 7')
        else:
           print('сумма цифр НЕ кратна 7')







