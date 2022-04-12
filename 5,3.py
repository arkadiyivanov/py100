#Определить, сколько в введенном пользователем числе четных цифр, а сколько нечетных.
if __name__ == '__main__':
     while True:
          a = int(input("Введите число"))
          even = 0
          odd = 0
          list_ = [int(a) for a in str(a)]
          for a in list_:
               if a % 2 == 0:
                    even += 1
               else:
                    odd += 1
          print("Чётных чисел = ", even, "Нечётных = ", odd)











