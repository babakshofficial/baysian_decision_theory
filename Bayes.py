def calculate_binary_BAYES_test(cost_matrix, pc1, pc2, likes):
    likeC1, likeC2 = likes[0], likes[1]
    landa_11 = cost_matrix[0][0]
    landa_12 = cost_matrix[0][1]
    landa_21 = cost_matrix[1][0]
    landa_22 = cost_matrix[1][1]
    first_greatness = likeC1 / likeC2
    second_greatness = ((landa_12 - landa_22) * pc2) / ( (landa_21 - landa_11) * pc1)
    if first_greatness > second_greatness:
        return 1
    return 2

def calculate_multi_class_BAYES_test(cost_matrix, pc1, pc2, pc3, pc4, likes):
    likeC1, likeC2, likeC3, likeC4 = likes[0], likes[1], likes[2], likes[3]
    greatness1 = 0
    greatness2 = 0
    greatness = 0
    landa_11 = cost_matrix[0][0]
    landa_12 = cost_matrix[0][1]
    landa_21 = cost_matrix[1][0]
    landa_22 = cost_matrix[1][1]
#   winner between C1 , C2
    first_greatness = likeC1 / likeC2
    second_greatness = ((landa_12 - landa_22) * pc2) / ( (landa_21 - landa_11) * pc1)
    if first_greatness > second_greatness:
        greatness1 = 1
    else:
        greatness1 = 2

#   winner between C3 , C4
    first_greatness = likeC3 / likeC4
    second_greatness = ((landa_12 - landa_22) * pc4) / ((landa_21 - landa_11) * pc3)
    if first_greatness > second_greatness:
        greatness2 = 3
    else:
        greatness2 = 4

#   winner between C1 , C3
    if greatness1 == 1 and greatness2 == 3:
        first_greatness = likeC1 / likeC3
        second_greatness = ((landa_12 - landa_22) * pc3) / ((landa_21 - landa_11) * pc1)
        if first_greatness > second_greatness:
            greatness = 1
        else:
            greatness = 3

#   winner between C1 , C4
    elif greatness1 == 1 and greatness2 == 4:
        first_greatness = likeC1 / likeC4
        second_greatness = ((landa_12 - landa_22) * pc4) / ((landa_21 - landa_11) * pc1)
        if first_greatness > second_greatness:
            greatness = 1
        else:
            greatness = 4

#   winner between C2 , C3
    elif greatness1 == 2 and greatness2 == 3:
        first_greatness = likeC1 / likeC4
        second_greatness = ((landa_12 - landa_22) * pc3) / ((landa_21 - landa_11) * pc2)
        if first_greatness > second_greatness:
            greatness = 2
        else:
            greatness = 3

#   winner between C2 , C4
    elif greatness1 == 2 and greatness2 == 4:
        first_greatness = likeC2 / likeC4
        second_greatness = ((landa_12 - landa_22) * pc4) / ((landa_21 - landa_11) * pc2)
        if first_greatness > second_greatness:
            greatness = 2
        else:
            greatness = 4
    return greatness