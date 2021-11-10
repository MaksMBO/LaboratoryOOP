import sys
from string import ascii_letters


def recursion_check(list_num, operation_signs, ind):
    long = len(list_num)
    if ind == long - 1 and not list_num[ind].isalpha():
        return True
    elif list_num[ind].isdecimal():
        return recursion_check(list_num, operation_signs, ind + 1)
    elif operation_signs.count(list_num[ind]) == 1:
        if ind <= long - 1 and operation_signs.count(list_num[ind + 1]) == 1:
            return False
        elif operation_signs.count(list_num[long - 1]) == 1:
            return False
        elif list_num[ind] == operation_signs[2]:
            return False
        else:
            return recursion_check(list_num, operation_signs, ind + 1)

    return False


argument = sys.argv[1:]
indicator = 0
symbol = ('+', '-', '=')

num_list = []
line = ''
if argument:
    for char in argument[0]:
        if char.isdigit() or char in ascii_letters:
            line += char
        else:
            if line != '':
                num_list.append(line)
                line = ''
            if symbol.count(char):
                num_list.append(char)
    if line != '':
        num_list.append(line)
else:
    num_list.append("None")

if recursion_check(num_list, symbol, indicator):
    print(f"({recursion_check(num_list, symbol, indicator)}, {eval(''.join(argument))})")
else:
    print(f"({recursion_check(num_list, symbol, indicator)}, {None})")
