# Напечатать таблицу умножения до n.
while True:
     n = int(input("Введите число то которого необходимо распечатать таблицу умножения  "))

     for row in range(1, n + 1):
         for column in range(1, n + 1):
             print(row * column, end='\t')
         print()





