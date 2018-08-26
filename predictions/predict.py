import pandas as pd
import matplotlib
import numpy as np

def pre_process(file):
    df = pd.read_csv(file)
    print(df.head(10))
    return df.head(1)

def plot_graph(df):
    X = df['Year'].values
    Y = df['GDP'].values
    print(X,Y)
    return 'ad'