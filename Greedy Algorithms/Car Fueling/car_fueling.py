# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    refillings = 0
    current_stop = 0

    stops.append(d)
    stops.insert(0, 0)

    while stops[current_stop] < d:
        last_stop = current_stop
        while current_stop < len(stops) - 1 and stops[current_stop + 1] - stops[last_stop] <= m:
            current_stop += 1
        if last_stop == current_stop:
            return -1
        if stops[current_stop] < d:
            refillings += 1

    return refillings


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
