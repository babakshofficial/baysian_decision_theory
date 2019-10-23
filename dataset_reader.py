def reading(path):

    # matrix initialization
    total_matrix = []
    vector = []

    # reading each line
    file = open(path, "r")

    # creating the data Matrix
    for i in file:
        vector = []
        for j in i.split(','):
            vector.append(int(j))
        total_matrix.append(vector)

    return total_matrix

