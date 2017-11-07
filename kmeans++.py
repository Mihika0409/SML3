import random
import operator
import sys


def calc_kpp_clusters(i, rows):
    while len(rows) < i:
        dist_dict = {}
        for j in range(len(a)):
            if j in rows:
                pass
            else:
                min_dist = sys.float_info.max
                for k in range(len(rows)):
                    dist = 0
                    for l in range(len(a[j])):
                        dist += (a[j][l] - a[rows[k]][l])**2
                    if min_dist > dist:
                        min_dist = dist
                    dist_dict[j] = min_dist
        next_cluster_index = max(dist_dict.iteritems(), key=operator.itemgetter(1))[0]
        rows.append(next_cluster_index)
    print rows


def initialize_kpp_clusters():
    for i in range(2, 5):
        rows = [random.randint(0, len(a))]
        calc_kpp_clusters(i, rows)


a = [[1, 1], [1, 2], [2, 1], [2, 2], [1, -1], [1, -2], [2, -1], [2, -2], [-1, 1], [-1, 2], [-2, 1], [-2, 2], [-1, -1], [-1, -2], [-2, -1], [-2, -2]]
initialize_kpp_clusters()
