import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

from pathlib import Path

class Result:
    def __init__(self):
        self.key    = []
        self.val    = {}

    def add_result(self):
        pass

class Data:
    def __init__(self):
        base = Path(__file__).resolve().parents[1]
        self.file_data_point_dir = base / "data" / "point.csv"
    
    def get_point(self):
        pt = np.genfromtxt(self.file_data_point_dir, delimiter= ",")
        return pt

class Plot:
    def __init__(self):
        self.figsize = (8,8)
    
    def plot_point(self, x, y):
        plt.figure(figsize= self.figsize)
        plt.plot(x, y, "bo")

# class

if __name__=="__main__":
    print(Path(__file__).re)