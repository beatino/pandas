# Pandas - Binning

import os
import numpy as np
import pandas as pd

def binning(data_vec, cut_points, labels=None):
    #Define min and max values:
    minval = data_vec.min()
    maxval = data_vec.max()
    #create list by adding min and max to cut_points  
    break_points = [minval] + cut_points + [maxval]
    #if no labels provided, use default labels 0 ... (n-1)
    if not labels:
        labels = range(len(cut_points)+1)
    #Binning cut function of pandas
    colBin = pd.cut(data_vec,bins=break_points,labels=labels,include_lowest=True)
    return colBin
    

cut_points = [0.3,0.5,0.7]
labels = ["low","medium","high","very high"]
data = pd.DataFrame(np.random.rand(10,1), columns=['Value'])
data['K'] = binning(data["Value"], cut_points,labels)
data