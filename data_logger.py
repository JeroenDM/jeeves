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
    def __init__(self, path, filename, header, log_interval=9):
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
        
        # initialize cache
        self._reset_cache()
        
        # keep last logging time
        self.i = 0
        self.di_max = log_interval
    
    def log(self, *arg, **kwarg):
        if self.i >= self.di_max:
            self.i = 0
            self._append_to_cache(*arg, **kwarg)
            self._write_to_file()
            self._reset_cache()
        else:
            self.i += 1
            self._append_to_cache(*arg, **kwarg)
    
    def flush_cache(self):
        self._write_to_file()
        self._reset_cache()     
    
    def _write_to_file(self):
        self.cache.to_csv(self.p, columns=self.h, index=False, mode='a', header=False)
        self._reset_cache()
    
    def _append_to_cache(self, *arg, **kwarg):
        if not len(kwarg) == self.n_col:
            raise ValueError("Wrong number of variables")
        data = {}
        for key in self.h:
            data[key] = kwarg[key]
        try:
            df = pd.DataFrame(data)
        except ValueError:
            # solution for error
            # ValueError: If using all scalar values, you must pass an index
            df = pd.DataFrame(data, index=[0])
        self.cache = self.cache.append(df, ignore_index=True)
    
    def _reset_cache(self):
        self.cache = pd.DataFrame(columns=self.h)

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
    dl.flush_cache()
    end = time.time()
    #print(end - start)
    res = pd.read_csv('data.csv')
    print("Data from csv file (first rows):")
    print(res.head())