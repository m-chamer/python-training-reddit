tab = [0, 0, 0, 3, 4, 1, 2, 9]


def list_to_int(table):
    result = 0
    lenght = len(table)
    for position, element in enumerate(table, 1):
        result += element*(10**(lenght-position))
    return result


def int_to_list(number):
    result = list()
    i = 10
    while(number):
        digit = number % i
        result.append(digit)
        number /= i
    return list(reversed(result))


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


def add_lists(table1, table2):
    table1.reverse()
    table2.reverse()
    if len(table1) > len(table2):
        shorter = table2
        longer = table1
    else:
        shorter = table1
        longer = table2
    for idx, element in enumerate(shorter):
        longer[idx] += element
        if longer[idx] >= 10:
            longer[idx] %= 10
            try:
                longer[idx+1] += 1
            except IndexError:
                longer.insert(idx+1, 1)
    return list(reversed(longer))



def add_number(table, number):
    return add_lists(table, int_to_list(number))


to_print = list()
to_print.append(list_to_int(tab))
to_print.append(add_digit(tab, 9))
to_print.append(int_to_list(123))
print(to_print)

