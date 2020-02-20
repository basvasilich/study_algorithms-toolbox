# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    if len(elements) < 3:
        return 0

    def count_num(start, end, el):
        count = 0
        for i in range(start, end + 1):
            if elements[i] == el:
                count += 1

        return count

    def helper(start, end):
        if start == end:
            return elements[start]

        mid = (end - start) // 2 + start
        left = helper(start, mid)
        right = helper(mid + 1, end)

        if left == right:
            return left

        left_count = count_num(start, end, left)
        right_count = count_num(start, end, right)

        return left if left_count > right_count else right

    return 1 if count_num(0, len(elements) - 1, helper(0, len(elements) - 1)) > len(elements) / 2 else 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
