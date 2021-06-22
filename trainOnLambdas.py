from functools import reduce

number = [10, 20, 30, 30, 15, 25, 35, 45]


def unique_sum(lst):
    return reduce((lambda x, y: x + y), set(lst)) if lst else None
    # return sum(set(lst)) if lst else None


print(unique_sum(number))
