import math as math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator,LogLocator, NullFormatter


def open_file(filename):  # Opens file and reads it, returning a list of the lines and closes the file
    """
    param filename = string for the file name
    returns a list of lines, where a line is a string delimited by spaces
    """
    f = open(filename, "r")
    input_data = f.readlines()
    f.close()
    return input_data


# calling the open file function
EX_dataraw = open_file("Ex_grid.txt")
EY_dataraw = open_file("Ey_grid.txt")


def get_lines(inputlist):
    """
    param inputlist = list of raw data from the file, with each line as a string in the list
    returns a nested list, with each value having an index within the nested list
    """
    lines_list = []
    for line in inputlist:
        # uses a list comprehension to split the line strings and then appends them into a nested list
        lines_list.append([x for x in line.split()])
    return lines_list


# calling the function which splits the lines and makes the data usable
EX_datalist = get_lines(EX_dataraw[1:])
EY_datalist = get_lines(EY_dataraw[1:])


def find_e_strength(Ex_list, Ey_list):
    """
    param Ex_list = Equidistant grid of Ex values inputted as a list of lines
    param Ey_list = Equidistant grid of Ey values inputted as a list of lines
    returns a list of electric field strength values in an equidistant grid
    """
    matrix_ex = np.array(Ex_list, dtype=float)  # converting to numpy array
    matrix_ey = np.array(Ey_list, dtype=float)
    #  Performing the electric field strength calculation
    field_strength = np.sqrt(np.square(matrix_ex) + np.square(matrix_ey))
    return field_strength


def find_e_angle(Ex_list, Ey_list):
    """
    param Ex_list = Equidistant grid of Ex values inputted as a list of lines
    param Ey_list = Equidistant grid of Ey values inputted as a list of lines
    returns list of angles in the electric field
    """
    matrix_ex = np.array(Ex_list, dtype=float)  # converting to numpy array
    matrix_ey = np.array(Ey_list, dtype=float)
    # performing angle calculation and handling divide by zero errors
    angle = np.arctan(np.divide(matrix_ey, matrix_ex, out=np.zeros_like(matrix_ey), where=matrix_ex != 0))
    # divide calculation only divides when matrix_ex != 0 but when matrix_ex = 0 , 0 is outputted
    return angle


# calling the two function of electric field strength and angle for the different data lists
e_field_strength = find_e_strength(EX_datalist, EY_datalist)
e_field_angle = find_e_angle(EX_datalist, EY_datalist)


def interp_efield(desired_y, inputlist):
    """
    param desired_y = desired y between 0 - 5 m , on the grid of electric field strength values
    param inputlist = The electric field strength list input
    returns the row that the desired y corresponds to, which has been interpolated
    """
    # finding the percentage of the file at which the desired y value occurs
    percent_of_file = desired_y / 5.0
    # the index at which the desired y is then found
    desired_index = 101 * percent_of_file
    # Then the lower bound of this index is found, in case it is between 2 indexes
    rounded_index = int(math.floor(desired_index))
    # Following line gets the two indexes either side of the desired value, subtracts them and
    # multiplies it by the percentage difference between the floor value and the actual desired index
    # The lower bound + value between the two indexes is outputted
    percentage = (inputlist[rounded_index + 1] - inputlist[rounded_index]) * abs(desired_index - rounded_index)
    return percentage + inputlist[rounded_index]


efieldyvalues = interp_efield(0.5, e_field_strength)
x_values = np.arange(0, 5, (5 / 101))  # X values are generated between 0 - 5 m to limit the plot range
plt.figure()  # initialising figure
ax1 = plt.axes(xscale='log', yscale='linear')  # Assigning figure subplot region
ax1.plot(x_values, efieldyvalues, 'r-*', label='Electric field strength at y = 0.5m')
ax1.set_xticks([1,2,3,4,5])
ax1.set_xlim((1,5))
locatorscalar = AutoMinorLocator(5)
loglocator = LogLocator(base=10, numticks=10, subs="auto")
ax1.xaxis.set_minor_formatter(NullFormatter())
ax1.yaxis.set_minor_formatter(NullFormatter())
ax1.xaxis.set_minor_locator(loglocator)
ax1.yaxis.set_minor_locator(locatorscalar)
# Adding labels and Legend
ax1.set_xlabel("Distance (m)", fontsize=15)
ax1.set_ylabel("Electric field strength (V/m) ", fontsize=15)
ax1.legend(numpoints=1, loc='upper center', bbox_to_anchor=(0.72, 1.1), fancybox=True, shadow=True, ncol=5)
# Customising Ticks
ax1.tick_params(axis="both", which="major", labelsize=15, color="b", width=1, length=5, labelcolor="black")
ax1.tick_params(axis='both', which='minor', right='false', width=0.7, size=2, length=2)

# Setting grid
ax1.grid(True, which='major', ls='--')


def save_file(filename, array, header, format):
    """
    param filename = name of the file you want to save
    param array = data to be written into file
    param header = header to be placed at the top of file
    param format = Allows for the format of the data to be specified
    returns nothing , file is saved locally with given data and header
    """
    np.savetxt(filename, array, fmt=format, header=header)


# saving both files with headers and converting angles into degrees
save_file("Deg_grid.txt", np.degrees(e_field_angle), "E field angle in uniform X Y grid", "%-6.2f")
save_file("Etot_grid.txt", e_field_strength, "E field strength in uniform X Y grid", "%-12.5e")
print("Output files saved")
# Showing plot
plt.tight_layout()
plt.show()
