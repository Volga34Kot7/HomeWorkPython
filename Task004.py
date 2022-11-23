# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

coordinate_num = int(input('Введите номер четверти: '))
if coordinate_num == 1:
    print('x > 0 and y > 0')
elif coordinate_num == 4:
    print('x > 0 and y < 0')
elif coordinate_num == 2:
    print('x < 0 and y > 0')
elif coordinate_num == 3:
    print('x < 0 and y < 0')
elif coordinate_num < 1 or coordinate_num > 4:
    print('Введено неверное число')