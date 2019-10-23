from dataset_reader import reading

labels = ['Age','Year of operation','Positive axillary nodes','Survival']
cost_matrix = [[0,2],[1,0]]
print (reading('haberman.data'))