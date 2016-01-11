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
        # Items are strings, either letters or numbers
        elif type(item) is str and item.isalpha():
            continue
        elif type(item) is str and re.match(r'^-\d+$', item):
            item = int(item) + 1
            new_values.append(item)
        elif type(item) is str and item.isdigit():
            item = int(item) + 1
            new_values.append(item)
        # Level 3
        # Item is a string containing both letters and digits
        else:
            for entry in re.findall(r'(\D+)(\d+)(\D+)?(\d+)?', item):
                elements = [x for x in entry if x is not '']

                # Increment number strings in list by 1
                for index, new_item in enumerate(elements):
                    if new_item.isdigit():
                        if re.match(r'[0]\d', new_item):
                            new_item = int(new_item) + 1
                            new_item = '0' + str(new_item)
                            elements[index] = new_item
                        else:
                            new_item = int(new_item) + 1
                            elements[index] = str(new_item)

                new_values.append(''.join(elements))

    return new_values
