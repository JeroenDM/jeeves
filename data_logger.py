#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:58:24 2017

@author: jeroen
"""

import pandas as pd
import numpy as np
import os.path

# TODO fix order of reading variablse in log function
# FIXED: use the columns=... argument every time you create a dataframe
# TODO logging of a path (list) not possible yet
# TODO caching to avoid to many file operations?

class DataLogger:
    def __init__(self, path, filename, header):
        # setup and check file path and name
        self.p = path + filename
        if os.path.exists(self.p):
            raise ValueError("File already exists, use another name, not " + self.p)
        # dataframe parameters
        self.h = header
        self.n_col = len(header)
        
        # write initial header
        df = pd.DataFrame(columns=header)
        df.to_csv(self.p, index=False)
    
    def log(self, *arg, **kwarg):
        if not len(kwarg) == self.n_col:
            raise ValueError("Wrong number of variables")
        data = {}
        for key in self.h:
            data[key] = kwarg[key]
        df = pd.DataFrame(data)
        df.to_csv(self.p, columns=self.h, index=False, mode='a', header=False)

if __name__ == "__main__":
    print("------------------------")
    print("test DataLogger")
    print("------------------------")
    import time
    dl = DataLogger('', 'data.csv', ['b', 'a'])
    
    start = time.time()
    for i in range(10):
        ai = 7
        bi = np.random.rand(5)
        dl.log(a=ai, b=bi)
        dl.log(a=ai, b=bi)
    end = time.time()
    print(end - start)
    res = pd.read_csv('data.csv')
    print(res.head())