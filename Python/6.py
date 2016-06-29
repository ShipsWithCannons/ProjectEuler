def sums_and_squares():
    sum_of_squares, sums = 0, 0
    for i in xrange(1, 101):
        sum_of_squares += i**2
        sums += i
    return sums**2 - sum_of_squares

print sums_and_squares()
