#!/usr/bin/env python # -* - coding: utf-8-*
import math
import random
import re
import statistics
def first1():
    num = int(input("Введите число: "))
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            if i % 3 != 0:
                count += 1
    return num, count
def first2():
    num = int(input("Введите число: "))
    min = 9
    for i in str(num):
        if int(i) < min:
            min = int(i)
    return min
def first3():
    num = int(input("Введите число: "))
    s = 0
    p = 1
    for i in str(num):
        s += int(i)
        p *= int(i)
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            if math.gcd(s, i) == 1:
                if math.gcd(p, i) != 1:
                    count += i
    return s, p, count
def two(string):
    return "".join(random.sample(string, len(string)))
def three(s):
    s = s.lower().replace(' ', '')
    if s == s[::-1]:
        return True
    return False
def four(s):
    s.sort(key=len)
    return s
def five(text):
    pattern = r'\b\d{1,2}\s(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s\d{4}\b'
    dates = re.findall(pattern, text)
    return dates
def six(s):
    s = s.lower()
    max_rez = 0
    count = 0
    for c in s:
        if re.match('[а-яё]', c):
            count += 1
        else:
            max_rez = max(max_rez, count)
            count = 0
    return max_rez
def seven(s):
    return list(map(int, filter(str.isnumeric, s)))
def eight(s):
    max_count = 0
    current_count = 0
    for match in re.finditer(r'\d+', s):
        current_count = len(match.group(0))
        max_count = max(max_count, current_count)
    return max_count
def nine():
    strings = []
    n = int(input("Введите количество строк: "))
    print("Введите строки:")
    for _ in range(n):
        string = input()
        strings.append(string)
    sorted_strings = sorted(strings, key=len)
    print("Отсортированные строки:")
    for string in sorted_strings:
        print(string)
    return 'Сортировка завершена ☺\n 塵幗膂蓿f寥寢膃暠瘉甅甃槊槎f碣綮瘋聟碯颱亦尓㍍i:i:i;;:;:: : :\n澣幗嶌塹傴嫩榛畝皋i袍耘蚌紕欒儼巓襴踟篁f罵f亦尓㍍i:i:i;;:;:: : :\n漲蔭甃縟諛f麭窶膩I嶮薤篝爰曷樔黎㌢´　　｀ⅷ踟亦尓㍍i:i:i;;:;:: : :\n蔕漓滿f蕓蟇踴f歙艇艀裲f睚鳫巓襴骸　　　　　贒憊亦尓㍍i:i:i;;:;:: : :\n榊甃齊爰f懈橈燗殪幢緻I翰儂樔黎夢' '”　 　 ,ｨ傾篩縒亦尓㍍i:i:i;;:;:: : :\n箋聚蜚壊劑薯i暹盥皋袍i耘蚌紕偸′　　　 雫寬I爰曷f亦尓㍍i:i:i;;:;:: : :\n銕颱麼寰篝螂徑悗f篝嚠篩i縒縡齢　　 　 　 Ⅷ辨f篝I鋗f亦尓㍍i:i:i;;:; : : .\n碯聟f綴麼辨螢f璟輯駲f迯瓲i軌帶′　　　　　`守I厖孩f奎亦尓㍍i:i:i;;:;:: : : .\n綮誣撒f曷磔瑩德f幢儂儼巓襴緲′　 　 　 　 　 `守枢i磬廛i亦尓㍍i:i:i;;:;:: : : .\n慫寫廠徑悗緞f篝嚠篩I縒縡夢' '´　　　 　 　 　 　 　 `守峽f徑悗f亦尓㍍i:i:i;;:;:: : : .\n廛僵I數畝篥I熾龍蚌紕襴緲′　　　　　　　　　　　　　‘守畝皋弊i劍亦尓㍍i:i:i;;:;:: : : .\n瘧i槲瑩f枢篝磬曷f瓲軌揄′　　　　　　　　　　　　　,gf毯綴徑悗嚠迩忙亦尓㍍i:i:i;;:;::\n襴罩硼f艇艀裲睚鳫襴鑿緲''　　　　　　　　　　 　 　 奪寔f厦傀揵猯i爾迩忙亦尓㍍i:i:\n椈棘斐犀耋絎絲絨緲′　　　　　　 　 　 　 　 　 　 　 ”''罨悳萪f蒂渹幇f廏迩忙i亦尓㍍\n潁樗I瘧德幢i儂巓緲′　　　　　　 　 　 　 　 　 　 r㎡℡〟”''罨椁裂滅楔滄愼愰迩忙亦\n翦i磅艘溲I搦儼巓登zzz zzz㎜㎜ｧg　 　 緲 g　 　 甯體i爺ゎ｡, ”''罨琥焜毳徭i嵬塰慍絲\n枢篝磬f曷迯i瓲軌f襴暹 甯幗緲 ,fi''　　 緲'',纜｡　　贒i綟碕碚爺ゎ｡ ”罨皴發傲亂I黹靱\n緞愾慊嵬嵯欒儼巓襴驫 霤I緲 ,緲　　 ＂,纜穐　　甯絛跨飩i髢馳爺ゎ｡`等誄I筴碌I畷\n罩硼I蒻筵硺艇艀i裲睚亀 篳' '’,緲　　g亀 Ⅶil齢　　贒罩硼i艇艀裲睚鳫爺靠飭蛸I裘裔\n椈f棘豢跫跪I衙絎絲絨i爺i㎜iⅣ 　 ,緲i亀 Ⅶ靈,　　甯傅喩I揵揚惹屡絎痙棏敞裔筴敢\n頬i鞏褂f跫詹雋髢i曷迯瓲軌霤 　 ,緲蔭穐 Ⅶ穐 　 讎椈i棘貅f斐犀耋f絎絲觚f覃黹黍\n襴蔽戮貲艀舅I肅肄肆槿f蝓Ⅷ 　 緲$慚I穐,疊穐　 甯萪碾f鋗輜靠f誹臧鋩f褂跫詹i雋\n鋐篆f瘧蜑筴裔罩罧I緜孵蓼Ⅷ　 i鷆嫩槞i歉皸鱚　 冑縡諛諺彙溘嵳勠尠錣綴麼辨螢\n'
