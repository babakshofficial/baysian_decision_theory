from dataset_reader import reading
from prior import calculate_prior
from gaussian_distribution import *
import numpy as np
from likelihood import *
import matplotlib.pyplot as plot

attr = ['Age','Year of operation','Positive axillary nodes','Survival']
cost_matrix = [[0,2],[1,0]]
binary_dataset = reading('haberman.data',',','int')
multi_class_dataset = reading('Data_User_Modeling_Dataset.txt','\t','float')

# for Binary Classification
# we classify the dataset to #2 Classes
# based on Survival Status.
# Survival Status == 1, belongs to ones_class,
# Survival Status == 2, belongs to twos_class

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
# values to the dictionary
binary_class_dict.update({'first_mean': np.mean(np.array(ones_class).T, 1)})
binary_class_dict.update({'second_mean': np.mean(np.array(twos_class).T, 1)})

# calculate and add total Binary class mean
# values to the dictionary
binary_class_dict.update({'mean': np.mean(np.array(total_binary_without_labels).T, 1)})

# create and store gaussian distribution in
# our binary class dictionary

binary_class_gauss = []
tmp = []
for item in ones_class:
    tmp.append(d_dim_calculate(item, 3, binary_class_dict['first_mean'], binary_class_dict['first_covMat']))
binary_class_dict.update({'first_gauss': tmp})

tmp = []
for item in twos_class:
    tmp.append(d_dim_calculate(item, 3, binary_class_dict['second_mean'], binary_class_dict['second_covMat']))
binary_class_dict.update({'second_gauss': tmp})

tmp = []
for item in total_binary_without_labels:
    tmp.append(d_dim_calculate(item, 3, binary_class_dict['mean'], binary_class_dict['covMat']))
binary_class_dict.update({'gauss': tmp})


# calculate and store likelihood for any class member
# into a list


binary_class_likelihood = []
for item in binary_dataset:
    tmp = calculate_binary_likelihood(4, binary_class_dict['first_prior'], binary_class_dict['second_prior'])
    binary_class_likelihood.append(tmp)



# for multi-class classification
# we can separate the data to four distinct classes
# actually the identifier for each class is the last
# field of a row(record) in second data set
# first_class: last field == 1,
# second_class: last field == 2,
# third_class: last field == 3,
# fourth_class: last field == 4

first_class = []
second_class = []
third_class = []
fourth_class = []
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
    multi_class_labels.append(item[5])

print('Multi Class')

# this is a dictionary data type for store
# data based on multi-class Classification

multi_class_dict = {}

# calculate and add each Binary class priors
# to the dictionary
multi_class_dict.update({'first_prior':calculate_prior(len(first_class), len(multi_class_dataset))})
multi_class_dict.update({'second_prior':calculate_prior(len(second_class), len(multi_class_dataset))})
multi_class_dict.update({'third_prior':calculate_prior(len(third_class), len(multi_class_dataset))})
multi_class_dict.update({'fourth_prior':calculate_prior(len(fourth_class), len(multi_class_dataset))})

# calculate and add each Binary class Covariance
# matrices to the dictionary
multi_class_dict.update({'first_covMat': np.cov(np.array(first_class).T)})
multi_class_dict.update({'second_covMat': np.cov(np.array(second_class).T)})
multi_class_dict.update({'third_covMat': np.cov(np.array(third_class).T)})
multi_class_dict.update({'fourth_covMat': np.cov(np.array(fourth_class).T)})

# calculate and add each Binary class mean
# values to the dictionary

multi_class_dict.update({'first_mean': np.mean(np.array(first_class).T,1)})
multi_class_dict.update({'second_mean': np.mean(np.array(second_class).T,1)})
multi_class_dict.update({'third_mean': np.mean(np.array(third_class).T,1)})
multi_class_dict.update({'fourth_mean': np.mean(np.array(fourth_class).T,1)})

#print(multi_class_dict)


multi_class_gauss = []

tmp = []
for item in first_class:
    tmp.append(d_dim_calculate(item,5,multi_class_dict['first_mean'],multi_class_dict['first_covMat']))

tmp = []
for item in second_class:
    tmp.append(d_dim_calculate(item,5,multi_class_dict['second_mean'],multi_class_dict['second_covMat']))

tmp = []
for item in third_class:
    tmp.append(d_dim_calculate(item,5,multi_class_dict['third_mean'],multi_class_dict['third_covMat']))

tmp = []
for item in fourth_class:
    tmp.append(d_dim_calculate(item,5,multi_class_dict['fourth_mean'],multi_class_dict['fourth_covMat']))









