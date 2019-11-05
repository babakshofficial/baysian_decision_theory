def make_binary_confusion_matrix(real, model):
    length = len(real)
    # at class_mn, m is real and n is predicted
    # 1 for class label 1
    # 2 for class label 2
    class_11, class_12 = 0, 0
    class_21, class_22 = 0, 0

    # 11, 22
    for i in range(length):
        if int(real[i]) == 1 and int(model[i]) == 1:
            class_11 = class_11 + 1
        elif int(real[i]) == 2 and int(model[i]) == 2:
            class_22 = class_22 + 1
    # 12, 21
    for i in range(length):
        if int(real[i]) == 1 and int(model[i]) == 2:
            class_12 = class_12 + 1
        elif int(real[i]) == 2 and int(model[i]) == 1:
            class_21 = class_21 + 1

    return [[class_11, class_12],[class_21, class_22]]

def make_multi_class_confusion_matrix(real, model):
    length = len(real)
    # at class_mn, m is real and n is predicted
    # 1 for class label 1
    # 2 for class label 2
    # 3 for class label 3
    # 4 for class label 4
    class_11, class_12, class_13, class_14 = 0, 0, 0, 0
    class_21, class_22, class_23, class_24 = 0, 0, 0, 0
    class_31, class_32, class_33, class_34 = 0, 0, 0, 0
    class_41, class_42, class_43, class_44 = 0, 0, 0, 0

    # 11,22,33,44
    for i in range(length):
        if int(real[i]) == 1 and int(model[i]) == 1:
            class_11 = class_11 + 1
        if int(real[i]) == 2 and int(model[i]) == 2:
            class_22 = class_22 + 1
        if int(real[i]) == 3 and int(model[i]) == 3:
            class_33 = class_33 + 1
        if int(real[i]) == 4 and int(model[i]) == 4:
            class_44 = class_44 + 1

    # 12,13,14
    for i in range(length):
        if int(real[i]) == 1 and int(model[i]) == 2:
            class_12 = class_12 + 1
        if int(real[i]) == 1 and int(model[i]) == 3:
            class_13 = class_13 + 1
        if int(real[i]) == 1 and int(model[i]) == 4:
            class_14 = class_14 + 1

    # 21,23,24
    for i in range(length):
        if int(real[i]) == 2 and int(model[i]) == 1:
            class_21 = class_21 + 1
        if int(real[i]) == 2 and int(model[i]) == 3:
            class_23 = class_23 + 1
        if int(real[i]) == 2 and int(model[i]) == 4:
            class_24 = class_24 + 1

    # 31,32,34
    for i in range(length):
        if int(real[i]) == 3 and int(model[i]) == 1:
            class_31 = class_31 + 1
        if int(real[i]) == 3 and int(model[i]) == 2:
            class_32 = class_32 + 1
        if int(real[i]) == 3 and int(model[i]) == 4:
            class_34 = class_34 + 1

    # 41,42,43
    for i in range(length):
        if int(real[i]) == 4 and int(model[i]) == 1:
            class_41 = class_41 + 1
        if int(real[i]) == 4 and int(model[i]) == 2:
            class_42 = class_42 + 1
        if int(real[i]) == 4 and int(model[i]) == 3:
            class_43 = class_43 + 1

    return [[class_11, class_12, class_13, class_14],
            [class_21, class_22, class_23, class_24],
            [class_31, class_32, class_33, class_34],
            [class_41, class_42, class_43, class_44]]

def print_diffrences(real, ml, bayes, map):
    length = len(real)
    print('Real' + '\t' + 'ML' + '\t' + 'MAP' + '\t' + 'Bayes')
    for item in range(length):
        print(str(int(real[item])) + '\t' + str(int(real[item]) == ml[item]) + '\t' + str(int(real[item]) == map[item]) + '\t' + str(int(real[item]) == bayes[item]))