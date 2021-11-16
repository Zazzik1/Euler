#!/usr/bin/env python3
import matplotlib.pyplot as plt
from math import exp

def euler(dx=0.005, max_value=5):
    """ returns both array of x values, array of y values and also exact result of diff. equation for the same x arguments """
    # initial conditions for diff eq.:
    x = 0
    y = 1

    val_x = []
    val_y = []
    exact_y = []

    dydx = y
    for i in range(int(max_value / dx)):
        newY = y + (dydx * dx)
        dydx = y # derivative - here put diff eq. (dy/dx = y => y = e^x)
        newX = x + dx
        
        val_x.append(newX)
        val_y.append(newY)
        exact_y.append(exp(newX))

        x = newX
        y = newY
    return val_x, val_y, exact_y

def draw_2plots(column, val_x, val_y, exact_y, dx): # column from 0 to 3
    """ draws plot with data and plot with corresponding error """
    # 1st plot - values:
    plt.subplot(241 + column)
    plt.plot(val_x, exact_y, label='exact value')
    plt.plot(val_x, val_y, '--', label='Euler\'s approximation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('dy/dx = y => y=e^x, step size: ' + str(dx), fontsize=9)
    plt.xlim(0)
    plt.ylim(0)

    # 2nd plot - error:
    plt.subplot(241 + (column + 4))
    error_x = []
    for id in range(len(val_y)):
        error_x.append(abs(exact_y[id] - val_y[id])/exact_y[id]*100)
    plt.plot(val_x, error_x)
    plt.xlim(0)
    plt.ylim(0)
    plt.xlabel('x')
    plt.ylabel('Error [%]')

if __name__ == '__main__':
    for id, step in enumerate([0.5, 0.05, 0.005, 0.0005]):
        val_x, val_y, exact_y = euler(step)
        draw_2plots(id, val_x, val_y, exact_y, step)
    plt.show()