def ten():
    def sort_by_word_count(strings):
        # Сортировка списка строк по количеству слов в каждой строке
        return sorted(strings, key=lambda x: len(x.split()))

    strings = []
    n = int(input("Введите количество строк: "))
    print("Введите строки:")
    for _ in range(n):
        string = input()
        strings.append(string)

    sorted_strings = sort_by_word_count(strings)
    for string in sorted_strings:
        print(string)
    return '\n\nОХ УЖ ЭТИ РУССКИЕ ХАКЕРЫ\n⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿\n⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿\n⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿\n⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿\n⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿\n⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿\n⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿\n⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿\n⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿\n⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉\n⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄'
def eleven():
    def average_ascii_weight(string):
        total_weight = sum(ord(char) for char in string)  # Вычисляем сумму ASCII-кодов символов строки
        return total_weight / len(string) if len(string) != 0 else 0  # Возвращаем среднее значение или 0 для пустой строки

    def sort_by_average_ascii_weight(strings):
        return sorted(strings, key=average_ascii_weight)

    strings = []
    n = int(input("Введите количество строк: "))
    print("Введите строки:")
    for _ in range(n):
        string = input()
        strings.append(string)
    sorted_strings = sort_by_average_ascii_weight(strings)
    print('\n')
    for string in sorted_strings:
        print(string)
    return('Сортировка завершена')
def twelve():    
    rows = []
    n = int(input("Введите количество строк: "))
    print("Введите строки:")
    for _ in range(n):
        row = input()
        rows.append(row)
    sorted_rows = []
    while rows:
        medians = []
        for row in rows:
            medians.append(statistics.median(map(float, row.split())))
        min_index = medians.index(min(medians))
        sorted_rows.append(rows.pop(min_index))
    print('\n')
    for row in sorted_rows:
        print(row)
    return "Соритровка закончена"
