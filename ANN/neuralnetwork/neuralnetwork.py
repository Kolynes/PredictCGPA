from ..matrix import matrix
import math

class NeuralNet:
    _layers: list

    def __init__(self, *layers):
        self._layers = layers

    def sigmoid(self, activation: float) -> float:
        return 1/ (1 + math.exp(-activation))

    def feed_foward(self, input_matrix: matrix.Matrix) -> matrix.Matrix:
        result = input_matrix
        for i in range(len(self._layers)):
            if i == 0: 
                continue
            layer: matrix.Matrix = self._layers[i]
            result = (layer * result).map(self.sigmoid)
        return result

    def train(self,):
        pass