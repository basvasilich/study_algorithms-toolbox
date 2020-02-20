# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4

    def helper(start, end, q):

        if start == end and keys[start] == q:
            return start

        if start == end:
            return -1

        mid = (end - start) // 2 + start

        if start == mid and keys[start] == q:
            return start

        if end == mid and keys[end] == q:
            return end

        if keys[mid] >= q:
            return helper(start, mid, q)
        else:
            return helper(mid + 1, end, q)

    return helper(0, len(keys) - 1, query)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
