
# ввод только целых чисел
def input_int():
    while True:
        try:
            num = int(input())
        except:
            print("Ошибка ввода! Введите целое число")
        else:
            break
    return num

# ввод только целых чисел в диапазоне от a до b
def input_int_limited(a, b):
    while True:
        try:
            num = int(input())
        except:
            print("Ошибка ввода! Введите целое число")
        else:
            if num > a and num < b:
                break
    return num

# ввод последовательности только целых чисел через пробел
def input_int_spaced():
    while True:
        try:
            numbers_str = input().split(' ')
            numbers = []
            for i in numbers_str:
                numbers.append(int(i))
        except:
            print("Ошибка ввода! Введите целые числа через пробел")
        else:
            break
    return numbers

# таблица умножения
def task1():
    print("|--- 1. Фрагмент таблицы умножения ---|")
    print("Введите начало таблицы построкам: ", end='')
    a = input_int_limited(0, 10)
    print("Введите конец таблицы построкам: ", end='')
    b = input_int_limited(0, 10)
    print("Введите начало таблицы столбцам: ", end='')
    c = input_int_limited(0, 10)
    print("Введите конец таблицы столбцам: ", end='')
    d = input_int_limited(0, 10)

    for i in range(c, d + 1, 1):
        print("\t", i, end='')

    for i in range(a, b + 1, 1):
        print("\n", i, "\t", end='')
        for j in range(c, d + 1, 1):
            print(i * j, "\t", end='')

# ввод чисел меньше 100
def task2():
    print("|--- 2. Ввод чисел меньше 100 и вывод чисел меньше 10 ---|")
    print("Вводите числа")
    while True:
        num = input_int()
        if num > 100:
            print("Ввод остановлен")
            break
        elif num < 10:
            print(">> ", num)

# сумма введённых чисел
def task3():
    print("|--- 3. Сумма введённых чисел ---|")
    sum = 0
    num = 1
    print("Вводите числа")
    while num != 0:
        num = input_int()
        sum += num
    print("Сумма: ", sum)

# минимальное количество кусков торта
def task4():
    print("|--- 4. Минимальное количество кусков торта ---|")
    print("Введите количество участников первой команды:")
    a = input_int()
    print("Введите количество участников второй команды:")
    b = input_int()
    d = a if a < b else b
    while True:
        if d % a == 0:
            if d % b == 0:
                break
            else:
                d += 1
        else:
            d += 1
    print("Количество кусков торта: ", d)

# среднее арифметическое всех чисел диапазона, кратных 3
def task5():
    print("|--- 5. Среднее арифметическое всех чисел диапазона, кратных 3 ---|")
    print("Введите начало диапазона:")
    a = input_int()
    print("Введите конец диапазона:")
    b = input_int()
    sum = 0
    count = 0
    for i in range(a, b + 1, 1):
        if i % 3 == 0:
            sum += i
            count += 1
    print("Среднее арифметическое всех чисел диапазона, кратных 3: ", sum / count)

# GC-состав генома
def task6():
    print("|--- 6. GC-состав генома ---|")
    print("Введите геном:")
    while True:
        genome = input().lower()
        if genome.isalpha():
            break
        print("Ошибка ввода! Введите геном, используя только прописные или заглавные буквы латинского алфавита")
    g_count = 0
    c_count = 0
    for i in genome:
        g_count += 1 if i == 'g' else 0
        c_count += 1 if i == 'c' else 0
    print(f"GC-состав: {(g_count + c_count) / len(genome) * 100}%")

# кодировка генома
def task7():
    print("|--- 7. Кодировка генома ---|")
    print("Введите геном: ", end='')
    while True:
        genome = input()
        if genome.isalpha():
            break
        print("Ошибка ввода! Введите геном, используя только прописные или заглавные буквы латинского алфавита")
    result = ""
    current_char = genome[0]
    current_count = 0
    for i in genome:
        if i == current_char:
            current_count += 1
        else:
            result += f"{current_char}{current_count}"
            current_char = i
            current_count = 1
    result += f"{current_char}{current_count}"
    print(f"Закодированный геном: {result}")

# сумма чисел в строке
def task8():
    print("|--- 8. Сумма чисел в строке ---|")
    print("Введите числа в одну строку, разделяя пробелами")
    numbers = input_int_spaced()
    sum = 0
    for i in numbers:
        sum += int(i)
    print(f"Сумма чисел в строке: {sum}")

# суммы соседних чисел в строке
def task9():
    print("|--- 9. Суммы соседних чисел в строке ---|")
    print("Введите числа в одну строку, разделяя пробелами")
    numbers = input_int_spaced()
    if len(numbers) > 1:
        result = f"{numbers[-1] + numbers[1]} "
        for i in range(1, len(numbers) - 1, 1):
            result += f"{numbers[i - 1] + numbers [i + 1]} "
        result += f"{numbers[-2] + numbers[0]} "
    else:
        result = f"{numbers[0]}"
    print(f"Суммы соседних чисел\n{result}")

# повторяющиеся числа
def task10():
    print("|--- 10. Вывод повторяющихся более 1 раза чисел ---|")
    print("Введите числа в одну строку, разделяя пробелами")
    numbers = sorted(input_int_spaced())
    current_num = numbers[0]
    current_count = 0
    result = ""
    for i in numbers:
        if i == current_num:
            current_count += 1
        else:
            result += f"{current_num} " if current_count > 1 else ""
            current_num = i
            current_count = 1
    print(f"Повторяющиеся более 1 раза\n{result}")

# сумма квадратов введённых чисел
def task11():
    print("|--- 11. Сумма квадратов введённых чисел ---|")
    print("Вводите числа построчно, пока их сумма не станет равна нулю")
    num = input_int()
    sum = num
    sum_square = num * num
    while sum != 0:
        num = input_int()
        sum += num
        sum_square += num * num
    print(f"Сумма квадратов введённых чисел: {sum_square}")

# вывод части числовой последовательности
def task12():
    print("|--- 12. Вывод части числовой последовательностие ---|")
    print("Введите количество символов для отображения: ", end='')
    count = input_int()
    result = ""
    i = 1
    while len(result) / 2 < count:
        result += f"{str(i)} " * i
        i += 1
    result = result[:count * 2 - 1]
    print(result)

print("Введите номер задания: ", end='')
task_num = input_int()
if task_num == 1:
    task1()
elif task_num == 2:
    task2()
elif task_num == 3:
    task3()
elif task_num == 4:
    task4()
elif task_num == 5:
    task5()
elif task_num == 6:
    task6()
elif task_num == 7:
    task7()
elif task_num == 8:
    task8()
elif task_num == 9:
    task9()
elif task_num == 10:
    task10()
elif task_num == 11:
    task11()
elif task_num == 12:
    task12()
else:
    print("Задания с таким номером не найдено!")