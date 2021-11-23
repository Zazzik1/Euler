#!/usr/bin/env python3
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class Euler(ABC):
    """ Base class for calculating diff equations using Euler's method. """
    @abstractmethod
    def initial_values(self) -> None:
        """ Here assign initial values of variables. That method will be executed at the beginning of calculation. """
        pass
        
    @abstractmethod
    def diff_equation_system(self, x: float, dx: float) -> None:
        """ 
        That method needs to be implemented to assign object a new value of attribute(s) based on calculated derivative(s). 
        Example: dy/dx = y => dy = y * dx => on each iteration y changes by dy = y * dx, thus:
        self.y += y * dx
        """
        pass

    def get_results(self, dx: float, x0: float = 0, max_x: float = 5) -> tuple[list]:
        """ Calculates the defined set of diff equations for every iteration. Returns list of x values. """
        # initial conditions for diff eq.:
        x = x0
        x_list = []
        self.initial_values()

        for i in range(int(max_x / dx)):
            self.diff_equation_system(x, dx) # derivatives
            x = x + dx
            x_list.append(x)
        return x_list

    def draw_data(self, x_list: tuple[float], y_list: tuple[float], dx: float, y_list_exact: tuple[float] = None, label: str=None, marker: str=None, color: str=None) -> None:
        """ Draws plot with data. """
        if y_list_exact != None:
            plt.plot(x_list, y_list_exact, label='exact value')
        if label == None:
            label = f"Euler's approximation, step {dx}"
        if marker == None:
            marker = '-'
        plt.plot(x_list, y_list, marker, label=label, c=color)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.title('step size: ' + str(dx), fontsize=9)
        plt.xlim(0)
        plt.ylim(0)

    def draw_data_and_error(self, column: int, x_list: tuple[float], y_list: tuple[float], dx: float, y_list_exact: tuple[float], columns_count: int=4) -> None: # column from 0 to columns_count-1
        """ Draws plot with data and plot with corresponding error on subplot defined by variable 'column'. """
        # 1st plot - values:
        plt.subplot(201 + column + (columns_count * 10))
        self.draw_data(x_list, y_list, dx, y_list_exact, marker='--')

        # 2nd plot - error:
        plt.subplot(201 + (column + columns_count) + (columns_count * 10))
        y_error = []
        for y, ye in zip(y_list, y_list_exact):
            if y == 0:
                y_error.append(None)
            else:
                y_error.append(abs(ye - y)/y*100)
        plt.plot(x_list, y_error)
        plt.xlim(0)
        plt.ylim(0)
        plt.xlabel('x')
        plt.ylabel('Error [%]')
    
    @staticmethod
    def show_plots():
        plt.show()
