import matplotlib.pyplot as plt
import numpy as np
import pickle
from sklearn.model_selection import train_test_split

#for the first trials we always have 7 values to train. This might change in later implementations
#we test the pattern for around 10 different series

#first we want to learn the +1 function:
#it adds 1 at every step in time

add_one_X = np.zeros((10,7))
for i in range(10):
    add_one_X[i,:] = np.arange(i,i+7)


add_one_Y = np.arange(7,17)
print(add_one_X)
print(add_one_Y)
