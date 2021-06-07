from collections import Counter


def find_uniq(arr):
    for key, value in Counter(arr).items():
        if value == 1:
            return key


# return Counter(a).most_common()[-1][0]

print(find_uniq([0, 1, 1, 1, 1]))
