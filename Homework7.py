#task 7
# from collections import Counter
#f = open('random.txt', 'r')
#a = 0
#data = f.read()
#s = Counter(data.split())
#s1 = sorted(s.items(), key=lambda item: item[1], reverse = True)
#for i , value in s1:

#    if a == 5:
#     break
#    a = a + 1
#    print(i , value)
#-------------------------------------------------------------------------
#Task 1
#number = []
#file = open('random.txt', 'r')
#data = file.read()
#for i in data:
# if i.isdigit():
#   number.append(i)
#print(number)
#---------------------------------------------------------------------------
#Task 3 -----------------------------
#f = open('data.txt' , 'w')
#b = int(input('Enter value N: '))
#for i in range(b):
# a = f.write(str(input('Enter value N: ')))
# a = a + 1

#f = open('random.txt' , 'w')
#b = int(input('Enter value N: '))
#data = ''
#for i in range(b):
#    data += (str(input('Enter value N: '))) + ' '

#f.write(data)
#print('Числа записани в файл')
#--------------------------------------------------------------------------------------
#Task 2
#f = open('random.txt' , 'w')
#a = f.write(str(input('Enter value N: ')))
#print('Текст запиан в файл')

#------------------------------------------------------------------------------------------
#Task 4
#import random
#f = open('random.txt' , 'w')
#for _ in range(100):
#    b = (random.randint(1, 100))
#    a = f.write(f'{b} \n')
#print('Чтсла успешно добавились в список')
#---------------------------------------------------------------------------------------------

#Task 5
#file = open('random.txt')
#words = 0
#for line in file.split:
#     count_Words = file.split()
#     words = words + count_Words

#print("Words:", words)
#---------------------------------------------------------------------------------------------
#Task 6
#with open('random.txt') as file:
#    for line in file.read().splitlines():
#        print(sum(map(int, line.split())))