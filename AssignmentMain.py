def open_file(filename):  # type_string -> List[str]
    f = open(filename, "r")
    input_data = f.readlines()
    f.close()
    return input_data

EX_dataraw = open_file("Ex_grid.txt")
EY_dataraw = open_file("Ey_grid.txt")


def strip_data(inputlist):
    columnlist = []
    for k in range(len(inputlist)):
        for i in range(len(inputlist[k].split())):
            columnlist.append([])
            columnlist[i].append(float(inputlist[k].split()[i]))
    return columnlist


EX_datalist = strip_data(EX_dataraw[1:])
print(EX_datalist[0][60])
print(EX_dataraw[61].split()[0])