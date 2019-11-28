#!/usr/bin/python3.7
from lib.NueralNetwork import NeuralNetwork

if __name__ == "__main__":
    nn = NeuralNetwork([3, 2, 4], 0)
    print(nn.weights)
