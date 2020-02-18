# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    result = 0
    values = []
    for index, price in enumerate(prices):
        values.append((price/weights[index], index))

    values_sorted = sorted(values, key=lambda v: v[0], reverse=True)

    for value in values_sorted:
        if capacity == 0:
            return result
        value_price, index = value
        weight = weights[index]
        a = min(weight, capacity)
        result += a * value_price
        capacity -= a

    return result


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
