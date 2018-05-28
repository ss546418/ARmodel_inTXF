import os
import sys

import pandas as pd
import numpy as np

##import statsmodels.formula.api as smf
##import statsmodels.tsa.api as smt
##import statsmodels.api as sm
##import scipy.stats as scs
##from arch import arch_model

import matplotlib.pyplot as plt


data=pd.read_csv('MXF_20min.txt')


data['r']=(data['C']-data['C'].shift(1))/data['C'].shift(1)
print(data)
