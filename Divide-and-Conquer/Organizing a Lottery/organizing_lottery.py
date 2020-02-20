# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    count = [None] * len(points)
    events = []
    rs = {}

    for i in range(len(starts)):
        events.append([starts[i], i, 'l'])
        events.append([ends[i], i, 'r'])
        rs[ends[i]] = rs[ends[i]] + 1 if ends[i] in rs.keys() else 1

    for i in range(len(points)):
        events.append([points[i], i, 'p'])

    events = sorted(events, key=lambda item: item[0])
    segments = 0
    for i, e in enumerate(events):
        value, index, event_type = e

        if event_type == 'l':
            segments += 1
        elif event_type == 'r':
            segments -= 1
        elif event_type == 'p':
            count[index] = segments

            if value in rs.keys():
                count[index] += rs[value]
        else:
            assert False

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
