import matplotlib.pyplot as plt
import numpy as np


def open_file(filename):  # Opens file and reads it, returning a list of the lines and closes the file
    f = open(filename, "r")
    input_data = f.readlines()
    f.close()
    return input_data


# calling the open file function
EX_dataraw = open_file("Ex_grid.txt")
EY_dataraw = open_file("Ey_grid.txt")


def get_lines(inputlist):  # opens the list of lines, splits spaces, adds them to a list, outputs a list of line lists
    lines_list = []
    for line in inputlist:
        lines_list.append([float(x) for x in line.split()])
    return lines_list


EX_datalist = get_lines(EX_dataraw[1:])
EY_datalist = get_lines(EY_dataraw[1:])
print(len(EX_datalist[0]))


def find_e_strength(Ex_list, Ey_list):  # inputs two lists of lines and outputs the resulting e field strength
    matrix_ex = np.nan_to_num(np.array(Ex_list, dtype=float))  # dealing with nan values and converting to numpy array
    matrix_ey = np.nan_to_num(np.array(Ey_list, dtype=float))
    field_strength = np.sqrt(((matrix_ex ** 2) + (matrix_ey ** 2)))
    return field_strength


np.seterr(divide='ignore', invalid='ignore')  # To stop divide by zero errors


def find_e_angle(Ex_list, Ey_list):
    matrix_ex = np.nan_to_num(np.array(Ex_list, dtype=float))  # dealing with nan values and converting to numpy array
    matrix_ey = np.nan_to_num(np.array(Ey_list, dtype=float))
    angle = np.arctan(np.divide(matrix_ey, matrix_ex, out=np.zeros_like(matrix_ey), where=matrix_ex != 0))
    return angle


e_field_strength = find_e_strength(EX_datalist, EY_datalist)
e_field_angle = find_e_angle(EX_datalist, EY_datalist)

nx, ny = 101, 101
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)
plt.figure(1)
plt.subplot(111)
color = 2 * np.log(np.hypot(np.array(EX_datalist), np.array(EY_datalist)))
plt.streamplot(x, y, np.array(EX_datalist), np.array(EY_datalist), linewidth=1, color=color, cmap="inferno", density=6,
               arrowstyle='->', arrowsize=1.5)
plt.figure(2)
plt.subplot(111)
plt.imshow(e_field_strength, cmap='spring', interpolation='none')
plt.colorbar()
plt.show()
