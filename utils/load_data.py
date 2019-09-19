import pandas as pd
import os
base_dir = os.path.dirname(os.path.dirname(__file__))


def load_regression():
    # load data
    train = pd.read_csv(os.path.join(base_dir, "data/Train_BigMartSales.txt"))
    test = pd.read_csv(os.path.join(base_dir, "data/Test_BigMartSales.txt"))
    return train, test

def load_classification():
    # load data
    train = pd.read_csv(os.path.join(base_dir, "data/titanic/train.csv"))
    test = pd.read_csv(os.path.join(base_dir, "data/titanic/test.csv"))
    return train, test