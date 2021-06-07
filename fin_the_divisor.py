number = 13


def divisor(integer):
    answer = list()
    for test_number in range(2, integer):
        if integer % test_number == 0:
            answer.append(test_number)

    return answer if len(answer) >= 1 else f"{integer} is prime"


print(divisor(number))
