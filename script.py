import numpy
import matplotlib.pyplot as plt
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

dataset = pandas.read_csv('international-airline-passengers.csv',
                          usecols=[1], engine='python', skipfooter=3)
plt.plot(dataset)
plt.show()
