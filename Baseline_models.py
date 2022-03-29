from random import randrange
#generate random predictions
def random_algorithm(test,train):
    output_values = [row[-1] for row in train ]
    unique = list(set(output_values))
    predicted = list()
    for row in test:
        index = randrange(len(unique))
        predicted .append(unique[index])
    return predicted


#zero rule algorithm for classification

def zero_rule_algorithm_classification(train, test):
    output_values =[row[-1] for row in train]
    prediction = max(set(output_values),key =output_values.count)
    predicted =[prediction for i in range(len(test))]
    return predicted
#zero rule algorithm for regression
def zero_rule_algorithm_regression(train,test):
    output_values = [row[-1] for row in train]
    prediction = sum(output_values)/float(len(output_values))
    predicted =[prediction for i in range(len(test))]
    return predicted
    