#task 1
#Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
#В исходном списке минимум 2 элемента.

#def change1(lst=[]):
#    lst[0],lst[-1] = lst[-1],lst[0]
#    return numbers

#print(change1([1,9,2,4,1,4,5,1,5]))

#Task2
#Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением.
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

#def to_dict(lst=[]):
#    return {element: element for element in lst}

#print(to_dict([1,2,3,4,5]))

#task3
#Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно.
#Если пользователь задаст первое число большее чем второе, просто поменяйте их местами
#def sum_range(start, end):
#  if start > end:
#    start, end = end, start
#  return sum(range(start, end+1))

#print(sum_range(1, 5))

#task
#Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).

#def read_last(lines, file):
#  with open(file) as f:
#    lines_in_file = sum(1 for line in f)
#    f.seek(0)
#    for i, line in enumerate(f):
#      if i >= lines_in_file - lines:
#        print(line.strip())

# Read the last 2 lines of the file 'my_file.txt'
#read_last(2, 'my_file.txt')
