from dataset_reader import reading
from prior import calculate_prior
import numpy as np

labels = ['Age','Year of operation','Positive axillary nodes','Survival']
cost_matrix = [[0,2],[1,0]]
dataset = reading('haberman.data')

# for Binary Classification
# we classify the dataset to #2 Classes
# based on Survival Status.
# Survival Status == 1, belongs to first_class,
# Survival Status == 2, belongs to second_class

first_class = []
second_class = []
for item in dataset:
    if item[3] == 1:
        first_class.append(item)
    elif item[3] == 2:
        second_class.append(item)

print("\n    Priors for Binary Classification")
binary_priors_dict = {}
binary_priors_dict.update({'first':calculate_prior(len(first_class), len(dataset))})
binary_priors_dict.update({'second':calculate_prior(len(second_class), len(dataset))})

print ("\nPrior for first Class with " + str(len(first_class)) + " data is " + str(binary_priors_dict['first']))
print ("\nPrior for second Class with " + str(len(second_class)) + " data is " + str(binary_priors_dict['second']))

print("\n    Covariance Matrices for Binary Classification")
print ("\nCovariance Matrix for first Class is \n" + str(np.cov(first_class)))
print ("\nCovariance Matrix for second Class is \n" + str(np.cov(second_class)))

print("\n    Mean Vectors for Binary Classification")
print ("\nMean Vector for first Class is " + str(np.mean(first_class)))
print ("\nMean Vector for second Class is " + str(np.mean(second_class)))



# for multi-class classification
# I try to seperate dataset[i]' and add each number to
# a seperate list to measure the length of each
# non-duplicate lists. I figured out the best list label for
# multi-class classification is 'Year Of Operation' with 12
# non-duplicate items.

year_of_operation = []
for item in dataset:
    if item[1] not in year_of_operation:
        year_of_operation.append(item[1])

# I use Dictionary in python for storing data

year_of_operation_dict = {}
for year in year_of_operation:
    temp_list = []
    for item in dataset:
        if item[1] == year:
            temp_list.append(item)

    year_of_operation_dict.update({year : temp_list})

print("\n    Priors for Multi-class Classification")
print("\nYear --   Prior")

for item in year_of_operation_dict:
    print(str(item) + "   --   " + str(calculate_prior(len(year_of_operation_dict[item]),len(dataset))))

print("\n    Covariance Matrices for Multi-class Classification")
for item in year_of_operation_dict:
    print("\nCovariance Matrix for " + str(item) + " is\n" + str(np.cov(year_of_operation_dict[item])))

print("\n    Mean Vectors for Binary Classification")
for item in year_of_operation_dict:
    print("\nMean Vector for " + str(item) + " is\n" + str(np.mean(year_of_operation_dict[item])))




