import math

# Step 1: Read input file and extract number of cities (n)
with open('C:/Users/user1/Desktop/192803004_ASEM_ALSALAHI/tsp_11849_1.txt', 'r') as f:
    n = int(f.readline())

   
    # Step 2: Create list of city coordinates
    coords = []
    for i in range(n):
        line = f.readline().split()
        coords.append((float(line[0]), float(line[1])))

# Step 3: Compute distance matrix
dist = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(i+1, n):
        d = math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
        dist[i][j] = dist[j][i] = d

# Step 4: Find minimum spanning tree using Prim's algorithm
path = [0] # Start at city 0
visited = [False] * n
visited[0] = True
while len(path) < n:
    min_dist = float('inf')
    min_index = -1
    for i in range(n):
        if not visited[i] and dist[path[-1]][i] < min_dist:
            min_dist = dist[path[-1]][i]
            min_index = i
    path.append(min_index)
    visited[min_index] = True

# Step 5: Compute length of tour
tour_length = 0
for i in range(n):
    tour_length += dist[path[i-1]][path[i]]

# Step 6: Add distance from last city to first city and print tour length and path
tour_length += dist[path[-1]][0]
path.append(0)
print("Optimal maliye değeri:", tour_length)
print("Optimal çözüm için sırası ile gidilecek nodelar (şehirler):", path)