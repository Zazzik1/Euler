#!/usr/bin/env python3
from enum import Enum
from src.euler import Euler

class constants(Enum):
    u_max = 0.16 # h^-1
    K_N = 0.010 # g N/L
    Y_XN = 31 # biomass/g nitrogen
    beta_max = 0.3 # g ethanol g biomass^-1 h^-1
    K_S = 10 # g sugar/L
    Y_ES = 0.47 # g ethanol/g sugar
    kd = 0.0001 # L/g ethanol h

class YeastEuler(Euler):
    def diff_equation_system(self, x: float, y: float) -> float:
        """ A system of differential equations. """
        return 2 * x # to implement

if __name__=='__main__':
    e = YeastEuler()
    step = 0.005
    x_list, y_list = e.get_results(step, x0=0)
    e.draw_data(x_list, y_list, step)
    YeastEuler.show_plots()