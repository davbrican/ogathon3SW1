def sum_of_squares_of_digits(n):
    return sum(int(d)**2 for d in str(n))

def ends_in_89(n, memo):
    original = n
    sequence = []
    while n != 1 and n != 89:
        if n in memo:
            n = memo[n]
            break
        sequence.append(n)
        n = sum_of_squares_of_digits(n)

    result = 89 if n == 89 else 1
    for num in sequence:
        memo[num] = result
    memo[original] = result
    return result == 89

def count_up_to_89(limit):
    memo = {}
    counter = 0
    for i in range(1, limit + 1):
        if ends_in_89(i, memo):
            counter += 1
    return counter
