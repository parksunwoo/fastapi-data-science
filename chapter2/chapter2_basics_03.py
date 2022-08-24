def euclidean_division(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return (quotient, remainder)

q, r = euclidean_division(3, 2)
print(q)
print(r)
