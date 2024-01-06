import json
import numpy as np
capacity = 600
weight = 0
weights = [0, 70, 70, 90, 50, 70, 90, 110, 70, 110, 70, 70, 110, 110, 90, 50, 90, 110, 90, 70, 110]
###Travelling SalesMen Problem###
def travellingsalesman(c):
    global cost
    global path
    global weights
    global weight 
    global capacity
    adj_vertex = 999999
    min_val = 999999
    visited[c] = 1
    path.append(c)
    weight = weight + weights[c]
    print(c, end=" ")
    print(weight,capacity)
    if weight < capacity:
        for k in range(n):
            if (tsp_g[c][k] != 0) and (visited[k] == 0):
                if tsp_g[c][k] < min_val:
                    min_val = tsp_g[c][k]
                    adj_vertex = k
        if min_val != 999999:
            cost = cost + min_val
        if adj_vertex == 999999:
            adj_vertex = 0
            path.append(adj_vertex)
            weight = weight + weights[adj_vertex]
            print(adj_vertex, end=" ")
            cost = cost + tsp_g[c][adj_vertex]
            return
        travellingsalesman(adj_vertex)
    else:
        print(11111111111111)
        print(weight,path)

###Travelling SalesMen Problem###

###Loading Data###
f = open('data.json')
data = json.load(f)
rest = data["restaurants"]["r0"]["neighbourhood_distance"]
dist_matrix = []
for j in range(len(data['neighbourhoods'])):
    node = "n"+str(j)
    dist_s = []
    for i in data['neighbourhoods'][node]['distances']:
        dist = i
        dist_s.append(dist)
    dist_matrix.append(dist_s)
for index in range(len(dist_matrix)):
    dist_matrix[index] = [rest[index]] + dist_matrix[index]
    index = index + 1
rest.insert(0,0)
rest = [rest]
for i in dist_matrix:
    rest.append(i)
f.close()
###Loading Data###

###Finding Shortest path###
n = len(rest)
cost = 0
path = []
visited = np.zeros(n, dtype=int)
tsp_g = np.array(rest)
travellingsalesman(0)
###Finding Shortest path###
print(path)


