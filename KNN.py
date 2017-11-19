# x = open("TrainData.txt")
# data = []
# for line in x:
#     data.append(line.split(','))
# print(data)
import numpy as np;
data = np.fromfile('TrainData.txt')
print(data)
