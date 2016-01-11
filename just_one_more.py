import re


def increment(values):
    new_values = []
    for item in values:
        if type(item) is int:
            item += 1
            new_values.append(item)
        elif type(item) is str and item.isalpha():
            continue
        elif type(item) is str:
            try:
                item = int(item) + 1
                new_values.append(item)
            except ValueError:
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
