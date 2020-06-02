from math import sqrt

def euclidean_distance(point1, point2):
    return sqrt(pow(point2[0] - point1[0], 2) + pow(point2[1] - point1[1], 2))


def find_farthest_points(points):
    ret = [(0, 0), (0, 0)]
    dist = 0.0
    for i in range(len(points)):
        for x in points[(i + 1)::]:
            d = euclidean_distance(points[i], x)
            if (d > dist):
                dist = d
                ret[0] = points[i]
                ret[1] = x
    return ret


#Expect [(1, 1), (3, 3)]
print(find_farthest_points([(2, 2), (1, 1), (3, 3)]))
