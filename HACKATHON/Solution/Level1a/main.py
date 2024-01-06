import json
###data loading###
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

order_quantity = []
for j in range(len(data['neighbourhoods'])):
    node = "n"+str(j)
    order_quantity.append(data['neighbourhoods'][node]['order_quantity'])
capacity = 600
print(order_quantity)
###data loading###
def knapsack(weights, values, capacity, n):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] > dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items = selected_items[::-1]
    return dp[n][capacity], selected_items

[70, 70, 90, 50, 70, 90, 110, 70, 110, 70, 70, 110, 110, 90, 50, 90, 110, 90, 70, 110]