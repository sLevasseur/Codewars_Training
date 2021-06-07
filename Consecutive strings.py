def longest_consec(strarr, k):
    if len(strarr) == 0 or k < 0 or k > len(strarr):
        return ""
    final_string = list()
    temp_string = list()
    for i in range(k, len(strarr)+1):
        del temp_string[:]
        for y in range(i - k, i):
            temp_string.append(strarr[y])
        if len("".join(temp_string)) > len("".join(final_string)):
            final_string = temp_string.copy()

    return "".join(final_string)

print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
