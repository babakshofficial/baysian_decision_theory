def reading(path,splitter,kind):

    # matrix initialization
    total_matrix = []
    vector = []

    # reading each line
    file = open(path, "r")

    # creating the data Matrix
    for i in file:
        vector = []
        for j in i.split(splitter):
            if kind == 'int':
                vector.append(int(j))
            else:
                vector.append(float(j))
        total_matrix.append(vector)

    return total_matrix

