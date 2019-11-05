def calculate_binary_MAP_test(pc1, pc2, likes):
    likeC1, likeC2 = likes[0], likes[1]
    first_greatness = likeC1 / likeC2
    second_greatness = pc2 / pc1
    if first_greatness > second_greatness:
        return 1
    return 2

def calculate_multi_class_MAP_test2(pc1, pc2, pc3, pc4, likes):
    greatness1 = 0
    greatness2 = 0
    greatness = 0
    likeC1, likeC2, likeC3, likeC4 = likes[0], likes[1], likes[2], likes[3]

#   the winner between C1 and C2
    first_greatness = likeC1 / likeC2
    second_greatness = pc2 / pc1
    if first_greatness > second_greatness:
        greatness1 = 1
    else:
        greatness1 = 2

#   the winner between C3 and C4
    first_greatness = likeC3 / likeC4
    second_greatness = pc4 / pc3
    if first_greatness > second_greatness:
        greatness2 = 3
    else:
        greatness2 = 4

#   the winner between C1 and C3
    if greatness1 == 1 and greatness2 == 3:
        first_greatness = likeC1 / likeC3
        second_greatness = pc3 / pc1
        if first_greatness > second_greatness:
            greatness = 1
        else:
            greatness = 3

#   the winner between C1 and C4
    elif greatness1 == 1 and greatness2 == 4:
        first_greatness = likeC1 / likeC4
        second_greatness = pc4 / pc1
        if first_greatness > second_greatness:
            greatness = 1
        else:
            greatness = 4

#   the winner between C2 and C3
    elif greatness1 == 2 and greatness2 == 3:
        first_greatness = likeC2 / likeC3
        second_greatness = pc3 / pc2
        if first_greatness > second_greatness:
            greatness = 2
        else:
            greatness = 3

#   the winner between C2 and C4
    elif greatness1 == 2 and greatness2 == 4:
        first_greatness = likeC2 / likeC4
        second_greatness = pc4 / pc2
        if first_greatness > second_greatness:
            greatness = 2
        else:
            greatness = 4

#   the winner between C1, C2, C3 and C4
    return greatness

def calculate_multi_class_MAP_test(pc1, pc2, pc3, pc4, likes):
    greatness1 = 0
    greatness2 = 0
    greatness = 0
    likeC1, likeC2, likeC3, likeC4 = likes[0], likes[1], likes[2], likes[3]

#   the winner between C1 and C2
    first_greatness = likeC1 * pc1
    second_greatness = pc2 * likeC2
    if first_greatness > second_greatness:
        greatness1 = 1
    else:
        greatness1 = 2

#   the winner between C3 and C4
    first_greatness = likeC3 * pc3
    second_greatness = pc4 * likeC4
    if first_greatness > second_greatness:
        greatness2 = 3
    else:
        greatness2 = 4

#   the winner between C1 and C3
    if greatness1 == 1 and greatness2 == 3:
        first_greatness = likeC1 * pc1
        second_greatness = pc3 * likeC3
        if first_greatness > second_greatness:
            greatness = 1
        else:
            greatness = 3

#   the winner between C1 and C4
    elif greatness1 == 1 and greatness2 == 4:
        first_greatness = likeC1 * pc1
        second_greatness = pc4 * likeC4
        if first_greatness > second_greatness:
            greatness = 1
        else:
            greatness = 4

#   the winner between C2 and C3
    elif greatness1 == 2 and greatness2 == 3:
        first_greatness = likeC2 * pc2
        second_greatness = pc3 * likeC3
        if first_greatness > second_greatness:
            greatness = 2
        else:
            greatness = 3

#   the winner between C2 and C4
    elif greatness1 == 2 and greatness2 == 4:
        first_greatness = likeC2 * pc2
        second_greatness = pc4 * likeC4
        if first_greatness > second_greatness:
            greatness = 2
        else:
            greatness = 4

    result = [pc1*likeC1, pc2*likeC2, pc3*likeC3, pc4*likeC4]
#   the winner between C1, C2, C3 and C4
    if greatness == (result.index(max(result)) + 1):
        return greatness
    return esult.index(max(result)) + 1