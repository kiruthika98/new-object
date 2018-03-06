def odd_even_sieve(x):
    output = x[:]
    even_index, odd_index = 0, 1
    for value in x:
        if value % 2 == 0:
            output[even_index] = value
            even_index += 2
        else:
            output[odd_index] = value
            odd_index += 2
    return output
