#!/usr/bin/env python3
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class Euler(ABC):
    """ Base class for calculating diff equations using Euler's method. """
    @abstractmethod
    def diff_equation_system(self, x: float, y: float) -> float:
        """ That method needs to be implemented and has to return value of the derivative dy/dx. """
        pass

    def get_results(self, dx: float, x0: float = 0, y0: float = 1, max_value: float = 5) -> tuple[list, list]:
        """ Returns both array of x values, array of y values and also exact result of diff. equation for the same x arguments. """
        # initial conditions for diff eq.:
        x = x0
        y = y0

        x_list = []
        y_list = []

        dydx = self.diff_equation_system(x, y)
        for i in range(int(max_value / dx)):
            newY = y + (dydx * dx)
            dydx = self.diff_equation_system(x, y) # derivative
            newX = x + dx
            
            x = newX
            y = newY

            x_list.append(x)
            y_list.append(y)
        return x_list, y_list

    def draw_data(self, x_list: tuple[float], y_list: tuple[float], dx: float, y_list_exact: tuple[float] = None) -> None:
        """ Draws plot with data. """
        if y_list_exact != None:
            plt.plot(x_list, y_list_exact, label='exact value')
        plt.plot(x_list, y_list, '--', label=f"Euler's approximation, step {dx}")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.title('step size: ' + str(dx), fontsize=9)
        plt.xlim(0)
        plt.ylim(0)

    def draw_data_and_error(self, column: int, x_list: tuple[float], y_list: tuple[float], dx: float, y_list_exact: tuple[float], columns_count: int=4) -> None: # column from 0 to columns_count-1
        """ Draws plot with data and plot with corresponding error one the defined subplot defined by variable 'column'. """
        # 1st plot - values:
        plt.subplot(201 + column + (columns_count * 10))
        self.draw_data(x_list, y_list, dx, y_list_exact)

        # 2nd plot - error:
        plt.subplot(201 + (column + columns_count) + (columns_count * 10))
        y_error = [abs(ye - y)/y*100 for y, ye in zip(y_list, y_list_exact)]
        plt.plot(x_list, y_error)
        plt.xlim(0)
        plt.ylim(0)
        plt.xlabel('x')
        plt.ylabel('Error [%]')
    
    def show_plots():
        plt.show()
