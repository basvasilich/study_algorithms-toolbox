# python3
import math


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 100

    if n == 0:
        return 0

    v1, v2, v3 = 1, 1, 0  # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':    v1, v2, v3 = v1 + v2, v1, v2
    return v2


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
