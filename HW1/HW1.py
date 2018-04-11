# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 23:54:24 2018

@author: s110024
"""

from skimage import io
import numpy as np
import os

def loading(dirs):

    trainMatrix = np.array([], dtype=np.float64)
    trainBelong = np.array([])
    testMatrix = np.array([], dtype=np.float64)
    testBelong = np.array([])
    countOfPeople = 0
    dirs = os.getcwd()
    for i in range(1, 40):
        if i == 14:
            continue
        file = os.path.join(dirs, 'CroppedYale', 'yaleB%02d' % i, '*.pgm')
        imgs = io.imread_collection(file)
        imgs = np.array(imgs, dtype=np.float64)
        
        countOfPeople = len(imgs)
        
        for j in range(0, 35):
            if len(trainMatrix) is 0:
                trainMatrix = imgs[j].flatten()
            else:
                trainMatrix = np.vstack((trainMatrix, imgs[j].flatten()))
                
            if len(trainBelong) is 0:
                trainBelong = [i]
            else:
                trainBelong = np.concatenate((trainBelong, [i]))
        #print(trainMatrix.shape)
            
        for j in range(35, countOfPeople):
            if len(testMatrix) is 0:
                testMatrix = imgs[j].flatten()
            else:
                testMatrix = np.vstack((testMatrix, imgs[j].flatten()))
                
            if len(testBelong) is 0:
                testBelong = [i]
            else:
                testBelong = np.concatenate((testBelong, [i]))
                
    return trainMatrix, trainBelong, testMatrix, testBelong
            
        
trainMatrix, trainBelong, testMatrix, testBelong = loading(os.getcwd())
trainCount = np.size(trainMatrix, 0)
testCount = np.size(testMatrix, 0)
print("TrainCount: %d" % trainCount)
print("TestCount: %d" % testCount)

correctSAD = 0;
correctSSD = 0;

for test in range(testCount):
    minSAD, minSSD, AIndex, SIndex = -1, -1, -1, -1
    for train in range(trainCount):
        distance = testMatrix[test] - trainMatrix[train]
        SAD = np.sum(np.abs(distance))
        if SAD < minSAD or minSAD == -1:
            minSAD = SAD
            AIndex = train
            
        SSD = np.sum(distance**2)
        if SSD < minSSD or minSSD == -1:
            minSSD = SSD
            SIndex = train
            
    if testBelong[test] == trainBelong[AIndex]:
        correctSAD += 1
    if testBelong[test] == trainBelong[SIndex]:
        correctSSD += 1
    
print("correctSAD: %d" % correctSAD)
print("correctSSD: %d" % correctSSD)
    
print("SAD: %5f%%" %(correctSAD/testCount*100))
print("SSD: %5f%%" %(correctSSD/testCount*100))
