import pandas as pd

df = pd.read_csv('full_ds_classification.csv')

train = []
test = []
valid = []
# iterate over the rows
for index, row in df.iterrows():
    file_name = row['file']
    label = row['label']
    file_set = row['set']
    if file_set == 'Train':
        train.append(file_name)
    elif file_set == 'Test':
        test.append(file_name)
    elif file_set == 'Valid':
        valid.append(file_name)
    else:
        raise ValueError('Unknown file set: {}'.format(file_set))

    # make 3 text files for each set
with open("train_list.txt", 'w') as f:
    for item in train:
        f.write("%s\n" % item)
with open("test_list.txt", 'w') as f:
    for item in test:
        f.write("%s\n" % item)
with open("valid_list.txt", 'w') as f:
    for item in valid:
        f.write("%s\n" % item)

bb_images = []
bb_df = pd.read_csv('BBox_List_2017.csv')
for index, row in bb_df.iterrows():
    file_name = row['Image Index']
    bb_images.append(file_name)

with open("bb_list.txt", 'w') as f:
    for item in bb_images:
        f.write("%s\n" % item)