from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
import pandas as pd
import numpy as np

data = pd.read_csv('spambase.data').as_matrix()


def run():
    np.random.shuffle(data)

    X = data[:, :48]
    Y = data[:, -1]

    Xtrain = X[:-100, ]  # starts from the beginning, and ends at (n-100)
    Ytrain = Y[:-100, ]

    Xtest = X[-100:, ]  # starts from (n-100), and ends at n
    Ytest = Y[-100:, ]

    model = BernoulliNB()
    model.fit(Xtrain, Ytrain)
    global b
    b += model.score(Xtest, Ytest)

    model = GaussianNB()
    model.fit(Xtrain, Ytrain)
    global g
    g += model.score(Xtest, Ytest)

    model = MultinomialNB()
    model.fit(Xtrain, Ytrain)
    global m
    m += model.score(Xtest, Ytest)


if __name__ == '__main__':
    b = 0.0
    g = 0.0
    m = 0.0
    for x in range(0, 10):
        run()


    print("BernouliiNB: ", b/10, "MultinomialNB: ", m/10, "GaussianNB: ", g/10)
