test = "aA11"


def duplicate_count(text):
    run = list(text.lower())
    x = 0
    list_temp = list()
    for letter in run:
        if letter not in list_temp:
            count = run.count(letter)
            if count > 1:
                x += 1
                list_temp.append(letter)
        else:
            continue
    return x


print(duplicate_count(test))
