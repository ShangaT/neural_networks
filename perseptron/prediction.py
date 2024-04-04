#!/usr/bin/python
from perceptron import Perceptron
import pandas as pd

df = pd.read_csv('dollar.csv')

#подготовка данных
rate = df['rate'].to_list()
for i in range(len(rate)):
    rate[i] = rate[i] / 100

x = []
for i in range(len(rate)-1):
    x_i = [rate[i], rate[i+1]]
    x.append(x_i)

y = []
for i in range(2, len(rate)):
    y_i = [rate[i]]
    y.append(y_i)

x_test = x[len(x)-1]
del x[len(x)-1]

#обучение и предсказание
perseptron = Perceptron(len(x[0]), 2, 2, len(y[0]))
perseptron.lerning(x, y, r=0.01, error=0.02)
test_result = perseptron.predict(x_test)
result = [i * 100 for i in test_result]
print(result)    