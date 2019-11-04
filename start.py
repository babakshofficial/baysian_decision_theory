from dataset_reader import reading
from prior import calculate_prior
from gaussian_distribution import *
import numpy as np
import matplotlib.pyplot as plot
from ML import *
from MAP import *
from Bayes import *
from confusion_matrix import *

attr = ['Age','Year of operation','Positive axillary nodes','Survival']
cost_matrix = [[0,2],[1,0]]
binary_dataset = reading('haberman.data',',','int')
multi_class_dataset = reading('Data_User_Modeling_Dataset.txt','\t','float')

#----------------------------------------------------
# for Binary Classification
# we classify the dataset to #2 Classes
# based on Survival Status.
# Survival Status == 1, belongs to ones_class,
# Survival Status == 2, belongs to twos_class
#----------------------------------------------------

ones_class = []
twos_class = []
total_binary_without_labels = []
binary_labels = []

# adding data to appropriate class list

for item in binary_dataset:
    if item[3] == 1:
        ones_class.append(item[0:3])
    elif item[3] == 2:
        twos_class.append(item[0:3])
    total_binary_without_labels.append(item[0:3])
    binary_labels.append(item[3])

# this is a dictionary data type for store
# data based on Binary Classification

binary_class_dict = {}

# calculate and add each Binary class priors
# to the dictionary
binary_class_dict.update({'first_prior':calculate_prior(len(ones_class), len(binary_dataset))})
binary_class_dict.update({'second_prior':calculate_prior(len(twos_class), len(binary_dataset))})

# calculate and add each Binary class Covariance
# matrices to the dictionary
binary_class_dict.update({'first_covMat': np.cov(np.array(ones_class).T)})
binary_class_dict.update({'second_covMat': np.cov(np.array(twos_class).T)})

# calculate and total Binary class Covariance
# matrices to the dictionary
binary_class_dict.update({'covMat': np.cov(np.array(total_binary_without_labels).T)})

# calculate and add each Binary class mean
# vectors to the dictionary
binary_class_dict.update({'first_mean': np.mean(np.array(ones_class).T, 1)})
binary_class_dict.update({'second_mean': np.mean(np.array(twos_class).T, 1)})

# calculate and add total Binary class mean
# vectors to the dictionary
binary_class_dict.update({'mean': np.mean(np.array(total_binary_without_labels).T, 1)})

binary_likelihood = []
for item in total_binary_without_labels:
    tmp = []
    tmp.append(d_dim_calculate(item,
                               3,
                               binary_class_dict['first_mean'],
                               binary_class_dict['first_covMat']))
    tmp.append(d_dim_calculate(item,
                               3,
                               binary_class_dict['second_mean'],
                               binary_class_dict['second_covMat']))
    binary_likelihood.append(tmp)

binary_ML_labels = []
binary_MAP_labels = []
binary_BAYES_labels = []

for item in binary_likelihood:
    binary_ML_labels.append(calculate_binary_ML_test(item))
    binary_MAP_labels.append(calculate_binary_MAP_test(binary_class_dict['first_prior'],
                                                       binary_class_dict['second_prior'],
                                                       item))
    binary_BAYES_labels.append(calculate_binary_BAYES_test(cost_matrix,
                                                           binary_class_dict['first_prior'],
                                                           binary_class_dict['second_prior'],
                                                           item))
print('Binary')
print(binary_labels)
print(binary_ML_labels)
print(binary_MAP_labels)
print(binary_BAYES_labels)
print_diffrences(binary_labels, binary_ML_labels, binary_BAYES_labels, binary_MAP_labels)
print('ML')
print(make_binary_confusion_matrix(binary_labels, binary_ML_labels))
print('MAP')
print(make_binary_confusion_matrix(binary_labels, binary_MAP_labels))
print('BAYES')
print(make_binary_confusion_matrix(binary_labels, binary_BAYES_labels))

#----------------------------------------------------
# for multi-class classification
# we can separate the data to four distinct classes
# actually the identifier for each class is the last
# field of a row(record) in second data set
# first_class: last field == 1,
# second_class: last field == 2,
# third_class: last field == 3,
# fourth_class: last field == 4
#----------------------------------------------------

first_class = []
second_class = []
third_class = []
fourth_class = []
total_multi_class_without_labels = []
multi_class_labels = []

# adding data to appropriate class list

