import re
from functools import partial


def increment_match(matchobj):
    value = matchobj.group(0)
    leading_zero = re.compile(r'[0]\d+')

    if re.match(leading_zero, value):
        return '0' + str(int(value) + 1)
    else:
        return str(int(value) + 1)


def increment(values):
    check_negative = partial(re.match, r'^-\d+$')
    find_digits = re.compile(r'\d+')

    new_values = []
    for item in values:
        # Level 1
        if type(item) is int:
            item += 1
        # Level 2
        elif type(item) is str:
            if item.isalpha():
                continue
            elif check_negative(item):
                item = int(item) + 1
            elif item.isdigit():
                item = int(item) + 1
        # Level 3
            else:
                item = re.sub(find_digits, increment_match, item)
        new_values.append(item)

    return new_values
