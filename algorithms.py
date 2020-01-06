
def twh_conversion(tWh):
    formula = tWh * 614175.1627564
    answer = str(formula)
    return answer


def average(List):
    base = 0
    for item in List:
        base += item
    values = len(List)
    avg = base/values
    return avg


def standard_deviation(List):

    from math import sqrt
    u = average(List)
    top = 0

    for x in List:
        top = abs(x - u)**2
    bottom = top/len(List)
    answer = round(sqrt(bottom), 3)

    return answer


def change_finder(testedList, interactive=False):

    changes = []

    for item1, item2 in zip(testedList, testedList[1:]):
        if item1 > item2:
            range_result = '-' + str(item1 - item2)
            if interactive:
                print('Change: ' + range_result)
            changes.append(range_result)
        elif item1 < item2:
            range_result = '+' + str(item2 - item1)
            if interactive:
                print('Change: ' + range_result)
            changes.append(range_result)
        elif item1 == item2:
            range_result = '0'
            if interactive:
                print('Change: None')
            changes.append(range_result)

    return changes


def change_to_int(List):

    processed_list = []

    for item in List:
        if '-' in item:
            int_change = item.replace('-', '')
            processed_list.append(int(int_change))
        elif '+' in item:
            int_change = item.replace('+', '')
            processed_list.append(int(int_change))

    return processed_list


def outliers(List, interactive=False):

    outlier_list_loc = []
    returned_outliers = []

    int_list = change_to_int(List)
    list_average = average(int_list)
    sd = standard_deviation(List)

    for item in int_list:
        if item > list_average*sd or item < list_average*sd*-1:
            outlier_list_loc.append(int_list.index(item))
            pass
        else:
            pass

    if interactive:
        print('\n** RESULTS **')
    for item in outlier_list_loc:
        loc = item+1
        if interactive:
            try:
                print('** OUTLIER FOUND: ' + str(List[loc]))
            except IndexError:
                pass
        try:
            returned_outliers.append(str(List[loc]))
        except IndexError:
            pass

    return returned_outliers


def dict_to_graph(dictionary, title):

    # METHOD IMPORT
    import matplotlib.pyplot as mpl

    graph_titles = []
    graph_values = []

    for key, value in dictionary.items():
        graph_titles.append(key)
        graph_values.append(value)

    x_graph_title, x_value, y_graph_title, y_value = graph_titles[0], graph_values[0], graph_titles[1], graph_values[1]

    mpl.plot(x_value, y_value)
    mpl.title(title, fontsize=15)
    mpl.xlabel(x_graph_title, fontsize=10)
    mpl.ylabel(y_graph_title, fontsize=10)
    mpl.tick_params('both', labelsize=7)

    mpl.show()