for item in multi_class_dataset:
    if item[5] == 1:
        first_class.append(item[0:5])
    elif item[5] == 2:
        second_class.append(item[0:5])
    if item[5] == 3:
        third_class.append(item[0:5])
    elif item[5] == 4:
        fourth_class.append(item[0:5])
    total_multi_class_without_labels.append(item[0:5])
    multi_class_labels.append(item[5])

print('Multi Class')

# this is a dictionary data type for store
# data based on multi-class Classification

multi_class_dict = {}

# calculate and add each multi-class priors
# to the dictionary
multi_class_dict.update({'first_prior':calculate_prior(len(first_class), len(multi_class_dataset))})
multi_class_dict.update({'second_prior':calculate_prior(len(second_class), len(multi_class_dataset))})
multi_class_dict.update({'third_prior':calculate_prior(len(third_class), len(multi_class_dataset))})
multi_class_dict.update({'fourth_prior':calculate_prior(len(fourth_class), len(multi_class_dataset))})

# calculate and add each multi-class Covariance
# matrices to the dictionary
multi_class_dict.update({'first_covMat': np.cov(np.array(first_class).T)})
multi_class_dict.update({'second_covMat': np.cov(np.array(second_class).T)})
multi_class_dict.update({'third_covMat': np.cov(np.array(third_class).T)})
multi_class_dict.update({'fourth_covMat': np.cov(np.array(fourth_class).T)})

# calculate and add each multi-class mean
# vectors to the dictionary
multi_class_dict.update({'first_mean': np.mean(np.array(first_class).T,1)})
multi_class_dict.update({'second_mean': np.mean(np.array(second_class).T,1)})
multi_class_dict.update({'third_mean': np.mean(np.array(third_class).T,1)})
multi_class_dict.update({'fourth_mean': np.mean(np.array(fourth_class).T,1)})

# calculate and add total multi-class mean
# vectors to the dictionary
multi_class_dict.update({'mean': np.mean(np.array(total_multi_class_without_labels).T,1)})

# calculate and add total multi-class Covariance
# matrices to the dictionary
multi_class_dict.update({'covMat': np.cov(np.array(total_multi_class_without_labels).T)})

multi_class_likelihood = []
for item in total_multi_class_without_labels:
    tmp = []
    tmp.append(d_dim_calculate(item,
                               5,
                               multi_class_dict['first_mean'],
                               multi_class_dict['first_covMat']))
    tmp.append(d_dim_calculate(item,
                               5,
                               multi_class_dict['second_mean'],
                               multi_class_dict['second_covMat']))
    tmp.append(d_dim_calculate(item,
                               5,
                               multi_class_dict['third_mean'],
                               multi_class_dict['third_covMat']))
    tmp.append(d_dim_calculate(item,
                               5,
                               multi_class_dict['fourth_mean'],
                               multi_class_dict['fourth_covMat']))
    multi_class_likelihood.append(tmp)

# for item in multi_class_likelihood:
#     print(calculate_multi_class_MAP_test(multi_class_dict['first_prior'],
#                                          multi_class_dict['second_prior'],
#                                          multi_class_dict['third_prior'],
#                                          multi_class_dict['fourth_prior'],
#                                          item))

multi_class_ML_labels = []
multi_class_MAP_labels = []
multi_class_BAYES_labels = []

for item in multi_class_likelihood:
    multi_class_ML_labels.append(calculate_multi_class_ML_test(item))
    multi_class_MAP_labels.append(calculate_multi_class_MAP_test(multi_class_dict['first_prior'],
                                                                 multi_class_dict['second_prior'],
                                                                 multi_class_dict['third_prior'],
                                                                 multi_class_dict['second_prior'],
                                                                 item))
    multi_class_BAYES_labels.append(calculate_multi_class_BAYES_test(cost_matrix,
                                                                     multi_class_dict['first_prior'],
                                                                     multi_class_dict['second_prior'],
                                                                     multi_class_dict['third_prior'],
                                                                     multi_class_dict['second_prior'],
                                                                     item))
print(multi_class_labels)
print(multi_class_ML_labels)
print(multi_class_MAP_labels)
print(multi_class_BAYES_labels)
print_diffrences(multi_class_labels,
                 multi_class_ML_labels,
                 multi_class_BAYES_labels,
                 multi_class_MAP_labels)
print('ML')
print(make_multi_class_confusion_matrix(multi_class_labels, multi_class_ML_labels))
print('MAP')
print(make_multi_class_confusion_matrix(multi_class_labels, multi_class_MAP_labels))
print('BAYES')
print(make_multi_class_confusion_matrix(multi_class_labels, multi_class_BAYES_labels))







