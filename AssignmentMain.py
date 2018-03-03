import matplotlib.pyplot as plt
import numpy as np
import math as math


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
        lines_list.append([x for x in line.split()])
    return lines_list


EX_datalist = get_lines(EX_dataraw[1:])
EY_datalist = get_lines(EY_dataraw[1:])


def find_e_strength(Ex_list, Ey_list):  # inputs two lists of lines and outputs the resulting e field strength
    matrix_ex = np.array(Ex_list, dtype=float)  # converting to numpy array
    matrix_ey = np.array(Ey_list, dtype=float)
    field_strength = np.sqrt(np.square(matrix_ex) + np.square(matrix_ey))
    return field_strength


np.seterr(divide='ignore', invalid='ignore')  # To stop divide by zero errors


def find_e_angle(Ex_list, Ey_list):
    matrix_ex = np.array(Ex_list, dtype=float)  # converting to numpy array
    matrix_ey = np.array(Ey_list, dtype=float)
    angle = np.arctan(np.divide(matrix_ey, matrix_ex, out=np.zeros_like(matrix_ey), where=matrix_ex != 0))
    return angle


e_field_strength = find_e_strength(EX_datalist, EY_datalist)
e_field_angle = find_e_angle(EX_datalist, EY_datalist)


def interp_efield(desiredx, inputlist):  # type_ float , list -> list
    percent_of_file = desiredx / 5.0
    desired_index = round(101 * percent_of_file, 4)
    rounded_index = int(math.floor(desired_index))
    result = []
    for line in inputlist:
        percentage = (float(line[rounded_index + 1]) - float(line[rounded_index])) * abs(desired_index - rounded_index)
        result.append(float(percentage) + float(line[rounded_index]))
    return result


efieldyvalues = interp_efield(0.5, e_field_strength)
x_values = np.arange(0, 5, (5 / 101))
plt.semilogx(x_values, efieldyvalues)
plt.show()


def save_file(filename,array,header,format):
    np.savetxt(filename,array,fmt=format,header=header)


save_file("Deg_grid.txt", e_field_angle, "E field angle in uniform X Y grid", "%1.2f")
save_file("Etot_grid.txt", e_field_strength, "E field strength in uniform X Y grid", "%1.5e")
