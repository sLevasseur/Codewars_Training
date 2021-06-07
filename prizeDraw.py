import string
from collections import Counter

abc_value = dict()
for number, letter in zip(range(1, 27), string.ascii_lowercase):
    abc_value.__setitem__(letter, number)


def rank(st, we, n):
    if st == "":
        return "No participants."
    ranks = dict()
    st_as_list = st.lower().split(',')
    if n > len(st_as_list):
        return "Not enough participants."
    list_of_firstname_value = list()
    count_we = 0
    for firstname in st_as_list:
        som = 0
        for letter in firstname:
            som += abc_value.get(letter)
        ranks.__setitem__(firstname, (som + len(firstname)) * we[count_we])
        list_of_firstname_value.append((som + len(firstname)) * we[count_we])
        count_we += 1
    counter_duplicate = dict(Counter(ranks.values()))
    inv_counter_duplicate = {v: k for k, v in counter_duplicate.items()}
    duplicate = inv_counter_duplicate.get(2)
    list_of_duplicate_to_sort = list()
    if duplicate is not None:
        for items in ranks.items():
            if items[1] == duplicate:
                list_of_duplicate_to_sort.append(items[0])
    print(sorted(list_of_duplicate_to_sort))
    
    inv_map = {v: k for k, v in ranks.items()}



    winner = (sorted(list_of_firstname_value, reverse=True))[n-1]




    for name in st.split(','):
        if inv_map.get(winner) == name.lower():
            return name


print(rank("COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH", [1, 4, 4, 5, 2, 1], 4))
