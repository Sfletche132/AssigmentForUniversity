import numpy as np
import matplotlib.pyplot as plt


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


print(EX_datalist[60])
print(EY_datalist[60])


def find_e_strength(Ex_list, Ey_list):  # inputs two lists of lines and outputs the resulting e field strength
    matrix_ex = np.nan_to_num(np.array(Ex_list, dtype=float))
    matrix_ey = np.nan_to_num(np.array(Ey_list, dtype=float))
    field_strength = np.sqrt(((matrix_ex**2) + (matrix_ey**2)))
    return field_strength


e_field_strength = find_e_strength(EX_datalist, EY_datalist)

print(e_field_strength)
plt.imshow(e_field_strength,cmap='Blues', interpolation='none')
plt.colorbar()
plt.show()
