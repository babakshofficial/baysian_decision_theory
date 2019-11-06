
# created by Babak Shahriari
# this class calculate each class accuracy based on
# the true predictions that the code made

def calculate_class_accuracy(real, model, class_number):
    length = len(real)
    true_predictions = 0
    total_classified_class = 0
    for i in range(length):
        if int(real[i]) == int(model[i]) == class_number:
            true_predictions = true_predictions + 1
        if int(real[i]) == class_number:
            total_classified_class = total_classified_class + 1
    return true_predictions / total_classified_class
