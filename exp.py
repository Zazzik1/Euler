#!/usr/bin/env python3
from src.euler import Euler
from math import exp

class EulerExp(Euler):
    def diff_equation_system(self, x: float, y: float) -> float:
        """ Derivative 'dy/dx = y'. """
        return y

if __name__ == '__main__':
    e = EulerExp()
    for id, step in enumerate([0.5, 0.05, 0.005, 0.0005]):
        x_list, y_list = e.get_results(step)
        y_list_exact = [exp(x) for x in x_list]
        e.draw_data_and_error(id, x_list, y_list, step, y_list_exact)
    EulerExp.show_plots()