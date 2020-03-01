# python3


def edit_distance(first_string, second_string):
    d = [[0] * len(second_string) for _ in range(len(first_string))]

    if first_string[0] == second_string[0]:
        d[0][0] = 0
    else:
        d[0][0] = 1

    for j in range(1, len(second_string)):
        d[0][j] = j
        for i in range(1, len(first_string)):
            d[i][0] = i
            insertion = d[i][j - 1] + 1
            deletion = d[i - 1][j] + 1
            match = d[i - 1][j - 1]
            mismatch = d[i - 1][j - 1] + 1
            if first_string[i] == second_string[j]:
                d[i][j] = min(insertion, deletion, match)
            else:
                d[i][j] = min(insertion, deletion, mismatch)

    return d[len(first_string) - 1][len(second_string) - 1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
