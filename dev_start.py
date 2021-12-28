print('Начните ввод числе по одному, для окончания ввода нажмите Enter ')
first_list = []
while True:
    user_input = input('Введите число ')
    if user_input == '':
        break
    else:
        if user_input.isdigit():
            first_list.append(float(user_input))
        else:
            print('Вы ввели не число, повторите ввод')

second_list = []

for i in first_list:
    fracture = i % 2
    if fracture == 0:
        second_list.append(i)

print(f'Массив целых чисел {second_list}')

