#!/usr/bin/env python3
from src.euler import Euler
from math import exp

class ExpEuler(Euler):
    def initial_values(self):
        """ Initial value for variable y. """
        self.y = 1
        self.y_list = []

    def diff_equation_system(self, x: float, dx: float):
        """ Derivative 'dy/dx = y'. Hence it is known that dy = y * dx. """
        dy = self.y * dx

        self.y += dy
        self.y_list.append(self.y)


if __name__ == '__main__':
    e = ExpEuler()
    for id, step in enumerate([0.5, 0.05, 0.005, 0.0005]):
        x_list = e.get_results(step)
        y_list_exact = [exp(x) for x in x_list]
        e.draw_data_and_error(id, x_list, e.y_list, step, y_list_exact)
    Euler.show_plots()