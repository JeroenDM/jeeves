#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 14:46:35 2017

@author: jeroen
"""

#from data_logger import DataLogger
#
#var_names = ['i', 'pn']
#path = '/home/jeroen/Documents/gitlab/jeeves/'
#name = 'prime_numbers_1.csv'
#logger = DataLogger(path, name, var_names)

def is_prime(n):
    for ni in range(2, n):
        if (n % ni) == 0:
            return False
    return True

N_max = 100

for i in range(N_max):
    if is_prime(i):
        print(i)