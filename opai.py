import numpy
import matplotlib.pyplot as matplotlib

class New:
    # 初期値は大阪大学のおっぱいとする
    def __init__(self, type='osaka'):
        self.type = type

    # おっぱい計算のロジックは見せない
    def __calculateOppaiY(self, x):
        if self.type == 'bunkyo':
            e = numpy.e
            return (0.8 * (e ** ((-x ** 2) / 2))) + (e ** (-(x - 1.4) ** 2)) + \
                   ((1 / 6) * (e ** (-(2 * x - 4.17) ** 2))) + ((1 / 8) * (e ** (-(6.9 * x - 8.3) ** 2)))

        elif self.type == 'nagoya':
            return (1.2 * numpy.exp(-0.5 * x ** 2)) + (numpy.exp(0.1 * x) - 1.3 ** (0.6 * x) - 1.1 ** -x) + \
                   (0.2 * numpy.exp(-7 * (x - 0.8) ** 8)) + (0.1 * numpy.exp(-(8 * x - 2) ** 2) - 1.1 ** (x - 6)) + \
                   (0.4 * numpy.exp(-0.04 * x ** 8)) + (0.4 * numpy.exp(-0.04 * (x + 3) ** 8)) + (1.2)

        else:
            return ((numpy.sqrt((numpy.absolute(1 - x) + 1 - x) / 2) + (1 / 4)) * numpy.exp(-(1 - x) ** 2)) + \
                   (1 / 40) * ((numpy.absolute(1 - 2 ** 4 * (5 * x - 3) ** 4)) + (numpy.absolute(1 - 2 ** 9 * (5 * x - 3) ** 4)) + (2 - 528 * (5 * x - 3) ** 4))

    # おっぱい描画のロジックは見せない
    def __plot(self, x, y):
        matplotlib.title(self.type)
        matplotlib.axes().set_aspect('equal', 'datalim')
        matplotlib.grid()
        matplotlib.plot(x, y, 'black')
        matplotlib.show()

    # おっぱいを見せるのは外部から参照できても問題ない
    def show(self):
        x = numpy.arange(-3, 4 + 0.01, 0.01)
        y = self.__calculateOppaiY(x)
        self.__plot(x, y)