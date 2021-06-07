def to_camel_case(text):
    chars_to_replace = {"-": "", "_": ""}
    text_to_list = list(text)
    end_length = text.count('-') + text.count('_')
    for i in range(0, len(text)-end_length):
        if text_to_list[i] == '-' or text_to_list[i] == '_':
            char_to_upper = str(text_to_list.pop(i+1)).upper()
            text_to_list.insert(i+1, char_to_upper)
            del text_to_list[i]

    return "".join(text_to_list)

print(to_camel_case("The_pippi-is-cute"))
