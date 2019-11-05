def calculate_class_accuracy(real, model, class_number):
    length = len(real)
    true_predictions = 0
    for i in range(length):
        if int(real[i]) == int(model[i]) == class_number:
            true_predictions = true_predictions + 1
    return true_predictions / length
