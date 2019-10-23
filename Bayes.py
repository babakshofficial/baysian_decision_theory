from dataset_reader import reading

labels = ['Age','Year of operation','Positive axillary nodes','Survival']
cost_matrix = [[0,2],[1,0]]
dataset = reading('haberman.data')

# for Binary Classification
# we classify the dataset to #2 Classes
# based on Survival Status.


# for multi-class classification I try to
# seperate dataset[i]' and add each number to
# a seperate list to measure the length of each
# non-duplicate lists. I figured out the best list label for
# multi-class classification is 'Year Of Operation' with 12
# non-duplicate items.


