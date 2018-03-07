from collections import Counter


def order_by_occur_nums(iterable_obj):
    """
    对可迭代对象按照元素出现次数进行排序并去重
    如 ['Tom', 'Sim', 'Jack', 'Tom', 'Sleep', 'We', 'Tom', 'Tom', 'Sim', 'We', 'Tom']
       -->
       ['Tom', 'We', 'Sim', 'Sleep', 'Jack']
    :param iterable_obj: 可迭代对象
    :return: (list)  排序并去重后的list
    """

    # 如{'A': 3, 'C': 2, 'B':1}
    c = Counter(iterable_obj)

    # top_list = [('Tom', 5), ('We', 2), ('Sim', 2), ('Sleep', 1), ('Jack', 1)]
    top_list = c.most_common()

    # ['Tom', 'We', 'Sim', 'Sleep', 'Jack']
    return [i[0] for i in top_list]


# debug
if __name__ == '__main__':
    lst = ['Tom', 'Sim', 'Jack', 'Tom', 'Sleep', 'We', 'Tom', 'Tom', 'Sim', 'We', 'Tom']
    rv = order_by_occur_nums(lst)
