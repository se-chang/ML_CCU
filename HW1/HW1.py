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
        if i is 14:
            continue
        file = os.path.join(dirs, 'CroppedYale', 'yaleB%02d' % i, '*.pgm')
        imgs = io.ImageCollection(file)
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
        print(trainMatrix.shape)
            
        for j in range(35, countOfPeople):
            if len(testMatrix) is 0:
                testMatrix = imgs[j].flatten()
            else:
                testMatrix = np.vstack((testMatrix, imgs[j].flatten()))
                
            if len(testBelong) is 0:
                testBelong = [i]
            else:
                testBelong = np.vstack((testBelong, i))
                
    return trainMatrix, trainBelong, testMatrix, testBelong
            
        
loading(os.getcwd())