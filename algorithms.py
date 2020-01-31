
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


def dict_to_graph(dictionary, title, x_title=None, y_title=None):

    # METHOD IMPORT
    import matplotlib.pyplot as mpl

    x_value, y_value = [], []

    if x_title is not None and y_title is not None:
        x_graph_title = x_title
        y_graph_title = y_title

        for year, data in dictionary.items():
            x_value.append(year)
            y_value.append(data)

    else:

        graph_titles, graph_values = [], []

        for key, value in dictionary.items():
            graph_titles.append(key)
            graph_values.append(value)

        x_graph_title, x_value = graph_titles[1], graph_values[1]
        y_graph_title, y_value = graph_titles[0], graph_values[0]

    try:
        for y in range(0, len(y_value)):
            y_value[y] = float(y_value[y])
    except TypeError:
        pass

    try:
        for x in range(0, len(x_value)):
            x_value[x] = float(x_value[x])
    except TypeError:
        pass

    mpl.plot(x_value, y_value)
    mpl.title(title, fontsize=15)
    mpl.xlabel(x_graph_title, fontsize=12)
    mpl.ylabel(y_graph_title, fontsize=12)
    mpl.tick_params('both', labelsize=10)
    mpl.ticklabel_format(useOffset=False, style='plain')

    mpl.show()


def dict_to_box_plot(input_dict, title, xtitle, ytitle):

    import matplotlib.pyplot as mpl

    data_x = []
    z = 0
    for x in range(0, len(input_dict.values())):
        z += 1
        data_x.append(z)

    data_x_label = []
    for x in input_dict.keys():
        data_x_label.append(int(x))

    data_y = []
    for x in input_dict.values():
        data_y.append(x)

    mpl.boxplot(data_y)
    mpl.title(title, fontsize=15)
    mpl.ylabel(ytitle, fontsize=10)
    mpl.xlabel(xtitle, fontsize=10)
    mpl.xticks(data_x, data_x_label, rotation='vertical')
    mpl.margins(0.2)
    mpl.subplots_adjust(bottom=0.15)
    mpl.show()


def datetime_fmt(pro_list):

    list_of_processed_years = []

    for item in pro_list:
        new_str = ''
        item = list(item)
        del item[4:]
        for x in item:
            new_str = new_str + x
            if len(new_str) == 4:
                list_of_processed_years.append(new_str)

    return list_of_processed_years


def yearly_amt(pro_list):

    from collections import Counter

    earth_year, earth_frq = [], []
    yearly_amount = {}

    counted = Counter(datetime_fmt(pro_list))
    for key, value in counted.items():
        earth_frq.append(value)
        earth_year.append(key)

    for item1, item2 in zip(earth_year, earth_frq):
        yearly_amount[item1] = [float(item2)]

    return yearly_amount


def yearly_sev(pro_list_date, pro_list_mag):

    dates = datetime_fmt(pro_list_date)
    mags = pro_list_mag
    yearly_severity = {}

    for date, mag in zip(dates, mags):
        if date in yearly_severity.keys():
            yearly_severity[date].append(float(mag))
        elif date not in yearly_severity.keys():
            yearly_severity[date] = [float(mag)]

    return yearly_severity


def list_half(pro_list):
    x = len(pro_list)
    y = x/2

    if y is float:
        round(y)
        y = int(y)

    return y
