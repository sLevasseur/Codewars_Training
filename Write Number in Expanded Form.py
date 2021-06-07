# input as a string, then as a list, for each number
# get len(list)
# use base 10 to add zero
# in a loop use len(list) as a starting point then decrease to 1
# in each loop, enter the number * base10(i) in a list
# if number == 0 pass
# " + ".join(list)

def expanded_form(num):
    num_to_list = list(str(num))
    final_list = list()
    for number, base10, in zip(num_to_list, [x for x in range(len(num_to_list), 0, -1)]):
        final_list.append(str(10 ** int(base10 - 1) * int(number))) if number != "0" else "continue"

    return " + ".join(final_list)


print(expanded_form(70304))