def thirteen():
    rows = []
    n = int(input("Введите количество строк: "))
    print("Введите строки:")
    for _ in range(n):
        row = input()
        rows.append(row)
    sorted_strings = []
    sorted_strings = sorted(rows, key=lambda s: (max(map(ord, s)) - ord(s[len(s) // 2])) ** 2 +
                                                 sum((abs(ord(s[i]) - ord(s[-i - 1])) - (max(map(ord, s)) - ord(s[len(s) // 2]))) ** 2
                                                     for i in range(len(s) // 2)))

    for row in sorted_strings:
        print(row)
def fourteen():
    rows = []
    n = int(input("Введите количество строк: "))
    print("Введите строки:")
    for _ in range(n):
        row = input()
        rows.append(row)
    def quadratic_deviation(freq_common, freq_current):
        return (freq_current - freq_common) ** 2
    most_common = max(rows, key=lambda x: max(set(x), key=x.count))
    freq_common = most_common.count(max(set(most_common), key=most_common.count))
    deviations = [(row, quadratic_deviation(freq_common, row.count(max(set(row), key=row.count)))) for row in rows]
    sorted_strings = [pair[0] for pair in sorted(deviations, key=lambda x: x[1])]
    for row in sorted_strings:
        print(row)
def fiftheen():
    arr = []
    n = int(input("Введите количество элементов массива: "))
    for i in range(n):
        s = int(input("Введите элемент массива: "))
        arr.append(s)
    unique_element = 0
    for num in arr:
        unique_element ^= num
    if unique_element != 0:
        print("Значение отличающегося элемента:", unique_element)
    if unique_element == 0:
        print("Есть несколько отличающихся элементов")
def sixtheen():
    arr = []
    n = int(input("Введите количество элементов массива: "))
    for i in range(n):
        s = int(input("Введите элемент массива: "))
        arr.append(s)
    min1 = min2 = float('inf')
    for num in arr:
        if num < min1:
            min2 = min1  
            min1 = num   
        elif num < min2:
            min2 = num
    print("Два наименьших элемента массива:", min1, min2)
def seventheen(r,arr):
    min_diff = float('inf')
    closest_element = None
    
    for num in arr:
        diff = abs(r - num)
        if diff < min_diff:
            min_diff = diff
            closest_element = num
    
    print("Самое приближённое число: ",closest_element)
def eighteen():
    arr = []
    n = int(input("Введите количество элементов массива: "))
    for i in range(n):
        s = int(input("Введите положитльный элемент массива: "))
        if s > 0:
            arr.append(s)
        else:
            print("Читать умеешь?")
    divisors = []
    for num in arr:
        for i in range(1, num // 2 + 1):
            if num % i == 0 and i not in divisors:
                divisors.append(i)
        if num not in divisors:
            divisors.append(num)
    print("Положительные делители элементов списка:")
    print(divisors)
def ninetheen():
    arr = []
    n = int(input("Введите количество элементов массива: "))
    for i in range(n):
        s = int(input("Введите положитльный элемент массива: "))
        if s > 0:
            arr.append(s)
        else:
            print("Читать умеешь?")
    result = []
    counts = {}
    for num in arr:
        if num >= 0 and num < 100:
            counts[num] = counts.get(num, 0) + 1

    for num in set(arr):
        if num >= 0 and num < 100 and counts.get(num, 0) > 2:
            result.append(num ** 2)
    print(result)

    ##############
    # MAIN BLOCK #
    ##############

print("Выберите номер задания от 1 до 19")
nn = int(input("Номер: "))
if nn == 1:
    print("Выберите пункт:")
    print(" 1 - Найти количество делителей числа, не делящихся на 3:\n 2 - Найти минимальную нечетную цифру числа:\n 3 - Найти сумму всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа:")
    pp = int(input("Пункт: "))
    if pp == 1:
        numm, countt = first1()
        print("Количество делителей числа", numm, "равно", countt)
    elif pp == 2:
        minn = first2()
        print("Минимальная цифра числа", minn)
    elif pp == 3:
        sf, pf, countt = first3()
        print("Сумма делителей взаимно простых с", sf, "и не взаимно простых с", pf, "равно", countt)
    else:
        print("Не верный номер пункта")
if nn == 2:
    print("Задание: Дана строка. Необходимо перемешать все символы строки в случайном порядке.\n")
    s = input("Введите строку: ")
    randomized_string = two(s)
    print("Перемешанная строка:", randomized_string)
if nn == 3:
    print("Задание: Дана строка, состоящая из символов латиницы. Необходимо проверить, образуют ли прописные символы этой строки палиндром.\n")
    s = input("Введите строку: ")
    if three(s):
        print(s, "является палиндромом")
    else:
        print(s, "не является палиндромом")
if nn == 4:
    print("Задание: Дана строка в которой записаны слова через пробел. Необходимо упорядочить слова по количеству букв в каждом слове.\n")
    sf = input("Введите текст: ").split()
    print("Упорядоченные по длине слова:", *four(sf))
if nn == 5:
    print("Задание: Дана строка. Необходимо найти все даты, которые описаны в виде 31 февраля 2007.\n")
    sf = input("Введите строку: ")
    print("Все даты нужного вида:",five(sf))
if nn == 6:
    print("Задание: Дана строка. Необходимо найти наибольшее количество идущих подряд символов кириллицы.\n")
    sf = input("Введите строку: ")
    print("Максимальное количество символов кириллицы подряд равняется:", six(sf))
if nn == 7:
    print("Задание: Дана строка. Необходимо найти минимальное из имеющихся в ней натуральных чисел.\n")
    sf = input("Введите текст: ").split()
    minn = min(seven(sf))
    print("Минимальное натуральное число:", minn)
if nn == 8:
    print("Задание: Дана строка. Необходимо найти наибольшее количество идущих подряд цифр.")
    sf = input("Введите текст: ")
    print("Максимальное количество идуших подряд цифр:", eight(sf))
if nn == 9:
    print('Задание: Прочитать список строк с клавиатуры. Упорядочить по длине строки.')
    print(nine())
if nn == 10:
    print('Задание: Дан список строк с клавиатуры. Упорядочить по количеству слов в строке\n')
    print(ten())
if nn == 11:
    print('Задание: Отсортировать строки в порядке увеличения среднего веса ASCII-кода символа строки\n')
    print(eleven())
if nn == 12:
    print('Задание: Отсортировать строки в порядке увеличения медианного значения выборки строк (прошлое медианное значение удаляется из выборки и производится поиск нового медианного значения)\n')
    print(twelve())
if nn == 13:
    print('Задание: Отсортировать строки в порядке увеличения квадратичного отклонения между наибольшим ASCII-кодом символа строки и разницы в ASCII-кодах пар зеркально расположенных символов строки (относительно ее середины)')
    thirteen()
if nn == 14:
    print('Задание: Отсортировать строки в порядке увеличение квадратичного отклонения частоты встречаемости самого распространенного символа в наборе строк от частоты его встречаемости в данной строке.')
    fourteen()
if nn == 15:
    print('Задание: Дан целочисленный массив, в котором лишь один элемент отличается от остальных. Необходимо найти значение этого элемента.')
    fiftheen()
if nn == 16:
    print('Задание: Дан целочисленный массив. Необходимо найти два наименьших элемента.')
    sixtheen()
if nn == 17:
    print('Задание: Дано вещественное число R и массив вещественных чисел. Найти элемент массива, который наиболее близок к данному числу')
    r = float(input("Введите вещественное число: "))
    arr = []
    n = int(input("Введите количество элементов массива: "))
    for i in range(n):
        s = float(input("Введите вещественный элемент массива: "))
        arr.append(s)
    seventheen(r,arr)
if nn == 18:
    print('Для введенного списка положительных чисел построить список всех положительных делителей элементов списка без повторений')
    eighteen()
if nn == 19:
    print('Дан список. Построить новый список из квадратов неотрицательных чисел, меньших 100 и встречающихся в массиве больше 2 раз.')
    ninetheen()
