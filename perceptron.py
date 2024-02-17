#!/usr/bin/python
import random, math

class Element:
    def __init__(self, a_size):
        self.a = [random.uniform(0, 0.1) for i in range(0, a_size)]
        self.y = 0
        self.g = 0
        self.d = 0

    def sigmoid(self, x):
        # Функция активации - сигмоид
        return 1 / (1 + math.exp(-x))

    def calculation_y(self, layer_previous, layer_current):
        for i in range(len(layer_current)):
            multiplication = 0
            for j in range(len(layer_previous)):                
                multiplication += layer_previous[j].a[i] * layer_previous[j].y
            layer_current[i].y = self.sigmoid(multiplication)        
        
    def calculation_last_g(self, layer):
        for i in range(len(layer)):
            g = layer[i].y * (1 - layer[i].y) * (layer[i].d - layer[i].y)
            layer[i].g = g

    def calculation_g(self, layer_previous, layer_current):
        for i in range(len(layer_current)):
            summa = 0
            for j in range(len(layer_previous)):
                summa += layer_current[i].a[j] * layer_previous[j].g
        g = layer_current[i].y * (1 - layer_current[i].y) * summa
        layer_current[i].g = g

    def calculation_a(self, layer_previous, layer_current, r):
        for i in range(len(layer_current)):
            for j in range(len(layer_previous)):
                a = layer_current[i].a[j] + layer_previous[j].g * layer_current[i].y * r
                layer_current[i].a[j] = a
    
class Perceptron(Element):
    def __init__(self, input_vector_size: int, input_size: int, hidden_size: int, output_size: int):
        self.input_vector = [Element(input_size) for i in range(0, input_vector_size)]
        self.input_layer = [Element(hidden_size) for i in range(0, input_size)]
        self.hidden_layer = [Element(output_size) for i in range(0, hidden_size)]
        self.output_layer = [Element(0) for i in range(0, output_size)]

    def forward(self, x):
        #задаем входному слою значения y из значений входного вектора
        for i in range(len(x)): 
            self.input_vector[i].y = x[i]
        #расчитываем y для осталььных - прямой проход
        self.calculation_y(self.input_vector, self.input_layer)
        self.calculation_y(self.input_layer, self.hidden_layer)
        self.calculation_y(self.hidden_layer, self.output_layer)

    def back_popagation(self, y, r):
        #задаем выходному слою значения d из выходного вектора
        for i in range(len(y)):
            self.output_layer[i].d = y[i]

        self.calculation_last_g(self.output_layer) #расчитываем g для последнего слоя

        self.calculation_g(self.output_layer, self.hidden_layer) #расчитываем g для скрытого слоя
        self.calculation_a(self.output_layer, self.hidden_layer, r) #пересчитываем веса

        #повторяем для других слоев
        self.calculation_g(self.hidden_layer, self.input_layer)
        self.calculation_a(self.hidden_layer, self.input_layer, r)

        self.calculation_g(self.input_layer, self.input_vector)
        self.calculation_a(self.input_layer, self.input_vector, r)

    def lerning(self, x, y, r, error):
        epohe = 0
        while True:                        
            for i in range(len(x)):
                self.forward(x[i])
                self.back_popagation(y[i], r)

            delta = [] #отклонение
            for i in range(len(y[0])):
                delta.append(abs(self.output_layer[i].d - self.output_layer[i].y))
                               
            epohe += 1 #вывод кол-ва итераций
            print('Кол-во эпох: ', epohe, end='\r')
            
            if all(element <= error for element in delta): break
            # if math.isnan(self.output_layer[0].d - self.output_layer[0].y): 
            #     print('Ошибка')
            #     break
        print('Кол-во эпох: ', epohe)

    def predict(self, x):
        for i in range(len(x)): 
            self.input_vector[i].y = x[i]
        self.forward(x)        
        y = []
        for i in self.output_layer:
            y.append(i.y)
        return y
