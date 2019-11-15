tab = [0, 0, 0, 3, 4, 1, 2, 9]

def list_to_int(table):
    result = 0
    lenght = len(table)
    for position, element in enumerate(table, 1):
        result += element*(10**(lenght-position))
    return result

to_print = list()
to_print.append(list_to_int(tab))
print(to_print)
