import matplotlib.pyplot as plt
from math import sqrt, pow
import random

class KMeans:
    
    def __init__(self, k):
        self.k = k # 클러스터의 갯수
        self.means = None # 클러스터의 평균들

#유클리드 거리
    def EuclideanDistance(self, x, y): 
        S = 0
        for i in range(len(x)):
            S += pow(x[i] - y[i],2)
        return sqrt(S)

    def classify(self, input):
        return min(range(self.k), key=lambda i: EuclideanDistance(input, self.means[i]))

    def vector_mean(self, points):
        return (sum(points))/2

    def train(self, input):
        self.means = random.sample(input, self.k)
        assignments = None
        while True:
            new_assignments = map(self.classify, input)
        if assignments == new_assignments: return
        assignments = new_assignments
        for i in range(self.k):
            i_points = [p for p, a in zip(input, assignments) if a == i] # i 번 요소들의 리스트
            if i_points:
                self.means[i] = vector_mean(i_points) # 그것들의 평균 ( 중심점 )    

if __name__ == "__main__":
    inputs = [[100, 1410], [275, 1600], [240,2000], [50,2600], [300,2930], [500,2250], 
        [640,2600], [730,1700], [600, 1100], [930,1420], [100,1700], [1465,2020], 
        [1005,1000], [1225,930], [1150,600], [1370,950], [1480,1160], [1750,1500]]

    random.seed(0) 
    clusterer = KMeans(3)
    clusterer.train(inputs)

    plt.figure()
    plt.scatter(inputs[:,0], inputs[:,1], s=20)
    plt.show()
