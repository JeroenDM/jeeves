#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:46:35 2017

@author: jeroen
"""

import sys
import os
from data_logger import DataLogger

# process command line input
if len(sys.argv) > 1:
    N_max = int(sys.argv[1])
    if len(sys.argv) > 2:
        name = sys.argv[2]
    else:
        name = 'prime_numbers_1.csv'
else:
    print("Using default value N_max = 100")
    print("Optional command line argument to change this")
    N_max = 100
    name = 'prime_numbers_1.csv'

# setup other default parameters
var_names = ['i', 'pn']
path = os.getcwd() + '/'
logger = DataLogger(path, name, var_names, log_interval=99)

def is_prime(n):
    for ni in range(2, n):
        if (n % ni) == 0:
            return False
    return True

index = 0
for i in range(N_max):
    if is_prime(i):
        print(index, i)
        logger.log(i=index, pn=i)
        index += 1
logger.flush_cache()