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
print(EX_datalist[0])


def find_e_strength(Ex_list, Ey_list):
    result = []
    column_ex = []
    column_ey = []
    for x in range(0,len(Ex_list[0])):
        for k, n in zip(Ex_list, Ey_list):
            column_ex.append(k[x])
            column_ey.append(n[x])
            print(column_ex)
            result.append([np.sqrt(a ** 2 * b ** 2) for a, b in zip(column_ex, column_ey)])
    return result


e_field_strength = find_e_strength(EX_datalist, EY_datalist)

print(e_field_strength)
