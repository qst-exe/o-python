import numpy
import matplotlib.pyplot as matplotlib

class New:
    def __init__(self, type='opai'):
        self.type = type

    def __calculateOppaiY(self, x):
        if self.type == 'bunkyo':
            e = numpy.e
            y_1 = (0.8 * (e ** ((-x ** 2) / 2)))
            y_2 = (e ** (-(x - 1.4) ** 2))
            y_3 = ((1 / 6) * (e ** (-(2 * x - 4.17) ** 2)))
            y_4 = ((1 / 8) * (e ** (-(6.9 * x - 8.3) ** 2)))
            y = y_1 + y_2 + y_3 + y_4

            return y

        elif self.type == 'nagoya':
            y_1 = (1.2 * numpy.exp(-0.5 * x ** 2))
            y_2 = (numpy.exp(0.1 * x) - 1.3 ** (0.6 * x) - 1.1 ** -x)
            y_3 = (0.2 * numpy.exp(-7 * (x - 0.8) ** 8))
            y_4 = (0.1 * numpy.exp(-(8 * x - 2) ** 2) - 1.1 ** (x - 6))
            y_5 = (0.4 * numpy.exp(-0.04 * x ** 8))
            y_6 = (0.4 * numpy.exp(-0.04 * (x + 3) ** 8))
            y_7 = (1.2)
            y = y_1 + y_2 + y_3 + y_4 + y_5 + y_6 + y_7

            return y

        else:
            y_1 = ((numpy.sqrt((numpy.absolute(1 - x) + 1 - x) / 2) + (1 / 4)) * numpy.exp(-(1 - x) ** 2))
            y_2_1 = (1 / 40)
            y_2_2 = (numpy.absolute(1 - 2 ** 4 * (5 * x - 3) ** 4))
            y_2_3 = (numpy.absolute(1 - 2 ** 9 * (5 * x - 3) ** 4))
            y_2_4 = (2 - 528 * (5 * x - 3) ** 4)
            y_2 = (y_2_1 * (y_2_2 + y_2_3 + y_2_4))
            y = y_1 + y_2

            return y


    def __plot(self, x, y):
        matplotlib.title(self.type)
        matplotlib.axes().set_aspect('equal', 'datalim')
        matplotlib.grid()
        matplotlib.plot(x, y, 'black')
        matplotlib.show()

    def show(self):
        x = numpy.arange(-3, 4 + 0.01, 0.01)
        y = self.__calculateOppaiY(x)
        self.__plot(x, y)