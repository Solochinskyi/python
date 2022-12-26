def is_power_of_two(number):
    if number <= 0:
        return 'no'
    while number > 1:
        if number % 2 != 0:
            return 'no'
        number = number // 2
    return 'yes'


print(is_power_of_two(32))

#task
#Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes' если number является степенью двойки, иначе 'no'.
#Запрещено пользоваться функцией или оператором возведение в степень.
