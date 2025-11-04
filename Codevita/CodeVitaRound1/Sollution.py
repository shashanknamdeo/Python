def polygon_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2


def polygon_perimeter(points):
    n = len(points)
    peri = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        peri += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return peri


def min_edge_length(points):
    n = len(points)
    return min(
        ((points[(i + 1) % n][0] - points[i][0]) ** 2 +
         (points[(i + 1) % n][1] - points[i][1]) ** 2) ** 0.5
        for i in range(n)
    )


def max_matchbox_volume(points):
    A0 = polygon_area(points)
    P = polygon_perimeter(points)

    # S = -4 (for rectilinear polygons)
    best = 0.0
    min_edge = min_edge_length(points)
    max_h = (min_edge / 2) - 0.05

    h = 0.1
    while h <= max_h + 1e-9:
        A = A0 - P * h + 4 * (h ** 2)
        if A <= 0:
            break
        V = A * h
        best = max(best, V)
        h = round(h + 0.1, 1)

    return best


# -------- MAIN ---------
# N = int(input().strip())
# points = [tuple(map(float, input().split())) for _ in range(N)]
# ans = max_matchbox_volume(points)
# print(f"{ans:.2f}")


points = [(0.0, 0.0), (8.0, 0.0), (8.0, 2.0), (5.0, 2.0), (5.0, 3.0), (3.0, 3.0), (3.0, 2.0), (0.0, 2.0)]

ans = max_matchbox_volume(points)
print(f"{ans:.2f}")

points = [(0.0, 0.0), (2.0, 0.0), (2.0, 2.0), (1.0, 2.0), (1.0, 1.0), (0.0, 1.0)]

ans = max_matchbox_volume(points)
print(f"{ans:.2f}")
