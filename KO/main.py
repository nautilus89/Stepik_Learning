import csv
import re
from datetime import datetime
import matplotlib.pyplot as plt


def make_a_dict():
    # ДАТА - ЦЕНА - ОТКР - МАКС - МИН - ОБЪЕМ - ИЗМ
    # основной словарь
    dict_full = []
    # открываем файл
    with open("KO_1.csv") as file:
        file_reader = csv.reader(file, delimiter=";")
        # бежим по строкам
        for row in file_reader:
            # словарь для каждой строки
            dict_row = []
            # ищем дату по шаблону
            item_date = re.findall(r'[0-9.]{10}', row[0])
            if item_date:
                weekday = datetime(int(item_date[0][6:]), int(item_date[0][3:5]), int(item_date[0][:2])).weekday()
                dict_row.append(item_date[0])
                # выбираем остальные значения
                text = re.findall(r'(\d+),(\d+)', row[0])
                for item in text:
                    if re.findall(r'-(\d+),(\d+)', row[0]):
                        float_item = (float(item[0]) + float(item[1]) / 100)*(-1)
                    else:
                        float_item = float(item[0])+float(item[1])/100
                    dict_row.append(float_item)
                for c in (1, 2, 3, 4, 5):
                    if dict_row[c] < 0:
                        dict_row[c] = float(dict_row[c]*(-1))
                dict_row.append(weekday)
                dict_full.append(dict_row)
    calculate(dict_full)
    middle_line(dict_full)


def calculate(dict_calc):
    # ДАТА - ЦЕНА - ОТКР - МАКС - МИН - ОБЪЕМ - ИЗМ
    current_id = len(dict_calc)-1
    # последняя цена
    current_price = dict_calc[-1][1]
    # последнее изменение цены в %
    current_change = dict_calc[-1][6]

    # максимальное число похожих дней
    days_equals = 0
    max_days_equals = 0
    item_max_equals = 0

    # среднее изменение цены
    mid_change = 0.0
    for item in dict_calc:
        mid_change += float(item[6])
    mid_change = mid_change/len(dict_calc)

    print('Текущий день:', dict_calc[-1][0], 'Последняя цена:', current_price, 'Последнее изменение:', current_change)
    # идем по словарю, запоминаем номера строк
    for item_id, prev_items in enumerate(dict_calc):
        if (abs(prev_items[6] - current_change) < mid_change) and (current_id != item_id):
            days_equals = 0
            for day in range(1, 30):
                prev_day = current_id-day
                item_day = item_id-day
                if prev_day < current_id:
                    if (abs(dict_calc[prev_day][6]-dict_calc[item_day][6])) < mid_change:
                        days_equals += 1
                        if days_equals > max_days_equals:
                            item_max_equals = item_id
    print('Похожий день:', dict_calc[item_max_equals][0], 'Изменение цены в этот день:', dict_calc[item_max_equals][6])
    print('Количество похожих дней до этого:', days_equals)
    if item_max_equals < current_id:
        future_change = dict_calc[item_max_equals+1][6]
        future_price = current_price + (current_price * (future_change/100))
        print('Прогноз на завтра:', future_change, 'Цена:', future_price)


#def trend(dict_trend):
    # ДАТА - ЦЕНА - ОТКР - МАКС - МИН - ОБЪЕМ - ИЗМ
    #for item in dict_trend:

#нужно учитывать интервал, неделю/месяц/квартал/полугодие

def middle_line(dict_orig):
    dict_middle = []
    for item_id, row in enumerate(dict_orig):
        if item_id > 0:
            mid = (dict_orig[item_id][1] + dict_orig[item_id-1][1])/2
        else:
            mid = 0
        dict_middle.append(mid)
    print(dict_middle)


make_a_dict()
