tab = [0, 0, 0, 3, 4, 1, 2, 9]


def list_to_int(table):
    result = 0
    lenght = len(table)
    for position, element in enumerate(table, 1):
        result += element*(10**(lenght-position))
    return result


def add_digit(table, digit):
    result = [0 for x in range(len(table))]
    for i in range(len(table) - 1, -1, -1):
        tmp_sum = table[i] + digit
        if tmp_sum >= 10:
            digit = 1
        else:
            digit = 0
        result[i] = tmp_sum % 10
    if digit:
        result.insert(0, digit)
    return result


to_print = list()
to_print.append(list_to_int(tab))
to_print.append(add_digit(tab, 9))
print(to_print)
