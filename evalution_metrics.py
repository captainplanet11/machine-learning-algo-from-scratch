# classification_Accuracy

#accuracy= correct predictions*100/total predictions
def accuracy_metric(actual,predicted):
    correct = 0 
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct+=1
    return correct/float(len(actual)) *100.0

actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,0,0,0,1,0,1,1,1]
accuracy = accuracy_metric(actual, predicted)
print(accuracy)

# calculate the confusion matrix
def confusion_matrix(actual,predicted):
    unique = set(actual)
    matrix = [list() for x in range(len(unique))]
    for i in range(len(unique)):
        matrix[i] = [0 for x in range(len(unique))]
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i 
    for i in range(len(actual)):
        x =lookup[actual[i]]
        y = lookup[predicted[i]]
        matrix[y][x] += 1
        return unique,matrix

#mean absolute error
def mae_metric(actual,predicted):
    sum_error = 0.0
    for  i in range(len(actual)):
        sum_error += abs(predicted[i] -actual[i])
    return sum_error /float(len(actual))
    