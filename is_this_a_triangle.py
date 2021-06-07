def is_triangle(a, b, c):
    return True if a + b > c and a + c > b and b + c > a else False


print(is_triangle(1, 2, 2))
