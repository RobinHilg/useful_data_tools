import numpy as np

#Removes outliers from data input given the outliers indices, returns cleaned data.
def outlierRemoval(data,outlierInd):
  data=np.delete(data,obj=outlierInd,axis=0)
  return data




#Inp data, output data cleared of meaningless features with 0 Variance and returns removed indices.
def meaninglessFeaturesRemoval(data):
  indices=np.zeros(0,dtype=int)
  for i in range (0,len(data[0,:])):
    if np.all(data[:,i]==data[0,i]): indices=np.append(indices,int(i))
  return np.delete(data,obj=indices,axis=1), indices
