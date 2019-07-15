import numpy
import matplotlib.pyplot as matplotlib

class Bunkyo:
    def calculateOppaiY(self, x):
        e = numpy.e
        y_1 = (0.8 * (e ** ((-x ** 2) / 2)))
        y_2 = (e ** (-(x - 1.4) ** 2))
        y_3 = ((1 / 6) * (e ** (-(2 * x - 4.17) ** 2)))
        y_4 = ((1 / 8) * (e ** (-(6.9 * x - 8.3) ** 2)))
        y = y_1 + y_2 + y_3 + y_4

        return y

    def plot(self, x, y):
        matplotlib.title('Bunkyo')
        matplotlib.axes().set_aspect('equal', 'datalim')
        matplotlib.grid()
        matplotlib.plot(x, y, 'black')
        matplotlib.show()

    def show(self):
        x = numpy.arange(-3, 4 + 0.01, 0.01)
        y = self.calculateOppaiY(x)
        self.plot(x, y)