import matplotlib.pyplot as plt

data = [[0]*2 for i in range(18)]

x = [100, 275, 240, 50, 300, 500, 640, 730, 600, 930, 100, 1465, 1005, 1225, 1150, 1370, 1480, 1750]
y = [1410, 1600, 2000, 2600, 2930, 2250, 2600, 1700, 1100, 1420, 1700, 2020, 1000, 930, 600, 950, 1160, 1500]

for i in range(18):
    data[i][0] = x[i]
    for j in range(2):
        data[i][j] = y[j]

        plt.figure()
        plt.scatter(data[i][0], data[0][j]])
        plt.show()