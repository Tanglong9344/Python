# python module 'pickle'
# write objects to a file persistently

# import cPickle
import pickle

# write
fileName = 'objectFile.txt'  # file that objects will be written
objs = ['Apple', 'Banana', True, 666]
file = open(fileName, 'wb')
pickle.dump(objs, file)
del objs
file.close()

# read
file = open(fileName, 'rb')
objs = pickle.load(file)
print('objs: ', objs)
