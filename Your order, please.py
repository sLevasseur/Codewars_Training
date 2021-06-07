import re

def order(sentence):
    sentence_to_list = sentence.split(" ")
    ordered = dict()
    new_sentence = list()
    for word in sentence_to_list:
        number = int(str(re.findall("\d+", word)).replace("['", "").replace("']", ''))
        ordered.__setitem__(number, word)
    for i in range(1, len(ordered) + 1):
        new_sentence.append(ordered.get(i))

    return " ".join(new_sentence)

print(order("is2 Thi1s T4est 3a"))
