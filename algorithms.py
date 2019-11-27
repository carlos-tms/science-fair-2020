
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


def range_patterns(testedList):

    changes = []

    for item1, item2 in zip(testedList, testedList[1:]):
        if item1 > item2:
            change = '-' + str(item1 - item2)
            print('Change: ' + change)
            changes.append(change)
        elif item1 < item2:
            change = '+' + str(item2-item1)
            print('Change: ' + change)
            changes.append(change)
        elif item1 == item2:
            change = '0'
            print('Change: None')
            changes.append(change)

