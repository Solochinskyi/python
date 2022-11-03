
#Вывести треугольник #1 с шириной N с помощью цикла while
#n = 5
#while n:
#    print('*'*n)
#    n = n - 1

#Вывести треугольник #2 с шириной N с помощью цикла while
#n = 1
#while n:
#    if n == 6:
#        break
#    print('*'*n)
#    n = n + 1
#Вывести треугольник #4с шириной N с помощью цикла while
n = 1
stars = "     *"

while n:
    print(stars)

    stars = stars.replace(" *", "**")
    if n == 5:
        break

    n += 1

#Вывести треугольник #3с шириной N с помощью цикла while
n = 5
stars = "*" * n

while n:
    print(stars)
    stars = stars.replace("*", " ", 1)
    n -= 1