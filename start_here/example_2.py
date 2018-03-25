# coding: utf-8
# This file is part of ExoPlex - a self consistent planet builder
# Copyright (C) 2017 - by the ExoPlex team, released under the GNU
# GPL v2 or later.


#**********************************************************************#
'''
This script deatils how a user can make models of various composition
along a range of masses. The following functions do not utilize the 
input file in example_1.py. Instead, the user will input the composition
and mass ranges as python lists in the following format:
[start, stop, step].


'''
#**********************************************************************#



import os
import sys
import numpy as np
import matplotlib.pyplot as plt
# hack to allow scripts to be placed in subdirectories next to burnman:
if not os.path.exists('ExoPlex') and os.path.exists('../ExoPlex'):
    sys.path.insert(1, os.path.abspath('..'))
    
import pdb
import run 


#####

'''
function: single_grid(**kwargs)


create a data grid for a planet of some mass.
vary BULK Fe/Mg, Si/Mg*, and water mass fraction to calculate the
radius of a planet as a function of mass and composition.


*core mass fraction is calculated from bulk inputs

returns:
.dat file will appear in Solutions/Grids folder. 

kwargs:
mass     = x  #mass of planet in Earth masses
femg     = [start, stop, step] range of elemental ratio of Fe to Mg in the mantle
simg     = [start, stop, step] range of elemental ratio of Si to Mg in the mantle
h2o      = [start, stop, step] (optional) range of water mass fraction
filename = 'file.dat'          (optional) string. name of file to be stored in Solutions/Grids                       
'''

#####

FeMg = [0.2, 0.3,0.1]
SiMg = [0.2, 0.4,0.1]
wt_h2o = [0.0, 0.0, 0.1]

run.single_grid(mass = 1.0,femg = FeMg, simg = SiMg)

sys.exit()



#####

'''
function: single_grid_cmf(**kwargs)

create a data grid for a planet of some mass
vary MANTLE Fe/Mg, Si/Mg, water mass fraction, and the CMF (core mass fraction)
This is good to make if there is not a premade grid for this 
specific range of mantle composition
or core mass fraction. 

returns:
.dat file will appear in Solutions/Grids folder. 

kwargs:
mass     = x  #mass of planet in Earth masses
femg     = [start, stop, step] range of elemental ratio of Fe to Mg in the mantle
simg     = [start, stop, step] range of elemental ratio of Si to Mg in the mantle
cmf      = [start, stop, step] core mass fraction range
h2o      = [start, stop, step] (optional) range of water mass fraction
filename = 'file.dat'          (optional) string. name of file to be stored in Solutions/Grids                       
'''

#####

FeMg = [0.2, 0.3,0.1]
SiMg = [0.2, 0.4,0.1]
CMF  = [0.3, 0.5,0.1]
wt_h2o = [0.0, 0.0, 0.1]

run.single_grid_cmf(mass = 1.0,femg = FeMg, simg = SiMg, cmf = CMF)




####
'''
function: mvr_grid()

create data grid for a range of compositions and masses. Each composition gets a file
with mass and resulting radius.

Output will appear in Solutions/Grids folder and optional Mass vs radius
plot will display on screen.

kwargs:
mass      = [start, stop, step]               mass of planets in Earth masses
femg      = [start, stop, step]               range of elemental ratio of Fe to Mg in the mantle
simg      = [start, stop, step]               range of elemental ratio of Si to Mg in the mantle
cmf       = [start, stop, step]               core mass fraction range
h2o       = [start, stop, step]               (optional) range of water mass fraction
filenames = ['file1.dat', 'file2.dat']      (optional) name of file to plot from
plot      = True|False                      (optional) plot mass v radius for each composition?

'''
####


M    = [0.8, 1.0, 0.1]
FeMg = [0.1, 0.3,0.1]
SiMg = [0.2, 0.4,0.1]
CMF  = [0.3, 0.5,0.1]
wt_h2o = [0.0, 0.0, 0.1]
run.mvr_grid(mass = M ,femg = FeMg, simg = SiMg, cmf = CMF, plot=True)




####
'''
Plot Mass vs radius from grid 

kwargs:
filename = x                  (optional) name of file to plot from

'''
####


sys.exit()











