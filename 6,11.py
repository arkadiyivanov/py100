# В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64.
# Дано натуральное число n.
# Как наименьшим количеством таких денежных купюр можно
# выплатить сумму n (указать количество каждой из используемых для выплаты купюр)?
# Предполагается, что имеется достаточно большое количество купюр всех достоинств.

while True:
    n = int(input("Введите натуральное число"))

    denomination = {64: 0, 32: 0, 16: 0, 8: 0, 4: 0, 2: 0, 1: 0}
    for num_ in dict(denomination):
        if n >= num_:
            denomination[num_] = denomination[num_] + 1
            n = n - num_
            if n // num_:
                denomination[num_] = denomination[num_] + 1
                n = n - num_




    print(denomination)


    # while n > 0:
    #     if n >= 64:
    #         n -= 64
    #         denomination[64] += 1
    #         if n == 0:
    #             print("Использованно купюр наминалом 64 = ", denomination[64], "шт.")
    #     elif n >= 32:
    #         n -= 32
    #         denomination[32] += 1
    #         if n == 0:
    #             print("Использованно купюр наминалом 64 = ", denomination[64], "шт.")
    #             print("Использованно купюр наминалом 32 = ", denomination[32], "шт.")
    #     elif n >= 16:
    #         n -= 16
    #         denomination[16] += 1
    #         if n == 0:
    #             print("Использованно купюр наминалом 64 = ", denomination[64], "шт.")
    #             print("Использованно купюр наминалом 32 = ", denomination[32], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[16], "шт.")
    #     elif n >= 8:
    #         n -= 8
    #         denomination[8] += 1
    #         if n == 0:
    #             print("Использованно купюр наминалом 64 = ", denomination[64], "шт.")
    #             print("Использованно купюр наминалом 32 = ", denomination[32], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[16], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[8], "шт.")
    #     elif n >= 4:
    #         n -= 4
    #         denomination[4] += 1
    #         if n == 0:
    #             print("Использованно купюр наминалом 64 = ", denomination[64], "шт.")
    #             print("Использованно купюр наминалом 32 = ", denomination[32], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[16], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[8], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[4], "шт.")
    #     elif n >= 2:
    #         n -= 2
    #         denomination[2] += 1
    #         if n == 0:
    #             print("Использованно купюр наминалом 64 = ", denomination[64], "шт.")
    #             print("Использованно купюр наминалом 32 = ", denomination[32], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[16], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[8], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[4], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[2], "шт.")
    #     elif n >= 1:
    #         n -= 1
    #         denomination[1] += 1
    #         if n == 0:
    #             print("Использованно купюр наминалом 64 = ", denomination[64], "шт.")
    #             print("Использованно купюр наминалом 32 = ", denomination[32], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[16], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[8], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[4], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[2], "шт.")
    #             print("Использованно купюр наминалом 16 = ", denomination[2], "шт.")
    # print(denomination)
        #






