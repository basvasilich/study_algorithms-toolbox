# python3


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}

    def make_array(s):
        arr_ops = {}
        arr_digits = {}
        for i, val in enumerate(s):
            if i == 0:
                arr_digits[len(arr_digits) + 1] = int(val)
            elif i % 2 == 1:
                arr_ops[len(arr_ops) + 1] = val
            else:
                arr_digits[len(arr_digits) + 1] = int(val)

        return arr_ops, arr_digits

    op, digits = make_array(dataset)

    n = len(digits)

    if n == 1:
        return int(digits[1])
    elif n == 2:
        return ops[op[1]](digits[1], digits[2])

    max_arr = {}
    min_arr = {}

    def min_max(i, j):
        min_value = float("inf")
        max_value = -1 * float("inf")

        for k in range(i, j):
            a = ops[op[k]](max_arr[i, k], max_arr[k + 1, j])
            b = ops[op[k]](max_arr[i, k], min_arr[k + 1, j])
            c = ops[op[k]](min_arr[i, k], max_arr[k + 1, j])
            d = ops[op[k]](min_arr[i, k], min_arr[k + 1, j])

            min_value = min(min_value, a, b, c, d)
            max_value = max(max_value, a, b, c, d)

        return min_value, max_value

    for i in range(1, n + 1):
        min_arr[i, i] = digits[i]
        max_arr[i, i] = digits[i]

    for s in range(1, n):
        for i in range(1, n - s + 1):
            j = i + s
            min_arr[i, j], max_arr[i, j] = min_max(i, j)

    return max(max_arr[1, n], min_arr[1, n])


if __name__ == "__main__":
    print(find_maximum_value(input()))
