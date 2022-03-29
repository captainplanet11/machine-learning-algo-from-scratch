#split the dataset into train and test dataset

from random import seed
from random import randrange


def train_test_split(dataset , split = 0.60):
    train = []
    train_size = split*len(dataset)
    dataset_copy = list(dataset)
    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train,dataset_copy


# test train/test split
seed(1)
dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
train, test = train_test_split(dataset)
print(train)
print(test)