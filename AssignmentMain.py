import math as math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import LogLocator


def open_file(filename):  # Opens file and reads it, returning a list of the lines and closes the file
    f = open(filename, "r")
    input_data = f.readlines()
    f.close()
    return input_data


# calling the open file function
EX_dataraw = open_file("Ex_grid.txt")
EY_dataraw = open_file("Ey_grid.txt")


def get_lines(inputlist):  # opens the list of lines, splits spaces, adds values to a list, outputs a list of line lists
    lines_list = []
    for line in inputlist:
        lines_list.append([x for x in line.split()])
    return lines_list


# calling the function which splits the lines and makes the data usable
EX_datalist = get_lines(EX_dataraw[1:])
EY_datalist = get_lines(EY_dataraw[1:])


def find_e_strength(Ex_list, Ey_list):  # inputs two lists of lines and outputs e field strength as numpy array
    matrix_ex = np.array(Ex_list, dtype=float)  # converting to numpy array to ease matrix multiplication
    matrix_ey = np.array(Ey_list, dtype=float)
    field_strength = np.sqrt(np.square(matrix_ex) + np.square(matrix_ey))
    return field_strength


def find_e_angle(Ex_list, Ey_list): # inputs two lists of lines and returns a numpy array of angles of e field
    matrix_ex = np.array(Ex_list, dtype=float)  # converting to numpy array
    matrix_ey = np.array(Ey_list, dtype=float)
    angle = np.arctan(np.divide(matrix_ey, matrix_ex, out=np.zeros_like(matrix_ey), where=matrix_ex != 0))
    # divide calculation only divides when matrix_ex != 0 but when matrix_ex = 0 , 0 is outputted
    return angle


e_field_strength = find_e_strength(EX_datalist, EY_datalist)
e_field_angle = find_e_angle(EX_datalist, EY_datalist)


def interp_efield(desired_y, inputlist):
    # inputs a desired y between 0 - 5 m , the inputted list is then interpolated so any y value can be found
    percent_of_file = desired_y / 5.0
    desired_index = 101 * percent_of_file
    rounded_index = int(math.floor(desired_index))
    percentage = (inputlist[rounded_index + 1] - inputlist[rounded_index]) * abs(desired_index - rounded_index)
    return percentage + inputlist[rounded_index]


efieldyvalues = interp_efield(0.5, e_field_strength)
x_values = np.arange(0, 5, (5 / 101))  # X values are generated between 0 - 5 m to limit the plot range
plt.figure()
ax1 = plt.subplot(1, 1, 1)
ax1.plot(x_values, efieldyvalues, 'r-*', label='Electric field strength at y = 0.5m')
ax1.set_xscale('log')  # setting x axis to logarithmic scale
ax1.set_xlabel("Distance (m)", fontsize=15)
ax1.set_ylabel("Electric field strength (V/m) ", fontsize=15)
ax1.legend(numpoints=1, loc='upper center', bbox_to_anchor=(0.32, 0.95), fancybox=True, shadow=True, ncol=5)
ax1.tick_params(axis="both", which="major", labelsize=15, color="b", width=1, length=5, labelcolor="black")
ax1.yaxis.set_minor_locator(AutoMinorLocator(5))
ax1.xaxis.set_minor_locator(LogLocator(10,subs="auto", numticks=10))
ax1.yaxis.set_tick_params(which='minor', right='false', width=0.7, size=2)
ax1.xaxis.set_tick_params(which='minor', right='false', width=0.7, size=2)
ax1.grid()
plt.tight_layout()
plt.show()


def save_file(filename, array, header, format):  # This function saves the file using the numpy savetxt method
    np.savetxt(filename, array, fmt=format, header=header)


# saving both files with headers and converting angles into degrees
save_file("Deg_grid.txt", np.degrees(e_field_angle), "E field angle in uniform X Y grid", "%1.2f")
save_file("Etot_grid.txt", e_field_strength, "E field strength in uniform X Y grid", "%1.5e")
