import VK.data_handler as dh
import matplotlib.pyplot as plt
import numpy as np
from textwrap import wrap


def main():
    plt.style.use('ggplot')

    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 
                'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    queries = ['Навальный', 'Путин']
    dataset = [{}, {}]

    s = "01-{}-201{}"
    for j, query in enumerate(queries):
        for i, month in enumerate(months, 1):
            m = str(i)
            if len(m)==1:
                m = '0'+m
            left = s.format(m, '8')
            m = str((i)%12+1)
            if len(m)==1:
                m = '0'+m
            right = s.format(m, 8+(i+1)//13)
            dataset[j][month] = dh.total_count(query, left, right)

    values = [np.array(list(data.values())) for data in dataset]

    # Результат по запросу
    fig = plt.figure("Активность")
    ax = plt.axes()

    ax.bar(dataset[0].keys(), values[0], width=-0.8, align='edge')

    ax.set_title('Результат по запросу: "{}" (2018 год)'.format(queries[0]))
    ax.set_ylabel('Количество постов в месяц')
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    fig.subplots_adjust(left=0.2)

    # Сравнение
    fig = plt.figure("Сравнение активности")
    ax = plt.axes()

    ax.bar(dataset[0].keys(), values[0], width=0.5, align='edge', label = queries[0])
    ax.bar(dataset[1].keys(), values[1], width=-0.5, align='edge', color='mediumaquamarine', 
                                                                label = queries[1])

    title = ax.set_title("\n".join(wrap('Сравнение результата по запросу: "{}"'
                            ' и "{}" (2018 год)'.format(queries[0], queries[1]),40)))
    title.set_y(1.05)
    fig.subplots_adjust(top=0.8, left=0.2)
    ax.set_ylabel('Количество постов в месяц')
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.legend()

    plt.show()


if __name__=='__main__':
    main()