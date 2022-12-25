import numpy as np

#Transform contonious data to discrete data for classific. applications by lables and thresholds
def classify(data,thresholds,labels):
    if len(thresholds)==len(labels)+1: return 4
    res=np.zeros(len(data),dtype=str)
    thresholds=np.sort(thresholds)
    for i in range (0,len(data)):
        for k in range (0,len(thresholds)):
            if data[i]<thresholds[k]:
                res[i]=labels[k][0]
                break
        if res[i]=='':
            if data[i]>thresholds[-1]:
                res[i]=labels[-1]
    return res
