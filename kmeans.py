import scipy.io
import numpy as np
import sys
import random
import operator
import matplotlib.pyplot as plt


# step 1 - initialize random clusters
def initialize_cluster_centres():
    for k in range(2, 11):
        cluster_centre_index = np.random.randint(instances, size=k)
        cluster_centre_features_list = []
        for i in range(len(cluster_centre_index)):
            cluster_centre_features_list.append(list(matrix[cluster_centre_index[i]]))
        iterate_over_instances(cluster_centre_features_list)


# step 2 - iterate over all instances
def iterate_over_instances(cluster_centre_features_list):
    for i in range(instances):
        calculate_euclidean_distance(i, matrix[i], cluster_centre_features_list)
    assign_instances_to_clusters(cluster_centre_features_list)


# step 3 - calculate distance and assign to cluster
def calculate_euclidean_distance(instance_index, instance, cluster_centre_features_list):
    min_dist = sys.float_info.max
    for i in range(len(cluster_centre_features_list)):
        dist = np.linalg.norm(instance - cluster_centre_features_list[i])
        if min_dist > dist:
            min_dist = dist
            instance_cluster_index_dict[instance_index] = i


# step 4 - assign instances to clusters
def assign_instances_to_clusters(cluster_centre_features_list):
    cluster_list = [[] for x in range(len(cluster_centre_features_list))]
    for key, value in instance_cluster_index_dict.iteritems():
        cluster_list[value].append(key)
    reinitialize_cluster_centres(cluster_centre_features_list, cluster_list)


# step 5 - calculate new cluster centres, iterate till convergence
def reinitialize_cluster_centres(cluster_centre_features_list, cluster_list):
    new_cluster_centre_list = []
    for i in range(len(cluster_list)):
        new_cluster_features = [[] for x in range(features)]
        for j in range(len(cluster_list[i])):
            for k in range(len(matrix[cluster_list[i][j]])):
                new_cluster_features[k].append(matrix[cluster_list[i][j]][k])
        new_cluster_centre = []
        for j in range(len(new_cluster_features)):
            new_cluster_centre.append(np.mean(new_cluster_features[j]))
        new_cluster_centre_list.append(new_cluster_centre)
    if new_cluster_centre_list == cluster_centre_features_list:
        compute_objective_function(new_cluster_centre_list, cluster_list)
    else:
        iterate_over_instances(new_cluster_centre_list)


# step 6 - compute objective function
def compute_objective_function(cluster_centre_list, cluster_list):
    obj_function = 0
    for i in range(len(cluster_list)):
        for j in range(len(cluster_list[i])):
            dist = np.linalg.norm(matrix[cluster_list[i][j]] - cluster_centre_list[i])**2
            obj_function += dist
    print obj_function
    objective_function.append(obj_function)


# step 1a - k means++
def initialize_kpp_clusters():
    for i in range(2, 11):
        rows = [random.randint(0, instances)]
        rows = calc_kpp_clusters(i, rows)
        cluster_centre_features_list = []
        for j in range(len(rows)):
            cluster_centre_features_list.append(list(matrix[rows[j]]))
        iterate_over_instances(cluster_centre_features_list)


# step 1b - k means++
def calc_kpp_clusters(i, rows):
    while len(rows) < i:
        dist_dict = {}
        for j in range(instances):
            if j in rows:
                pass
            else:
                min_dist = sys.float_info.max
                for k in range(len(rows)):
                    dist = 0
                    for l in range(len(matrix[j])):
                        dist += (matrix[j][l] - matrix[rows[k]][l])**2
                    if min_dist > dist:
                        min_dist = dist
                    dist_dict[j] = min_dist
        next_cluster_index = max(dist_dict.iteritems(), key=operator.itemgetter(1))[0]
        rows.append(next_cluster_index)
    return rows


# load .mat file
mat = scipy.io.loadmat('kmeans_data.mat')

# declare variables
matrix = mat['data']
instances = len(matrix)
features = len(matrix[0])
instance_cluster_index_dict = {}

objective_function = []
initialize_cluster_centres()
print objective_function

'''objective_function = []
initialize_kpp_clusters()
print objective_function'''

num_of_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10]
plt.plot(num_of_clusters, objective_function)
plt.xlabel('Number of clusters')
plt.ylabel('Objective function')
plt.axis([0, 10, 0, 3000])
plt.show()