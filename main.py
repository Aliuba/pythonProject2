# list = [22, 3, 5, 2,  8, 2, 2, -23, 8, 23, 5, 5, 22, 45, 45]
# print(list)

# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - найти min число в листе
# i = 0
# d = len(list)
# min = list[0]
# while i < d:
#     if list[i] < min:
#         min = list[i]
#     i += 1
# print(min)


#   - удалить все одинаковые значения

# list = [22, 3, 5, 2,  8, 2, 2, -23, 8, 23, 5, 5, 22, 45, 45]
# print(list)
# i = 1
# j = 0
#
# while j < len(list):
#    while i < len(list):
#        if list[i] == list[j]:
#           del list[i]
#           k = i
#           while k < len(list):
#              if list[k] == list[j]:
#                 del list[k]
#              k = k + 1
#           del list[j]
#           j = j-1
#        i +=1
#    j = j+1
#    i = j+1
# print(list)

# - заменить каждое четвертое значение на "Х"
# list = [22, 3, 5, 2,  8, 2, 2, -23, 8, 23, 5, 5, 22, 45, 45]
# print(list)
# print(list[::4])
# i = 0
# while i < len(list):
#     if i%4 == 0:
#        list[i] = "x"
#     i = i+1
# print(list)

# - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5
#
# list = [-10, 5, 5]
# i=0
# s=0
# a=0
# while i<len(list):
#     s = s+list[i]
#     a=s/len(list)
#     i +=1
# print(a, "середнє")
# m = list[0]
# j=0
# k = abs(list[0] - a)
# while j < len(list)-1:
#      if ( k > abs( list[j+1] - a )):
#         k = abs(list[j+1] - a)
#         print(k)
#         m = list[j+1]
#      j +=1
# print(m, 'найближче до середнього')

# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# a = input("input a: ")
# print(a)
# i=0
# list=''
# j=0
# k=0
# m=0
# while j< int(a):
#     if int(a)==1:
#         j=int(a)
#         print("*")
#
#     if j==0 :
#         while i<int(a)-1:
#             print("*", end=" ")
#             i +=1
#         if i == int(a)-1:
#              print("*")
#     if j<int(a)-2:
#         print("*", end=" ")
#         while k < int(a)-2:
#             print("_", end=" ")
#             k += 1
#         if k == int(a)-2:
#             print("*")
#         k=0
#     if j == int(a) - 1:
#         while m<int(a)-1:
#             print("*", end=" ")
#             m +=1
#         if m == int(a)-1:
#              print("*")
#     j+=1

# 3) переделать первое задание под меню с помощью цикла
# 1)Дан лист:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   1 найти min число в листе
#   2 удалить все одинаковые значения
#   3 заменить каждое четвертое значение на "Х"
#   4 вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# 5 exit
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5

# list =[22, 3,5,2,8,2,-23, 8,23,5]
# print(list)
# print("1 найти min число в листе")
# print("2 удалить все одинаковые значения")
# print("3 заменить каждое четвертое значение на X ")
# print("4 вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа")
# print("5 exit")
# m = input("зробіть свій вибір")
# if int(m) == 1:
#     # - найти min число в листе
#     i = 0
#     d = len(list)
#     min = list[0]
#     while i < d:
#         if list[i] < min:
#              min = list[i]
#         i += 1
#     print(min)
# if int(m) == 2:
#     i = 1
#     j = 0
#
#     while j < len(list):
#        while i < len(list):
#            if list[i] == list[j]:
#               del list[i]
#               k = i
#               while k < len(list):
#                  if list[k] == list[j]:
#                     del list[k]
#                  k = k + 1
#               del list[j]
#               j = j-1
#            i +=1
#        j = j+1
#        i = j+1
#     print(list)
#
# if int(m) == 3:
#     i = 0
#     while i < len(list):
#         if i%4 == 0:
#              list[i] = "x"
#         i = i+1
#     print(list)
#
# if int(m) == 4:
#     i=0
#     s=0
#     a=0
#     while i<len(list):
#         s = s+list[i]
#         a=s/len(list)
#         i +=1
#     m = list[0]
#     j=0
#     k = abs(list[0] - a)
#     while j < len(list)-1:
#          if ( k > abs( list[j+1] - a )):
#             k = abs(list[j+1] - a)
#             m = list[j+1]
#          j +=1
#     print(m, 'найближче до середнього')
#
# if int(m) == 5:
#     exit(1)

# 4) вывести табличку умножения с помощью цикла while

i=1
j=1
while i<10:
    while j<10:
        print(i*j, end=" ")
        j +=1
    print(" ")
    i += 1
    j=1






