def steps(number, n = 0):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    elif number == 1:
        return n
    else:
        n += 1
        if number % 2 == 0:
            return steps(number // 2, n)
        else:
            return steps(number * 3 + 1, n)
