import numpy as np

def calculate(list):
  if(len(list) != 9):
    raise ValueError('List must contain nine numbers.')

  outPutDict = {}
  list = np.array(list)
  print(list)
  list = list.reshape((3,3))
  print(list)
  print(list.mean(0))
  print(list.mean(1))
  print(list.mean())
  meanString = []
  meanString.append(list.mean(0).tolist())
  meanString.append(list.mean(1).tolist())
  meanString.append(list.mean())
  print(meanString)
  outPutDict["mean"] = meanString
  print(outPutDict)
  print(list.var(0))
  print(list.var(1))
  print(list.var())
  varString = []
  varString.append(list.var(0).tolist())
  varString.append(list.var(1).tolist())
  varString.append(list.var())
  outPutDict["variance"] = varString
  print(outPutDict)
  sdString = []
  sdString.append(list.std(0).tolist())
  sdString.append(list.std(1).tolist())
  sdString.append(list.std())
  outPutDict["standard deviation"] = sdString
  print(outPutDict)
  maxString = []
  maxString.append(list.max(0).tolist())
  maxString.append(list.max(1).tolist())
  maxString.append(list.max())
  outPutDict["max"] = maxString
  print(outPutDict)
  minString = []
  minString.append(list.min(0).tolist())
  minString.append(list.min(1).tolist())
  minString.append(list.min())
  outPutDict["min"] = minString
  print(outPutDict)
  sumString = []
  sumString.append(list.sum(0).tolist())
  sumString.append(list.sum(1).tolist())
  sumString.append(list.sum())
  outPutDict["sum"] = sumString
  print(outPutDict)





  return outPutDict