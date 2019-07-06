import matplotlib.pyplot as plt

data = [[0]*2 for i in range(18)]

x = [100, 275, 240, 50, 300, 500, 640, 730, 600, 930, 100, 1465, 1005, 1225, 1150, 1370, 1480, 1750]
y = [1410, 1600, 2000, 2600, 2930, 2250, 2600, 1700, 1100, 1420, 1700, 2020, 1000, 930, 600, 950, 1160, 1500]

for i in range(18):
    data[i][0] = x[i]
    for j in range(2):
        data[i][j] = y[j]

plt.figure()
plt.scatter(x, y)
plt.show()

colors = 10*["g","r","c","b","k"]


class K_Means:
    def __init__(self, k=3, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self,data):

        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification],axis=0)

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid) / original_centroid*100.0) > self.tol:
                    print(np.sum((current_centroid - original_centroid) / original_centroid*100.0))
                    optimized = False

            if optimized: break

clf = K_Means()
clf.fit(data)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1],
                marker="o", color="k", s=20, linewidths=5)

for classification in clf.classifications:
    color = colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker="x", color=color, s=20, linewidths=5)

plt.show()