#Определить, является ли шестизначное число "счастливым"
# (сумма первых трех цифр равна сумме последних трех цифр).


while True:
    list_arg = str(input('Введите шестизначное число'))
    if len(list_arg) != 6:
        print('Число не является шестизначным')
    list_arg = [int(arg) for arg in str(list_arg)]
    if not sum(list_arg[:3]) == sum (list_arg[3:]):
        print("Число не является счастливым")
    if sum(list_arg[:3]) == sum(list_arg[3:]):
        print("Число является счастливым")

