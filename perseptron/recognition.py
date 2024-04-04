#!/usr/bin/python
from perceptron import Perceptron

x=[
        [1, 0, 1,
         0, 1, 0,
         1, 0, 1],

        [1, 1, 1,
         1, 0, 1,
         1, 1, 1],

        [0, 0, 1,
         0, 1, 0,
         1, 0, 1],

        [1, 0, 1,
         1, 0, 1,
         1, 1, 1],

        [1, 0, 0,
         0, 1, 0,
         1, 0, 1],

        [1, 1, 1,
         1, 0, 0,
         1, 1, 1],

        [1, 0, 1,
         0, 1, 0,
         0, 0, 1],
        
        [1, 1, 1,
         0, 0, 1,
         1, 1, 1]]

y = [[1], [0], [1], [0], [1], [0], [1], [0]]

data_1=[1, 0, 1,
        0, 1, 0,
        1, 0, 0]

data_2=[1, 1, 1,
        1, 0, 1,
        1, 0, 1]

data_3=[1, 0, 1,
        0, 0, 0,
        1, 0, 1]

perseptron = Perceptron(len(x[0]), 4, 4, len(y[0]))
perseptron.lerning(x, y, r=0.1, error=0.1)

print(f'ЗНАЧЕНИЕ 1: {perseptron.predict(data_1)}')
print(f'ЗНАЧЕНИЕ 2: {perseptron.predict(data_2)}')
print(f'ЗНАЧЕНИЕ 3: {perseptron.predict(data_3)}')