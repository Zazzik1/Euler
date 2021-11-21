#!/usr/bin/env python3
from dataclasses import dataclass
from src.euler import Euler

class constants():
    u_max = 0.16 # [1/h]
    K_N = 0.010 # [g_N/L]
    Y_XN = 31 # [g_biomass/g_nitrogen]
    beta_max = 0.3 # [g_ethanol/(g_biomass * h)]
    K_S = 10 # [g_sugar/L]
    Y_ES = 0.47 # [g_ethanol/g_sugar]
    kd = 0.0001 # [L/g ethanol h]

@dataclass
class YeastEuler(Euler):
    """ Class used to simulate the process of yeast growth in nitrogen-limited fermentation. """
    c: constants
    N: float # nitrogen concentration [mg/L]
    S: float # sugar concentration [g/L]
    Xv: float # viable cell concentration [g/L]
    E: float = 0 # ethanol concentration [g/L]

    def initial_values(self):
        """ Setting initial values for variables used in diff equations. """
        self.N_list = []
        self.S_list = []
        self.E_list = []
        self.Xv_list = []

        u, beta = self.u_beta()
        self._equation_Xv(1, u)
        self._equation_N(1, u)
        self._equation_E(1, beta)
        self._equation_S(1, beta)

    def _equation_N(self, dt: float, u: float):
        """ Updates N by dN. """
        self.dN = -u * self.Xv / self.c.Y_XN * dt
        self.N += self.dN
        self.N_list.append(self.N)

    def _equation_S(self, dt: float, beta: float):
        """ Updates S by dS. """
        self.dS = -beta * self.Xv / self.c.Y_ES * dt
        self.S += self.dS
        self.S_list.append(self.S)

    def _equation_E(self, dt: float, beta: float):
        """ Updates E by dE. """
        self.dE = beta * self.Xv * dt
        self.E += self.dE
        self.E_list.append(self.E)

    def _equation_Xv(self, dt: float, u: float):
        """ Updates Xv by dXv. """
        kd = self.c.kd * self.E
        self.dXv = (u * self.Xv - kd * self.Xv) * dt
        self.Xv += self.dXv
        self.Xv_list.append(self.Xv)

    def u_beta(self) -> tuple[float, float]:
        """ Returns parameters required to calculate next values from diff equations. """
        u = (self.c.u_max * self.N) / (self.c.K_N + self.N)
        beta = (self.c.beta_max * self.S) / (self.c.K_S + self.S)
        return u, beta

    def diff_equation_system(self, x: float, dx: float) -> float:
        """ System of diff equations. """
        u, beta = self.u_beta()
        
        self._equation_Xv(dx, u)
        self._equation_N(dx, u)
        self._equation_E(dx, beta)
        self._equation_S(dx, beta)


if __name__=='__main__':
    e = YeastEuler(c=constants, N=2, S=5, Xv=0.001)
    step = 0.02
    x_list = e.get_results(step, max_x=300)
    e.draw_data(x_list, e.E_list[1:], step, label='Ethanol concentration [g/L]', color='blue', marker='--')
    e.draw_data(x_list, e.S_list[1:], step, label='Sugar concentration [g/L]', color='black')
    e.draw_data(x_list, e.Xv_list[1:], step, label='Biomass concentration [g/L]', color='black', marker='--')
    e.draw_data(x_list, e.N_list[1:], step, label='Nitrogen concentration [mg/L]', color='blue')

    Euler.show_plots()