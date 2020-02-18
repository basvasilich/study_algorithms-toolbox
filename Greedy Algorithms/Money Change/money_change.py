# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3

    result = 0
    coins = [10, 5, 1]

    for coin in coins:
        c = money // coin
        result += c
        money -= c * coin

    return result


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
