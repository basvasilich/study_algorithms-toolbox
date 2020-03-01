# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    operations = [1, 2, 3]
    amounts = [0] * (n + 1)
    mid = [n]

    for i in range(2, n + 1):
        amounts[i] = float("inf")
        for operation in operations:
            if operation == 1 and i >= 1:
                num_operations = amounts[i - 1] + 1
                if num_operations < amounts[i]:
                    amounts[i] = num_operations
            if operation > 1 and i % operation == 0:
                num_operations = amounts[int(i / operation)] + 1
                if num_operations < amounts[i]:
                    amounts[i] = num_operations

    for j in range(amounts[n], 0, -1):
        if n % 3 == 0 and amounts[int(n / 3)] == j - 1:
            mid.append(int(n / 3))
            n = int(n / 3)
        elif n % 2 == 0 and amounts[int(n / 2)] == j - 1:
            mid.append(int(n / 2))
            n = int(n / 2)
        elif n - 1 >= 0 and amounts[int(n - 1)] == j - 1:
            mid.append(n - 1)
            n -= 1
    mid.reverse()
    return mid


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
