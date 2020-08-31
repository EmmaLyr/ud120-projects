from sklearn.naive_bayes import GaussianNB

def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    clf = GaussianNB()
    ### fit the classifier on the training features and labels
    return (clf.fit(features_train, labels_train))
    ### return the fit classifier


    ### your code goes here!

    
