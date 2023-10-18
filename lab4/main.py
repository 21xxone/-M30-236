import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def r1(n, m, s):
    rand_list = []

    for i in range(n):
        rand_list.append(random.randint(m, s))
    return rand_list


# def r2(n, m, s):
#     res = random.sample(range(m, s), n)
#     return str(res)


# print(r2(10, 1, 6))


def r3(n, m, s):
    res = [random.randrange(m, s, 1) for i in range(n)]
    return str(res)


def r4(n, m, s):
    lis = []
    for _ in range(n):
        lis.append(random.randint(m, s))
    return (lis)


def r5(n, m, s):
    return (list(np.random.randint(low=m, high=s, size=n)))


def r6(n, s, m):
    return (np.random.random_sample(size=(n, s)))

# for i in range(10, 1000001):
#     n = i
#     m = 1
#     s = 6
#     print('знчения для', n)
#     print(r1(n, m, s), '  ',  r3(n, m, s), '  ', r4(n, m, s), '  ', r5(n, m, s), '  ', r6(n, m, s))
#     i = i * 10
#


def kubik(n: int) -> list:
    """

    :param n: Количество подбрасываний
    :return:  Список слкучайных подюрасываний кубика
    """
    data = []
    while len(data) < n:
        data.append(random.randint(1, 6))
    return data

def count_rate(kub_data: list):
    """
    Возвращает частоту выпадания значений кубика,
    согласно полученным данным
    :param kub_data: данные эксперимента
    :return:
    """
    kub_rate = {}
    for i in kub_data:
        if i in kub_rate:
            continue
        else:
            kub_rate[i] = kub_data.count(i)
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate

def sort_rate(counted_rate: dict):
    """
    Возвращает отсортированную частоту по ключу
    :param counted_rate: Наша неотсортированная частота
    :return:
    """
    sorted_rate = {}
    for key in sorted(counted_rate.keys()):
        sorted_rate[key] = counted_rate[key]
    return sorted_rate

def crate_dataframe(sorted_date: dict):
    """
    Создание и преобразование данных в Pandas dataframe
    :param sorted_date: dict
    :return: pd.Dataframe
    """
    df = pd.DataFrame(sorted_date, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))
    return df

def probability_solving(dataframe: pd.DataFrame):
    """
    Вычисление вероятности полученных результатов
    :param dataframe:
    :return:
    """
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability
    return dataframe

def graf(n, title, color):
    kub_data = kubik(n)
    kub_rate = count_rate(kub_data)
    sorted_rate = sort_rate(kub_rate)
    dataframe = crate_dataframe(sorted_rate)
    proba = probability_solving(dataframe)
    a4 = proba['Вероятность'].plot(kind='bar', legend=True, color=color)
    a4.figure.savefig(title)

graf(10, 'Вероятность10.png','green')
# graf(100, 'Вероятность100.png','blue')
# graf(10, 'Вероятность10.png','brown')
# graf(1000, 'Вероятность1000.png','pink')





# print(probability_solving(crate_dataframe(sort_rate(count_rate(kubik(10))))))
# data = probability_solving(crate_dataframe(sort_rate(count_rate(kubik(10)))))
# data['Вероятность'].plot(kind='bar', legend=True, color = 'pink')
 # a = proba['Вероятность'].plot(kind='bar', legend=True, color = 'pink')
# data.figure.savefig('Вероятность10.png')
#
#
# n = 10
# kub_data = kubik(n)
# kub_rate = count_rate(kub_data)
# sorted_rate = sort_rate(kub_rate)
# dataframe = crate_dataframe(sorted_rate)
# proba = probability_solving(dataframe)
# a = proba['Вероятность'].plot(kind='bar', legend=True, color = 'pink')
# a.figure.savefig('Вероятность10.png')




# n = 100
# kub_data = kubik(n)
# kub_rate = count_rate(kub_data)
# sorted_rate = sort_rate(kub_rate)
# dataframe = crate_dataframe(sorted_rate)
# proba = probability_solving(dataframe)
# a1 = proba['Вероятность'].plot(kind='bar', legend=True, color = 'black')
# a1.figure.savefig('Вероятность100.png')
#
# n = 1000
# kub_data = kubik(n)
# kub_rate = count_rate(kub_data)
# sorted_rate = sort_rate(kub_rate)
# dataframe = crate_dataframe(sorted_rate)
# proba = probability_solving(dataframe)
# a2 = proba['Вероятность'].plot(kind='bar', legend=True, color = 'green')
# a2.figure.savefig('Вероятность1000.png')
#
# n = 10000
# kub_data = kubik(n)
# kub_rate = count_rate(kub_data)
# sorted_rate = sort_rate(kub_rate)
# dataframe = crate_dataframe(sorted_rate)
# proba = probability_solving(dataframe)
# a3 = proba['Вероятность'].plot(kind='bar', legend=True, color = 'brown')
# a3.figure.savefig('Вероятность10000.png')
#
# n = 1000000
# kub_data = kubik(n)
# kub_rate = count_rate(kub_data)
# sorted_rate = sort_rate(kub_rate)
# dataframe = crate_dataframe(sorted_rate)
# proba = probability_solving(dataframe)
# a4 = proba['Вероятность'].plot(kind='bar', legend=True)
# a4.figure.savefig('Вероятность1000000.png')

