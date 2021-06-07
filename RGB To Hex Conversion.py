def rgb(r, g, b):
    # your code here :)
    hex_converter_letter = {15: "F", 14: "E", 13: "D", 12: "C", 11: "B", 10: "A"}
    decimals_to_convert = [r, g, b]
    string_return = ""

    for decimal in decimals_to_convert:
        try:
            if 0 < decimal < 256:
                pass
        except TypeError as e :
            string_return += "00"
        else:
            if decimal == 0:
                string_return += "00"
                continue
            if 0 < decimal < 256:
                r0 = (decimal / 16) % 1
                r1 = int(decimal / 16)
                if r1 > 9:
                    r1 = hex_converter_letter.get(r1)
                r2 = int(r0 * 16)
                if r2 > 9:
                    r2 = hex_converter_letter.get(r2)
                string_return += f'{r1}{r2}'
            else:
                if decimal < 0:
                    string_return += "00"
                else:
                    string_return += "FF"

    return string_return


"""r = (255 / 16) % 1
r0 = int(255 / 16)
print(r0)
print(r)
r1 = int(r * 16)
print(r1)
print(f'{r0}{r1}')"""

print(rgb(0, 0, 0))
