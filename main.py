"""
Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

my_file = open("task1.txt", "w")
line = input("Введите текст: \n")
while line:
    my_file.writelines("{}{}" .format(line, "\n"))
    line = input("Введите текст: \n")
    if not line:
        break

my_file.close()

"""
Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

my_file = open("task2.txt", "r")
count_lines = my_file.readlines()
my_file.close()
count_words = 0
print(f"Количество строк в файле: {len(count_lines)}")
for i in range(len(count_lines)):
    print(f"Количество слов в каждой строке: {len(count_lines[i].split(' '))}")
    count_words = count_words + len(count_lines[i].split(' '))
print(f"Всего слов в файле: {count_words}")

"""
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
"""

with open("task3.txt", "r") as my_file:
    finance = []
    users = []
    my_list = my_file.read().split("\n")
    for row_list in my_list:
        row_list = row_list.split(" ")
        if float(row_list[1]) < 20000:
            users.append(row_list[0])
        finance.append(row_list[1])
print(f"Оклад меньше 20.000 у след. сотрудников: {users},\nСредний оклад: {sum(map(float, finance)) / len(finance)}")

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские
числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_file = []
with open("task4_input.txt", "r") as my_file:
    for row_list in my_file:
        row_list = row_list.split(" ")
        new_file.append(row_list[0] + " — " + rus[row_list[0]] + "\n")
    print(new_file)

with open("task4_output.txt", "w") as my_file:
    my_file.writelines(new_file)

"""
Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""

def def_task_five():
    try:
        with open("task5.txt", "w+") as my_file:
            line = input("Введите набор чисел через проблем: \n")
            my_file.writelines(line)
            my_list_numbers = line.split(" ")
            print(sum(map(float, my_list_numbers)))
    except IOError:
        print("Error!")
    except ValueError:
        print("Error!")


def_task_five()

"""
Необходимо создать (не программно) текстовый файл, где
каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их
количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:
100(л)   50(пр)   20(лаб).
Физика:   30(л)   —   10(лаб)
Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40,
“Физкультура”: 30}
"""

subj = {}
with open("task6.txt", "r") as my_file:
    for row_file in my_file:
        subject, lecture, practice, lab = row_file.split(",")
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предметам:\n{subj}')

"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой
компании, а также среднюю прибыль. Если фирма получила убытки,
в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь
с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий
файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
{"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0

with open("task7.txt", "r") as my_file:
    for row_file in my_file:
        name, firm, earning, damage = row_file.split(",")
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f"Средняя прибыль: {prof_aver:.2f}")
    else:
        print(f"Средняя прибыль отсутствует (убытки)")
    pr = {"Средняя прибыль": round(prof_aver)}
    profit.update(pr)
    print(f"Прибыль каждой компании: {profit}")

with open('task7.json', 'w') as my_file:
    json.dump(profit, my_file)
    js_str = json.dumps(profit)
    print(f"JSON:\n{js_str}")
