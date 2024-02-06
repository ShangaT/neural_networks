#!/usr/bin/python
import random

class Element:
    def __init__(self, a_size):
        self.a = [random.uniform(0, 0.1) for i in range(0, a_size)]
        self.y = 0
        self.g = 0
        self.d = 0

    def calculation_y(self, layer_previous, layer_current):
        for i in range(len(layer_current)):
            for j in range(len(layer_previous)):                
                multiplication = layer_previous[j].a[i] * layer_previous[j].y
                layer_current[i].y += round(multiplication, 10)
        
    def calculation_last_g(self, layer):
        for i in range(len(layer)):
            g = layer[i].y * (1 - layer[i].y) * (layer[i].d - layer[i].y)
            layer[i].g = round(g, 10)

    def calculation_g(self, layer_previous, layer_current):
        for i in range(len(layer_current)):
            summa = 0
            for j in range(len(layer_previous)):
                summa += layer_current[i].a[j] * layer_previous[j].g
        g = layer_current[i].y * (1 - layer_current[i].y) * summa
        layer_current[i].g = round(g, 10)

    def calculation_a(self, layer_previous, layer_current, r):
        for i in range(len(layer_current)):
            for j in range(len(layer_previous)):
                a = layer_current[i].a[j] + layer_previous[j].g * layer_current[i].y * r
                layer_current[i].a[j] = round(a, 10)
    
class Perceptron(Element):
    def __init__(self, input_vector_size: int, input_size: int, hidden_size: int, output_size: int):
        self.input_vector = [Element(input_size) for i in range(0, input_vector_size)]
        self.input_layer = [Element(hidden_size) for i in range(0, input_size)]
        self.hidden_layer = [Element(output_size) for i in range(0, hidden_size)]
        self.output_layer = [Element(0) for i in range(0, output_size)]

    def back_popagation(self, x, y, r):
        #задаем входному слою значения y из значений входного вектора
        for i in range(len(x)): 
            self.input_vector[i].y = x[i]
        #задаем выходному слою значения d из выходного вектора
        for i in range(len(y)):
            self.output_layer[i].d = y[i]

        #while True:
            #расчитываем y для осталььных - прямой проход
        self.calculation_y(self.input_vector, self.input_layer)
        self.calculation_y(self.input_layer, self.hidden_layer)
        self.calculation_y(self.hidden_layer, self.output_layer)

        self.calculation_last_g(self.output_layer) #расчитываем g для последнего слоя

        self.calculation_g(self.output_layer, self.hidden_layer) #расчитываем g для скрытого слоя
        self.calculation_a(self.output_layer, self.hidden_layer, r) #пересчитываем веса

        #повторяем для других слоев
        self.calculation_g(self.hidden_layer, self.input_layer)
        self.calculation_a(self.hidden_layer, self.input_layer, r)

        self.calculation_g(self.input_layer, self.input_vector)
        self.calculation_a(self.input_layer, self.input_vector, r)

    def predict(self, x):
        for i in range(len(x)): 
            self.input_vector[i].y = x[i]

        self.calculation_y(self.input_vector, self.input_layer)
        self.calculation_y(self.input_layer, self.hidden_layer)
        self.calculation_y(self.hidden_layer, self.output_layer)
        return self.output_layer[0].y
        
        #delta = [abs(element.d - element.y) for element in self.output_layer]
            # for element in self.output_layer:
            #     delta.append(abs(element.d - element.y))

            # for i in delta:
            #     if i >= 0.5: break
            # else: break
            #if epohe == 0: break

x = [[1, 0, 1,
      0, 1, 0,
      1, 0, 1],
     
     [1, 1, 1,
      1, 0, 1,
      1, 1, 1],
      
      [1, 0, 0,
       0, 1, 0,
       1, 0, 1],
      
      [0, 1, 1,
       1, 0, 1,
       1, 1, 1]]

y = [[1], [0], [1], [0]]

perseptron = Perceptron(len(x[0]), 3, 3, len(y[0]))

while True:
    for i in range(len(y)):
        perseptron.back_popagation(x[i], y[i], r=0.1)
        delta = abs(perseptron.output_layer[0].d - perseptron.output_layer[0].y)
    if delta <= 0.2: break

a = perseptron.predict([1,0,1,0,1,0,1,0,1])

print(a)

