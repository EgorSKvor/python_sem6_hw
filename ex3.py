# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]
lst = [1, 1, 2, 3, 4, 4, 4]
# unco_lst = []
# for i in range(len(lst)):
#     if lst.count(i) == 1:
#         unco_lst.append(lst[i])
#     else:
#         pass
# print(unco_lst)
new_lst = [i for i in range(len(lst)) if lst.count(i) == 1]
print(new_lst)
