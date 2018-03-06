# coding: utf-8
# This file is part of ExoPlex - a self consistent planet builder
# Copyright (C) 2017 - by the ExoPlex team, released under the GNU
# GPL v2 or later.


#**********************************************************************#
'''
'''
#**********************************************************************#



import os
import sys
import numpy as np
import matplotlib.pyplot as plt
# hack to allow scripts to be placed in subdirectories next to burnman:
if not os.path.exists('ExoPlex') and os.path.exists('../ExoPlex'):
    sys.path.insert(1, os.path.abspath('..'))
    

import run as r


#Use inputs python file to call exoplex
# this creates an array of planet model data that you may use
# to plot or output files
#**NOTE: ENTER FILENAME WITHOUT .py**
# inputs_1 asks exoplex to model one planet. 

Planets = r.exoplex('inputs_1')


#all model data is now in Planets. Lets call some plotting functions

#our first output will be a plot against the PREM (Dziewonski & Anderson 1981)




