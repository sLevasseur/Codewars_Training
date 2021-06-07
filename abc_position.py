# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def abc_position(text):
    import string
    import re
    alphabet_letter = list(string.ascii_lowercase)
    abc_dict = dict()
    pos = 1
    abc_number = list()

    for letter in alphabet_letter:
        abc_dict.__setitem__(letter, pos)
        pos += 1

    for letter in re.findall("[a-z]", text.lower()):
        abc_number.append(str(abc_dict.get(letter)))

    return " ".join(abc_number)


print(abc_position("The sunset sets at twelve o' clock."))
