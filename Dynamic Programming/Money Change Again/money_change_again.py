# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    coins = [1, 3, 4]
    amounts = [0] * (money + 1)
    for i in range(1, money + 1):
        amounts[i] = float("inf")
        for coin in coins:
            if i >= coin:
                num_coins = amounts[i - coin] + 1
                if num_coins < amounts[i]:
                    amounts[i] = num_coins
    return amounts[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
