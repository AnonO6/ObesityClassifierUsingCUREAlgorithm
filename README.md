# CURE ALGORITHM

The CURE algorithm stands as a beacon of adaptability and precision in the vast sea of data clustering techniques. Its applications, from detecting the faintest outlier to grouping complex genomic sequences, underscore the algorithm's versatility and potency. The future of data analysis continues to brighten with the promise of CURE, illuminating patterns and clusters that were once veiled in the shadows of data complexity.

# CODE EXPLAINATION

1. getDistanceFromRepresentatives

Calculates the minimum distance from a given point to any of the representative points of a cluster.

```
def getDistanceFromRepresentatives(point, representativePoints_shifted): minimumDistance = float("inf") for repr_point in representativePoints_shifted: distance = getDistance(point, repr_point) if distance < minimumDistance: minimumDistance = distance return minimumDistance
```

Purpose: This function helps in assigning a point to the nearest cluster based on the shifted representative points.

2. computeCentroid

Computes the centroid (geometric center) of a cluster of points.

def computeCentroid(initialCluster): x = 0 y = 0 for point in initialCluster: x += point[0] y += point[1] numberOfPoints = len(initialCluster) return (x / numberOfPoints, y / numberOfPoints)

Purpose: To find the center of a cluster, which is used to shift representative points towards the centroid.

3. findRepresentativePoints

Selects n well-scattered representative points from a cluster.

    def findRepresentativePoints(initialCluster): representativePoints = [] representativePoints.append(list(initialCluster[0])) for i in range(n - 1): maximumDistance = float("-inf") for point in initialCluster: if point inrepresentativePoints: continue minimumDistance = float("inf") for representativePoint in representativePoints: distance = getDistance(point, representativePoint) if distance < minimumDistance: minimumDistance = distance if minimumDistance > maximumDistance: candidateRepresentativePoint = point maximumDistance = minimumDistance representativePoints.append(list(candidateRepresentativePoint)) returnrepresentativePoints

Purpose: To select a set of points that are representative of the cluster’s shape and spread.

4. getDistance

Calculates the Euclidean distance between two points.

    def getDistance(point1, point2): distance = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 return math.sqrt(distance)

Purpose: To measure the distance between two points, which is used in various parts of the clustering process.

5. clusterDistance

Calculates the minimum distance between any two points from two different clusters.

    def clusterDistance(cluster1, cluster2): minimumDistance = float("inf") for point1 incluster1: for point2 in cluster2: if minimumDistance > getDistance(point1, point2): minimumDistance = getDistance(point1, point2) return minimumDistance

Purpose: To determine the closeness of two clusters during hierarchical clustering.

6. formClusters_heirarchical

Performs hierarchical clustering on the sample data until the desired number of clusters k is achieved.

    def formClusters_heirarchical(sampleData): clusters = [[i] for i in sampleData] iters = len(sampleData) - k for iter in range(iters): min = float("inf") for i in range(0, len(clusters) - 1): for j in range(i + 1, len(clusters)): if min > clusterDistance(clusters[i], clusters[j]): min = clusterDistance(clusters[i], clusters[j]) c1 = i c2 = j clusters[c1].extend(clusters[c2]) del clusters[c2] returnclusters

Purpose: To reduce the initial dataset into k clusters using a hierarchical approach.

# Main Execution Flow

## Reading Input Data:

Reads sample and complete data files along with parameters for clustering.

    sampleDataFile = open(sys.argv[1]).readlines() completeDataFile = open(sys.argv[2]).readlines() k = int(sys.argv[3]) n = int(sys.argv[4]) p = float(sys.argv[5]) outputFileName = sys.argv[6]

## Parsing Data:

Converts the read data into lists of tuples representing points.

    completeData = [] for line in completeDataFile: line = line.split(",") completeData.append((float(line[0]), float(line[1]))) sampleData = [] for line insampleDataFile: line = line.split(",") sampleData.append((float(line[0]), float(line[1]))) sampleData = sorted(sampleData, key=lambda x: (x[0], x[1]))

## Hierarchical Clustering:

Forms initial clusters using hierarchical clustering on the sample data.

    initialClusters = formClusters_heirarchical(sampleData)

## Finding and Shifting Representative Points:

For each cluster, finds representative points and shifts them towards the centroid.

    representativePointsList = [] representativePoints_shifted = [] for initialCluster in initialClusters: representivePoints = findRepresentativePoints(initialCluster) representativePointsList.append(representivePoints) shiftedRepresentativePoints = [] centroid = computeCentroid(initialCluster) for representativePoint inrepresentivePoints: shiftX = (centroid[0] - representativePoint[0]) * p shiftY = (centroid[1] - representativePoint[1]) * p shiftedRepresentativePoints.append((representativePoint[0] + shiftX, representativePoint[1] + shiftY)) representativePoints_shifted.append(shiftedRepresentativePoints)

## Assigning Clusters:

Assigns each point in the complete dataset to the nearest cluster based on the representative points.

    outputPointList = [] for point in completeData: minimumDistance = float("inf") forclusterNum in range(k): distance = getDistanceFromRepresentatives(point, representativePoints_shifted[clusterNum]) if distance < minimumDistance: minimumDistance = distance clusterId = clusterNum outputPointList.append((point, clusterId))

## Writing Output:

Saves the clustering results to a specified output file.

    w = open(outputFileName, 'w') for point in outputPointList: w.write(str(point[0][0]) + "," + str(point[0][1]) + "," + str(point[1]) + "\n") w.close()

## Plotting the Results:

Uses matplotlib to create a scatter plot of the points colored by their assigned cluster.

    colors = plt.cm.get_cmap("tab10", k) for point, clusterId in outputPointList: plt.scatter(point[0], point[1], color=colors(clusterId)) plt.xlabel('X') plt.ylabel('Y') plt.title('CURE Clustering Result') plt.show()

# Overview of the CURE Algorithm Implementation

**Sampling:** Initially, a sample of the data is used to create clusters.
**Hierarchical Clustering:** The sample data undergoes hierarchical clustering to form k clusters.
**Representative Points:** For each cluster, n representative points are chosen that best capture the geometry of the cluster.
**Point Shifting:** These representative points are then shifted towards the cluster's centroid by a fraction p to reduce the effect of outliers.
**Assigning Clusters:** Each point in the complete dataset is assigned to the nearest cluster based on the minimum distance to the shifted representative points.
**Visualization:** Finally, the clustered points are plotted using different colors to visualize the clustering results.