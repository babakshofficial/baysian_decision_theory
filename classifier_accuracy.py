def calculate_accuracy(confusion_matrix):
    True_values = 0
    total_values = 0
    for i in range(len(confusion_matrix)):
        for j in range(len(confusion_matrix)):
            if i == j:
                True_values = True_values + confusion_matrix[i][j]
            total_values = total_values + confusion_matrix[i][j]
    return True_values / total_values







