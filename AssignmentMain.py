

def open_file(filename):  # Opens file and reads it, returning a list of the lines and closes the file
    f = open(filename, "r")
    input_data = f.readlines()
    f.close()
    return input_data


# calling the open file function
EX_dataraw = open_file("Ex_grid.txt")
EY_dataraw = open_file("Ey_grid.txt")


def get_columns(inputlist):  # opens the list of lines, splits spaces, adds them to a list, outputs a list of line lists
    columns_list = []
    for line in inputlist:
        columns_list.append([float(x) for x in line.split()])
    return columns_list


EX_datalist = get_columns(EX_dataraw[1:])
print(EX_datalist)
column1 = [x[0] for x in EX_datalist]
print(column1)
