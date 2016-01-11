import re


def increment(values):
    new_values = []
    for item in values:
        # Level 1
        # All items in the list are int
        if type(item) is int:
            item += 1
            new_values.append(item)
        # Level 2
        # Item is only letters, skip them
        elif type(item) is str and item.isalpha():
            continue
        # Item is a string containing negative value
        elif type(item) is str and re.match(r'^-\d+$', item):
            item = int(item) + 1
            new_values.append(item)
        # Item is a string containing digit
        elif type(item) is str and item.isdigit():
            item = int(item) + 1
            new_values.append(item)
        # Level 3
        # Item is a string containing both letters and digits
        else:
            elements = re.split(r'(\D+)(\d+)(\D+)?(\d+)?', item)
            new_item = ''
            for entry in elements:
                if entry is None:
                    continue
                elif entry == '':
                    continue
                else:
                    if entry.isdigit():
                        if re.match(r'[0]\d', entry):
                            entry = int(entry) + 1
                            new_item += '0' + str(entry)
                        else:
                            entry = int(entry) + 1
                            new_item += str(entry)
                    else:
                        new_item += entry
            new_values.append(new_item)

    return new_values
