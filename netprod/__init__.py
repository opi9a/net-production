print('calling the __init__')
import pandas as pd
import os
print('imported pandas')
import netprod.funcs

# Read in the reference data to an object 

# First need to get the right path
dirpath = netprod.__file__.split("__init__")[0]

#
prod_model = pd.read_csv(dirpath + "data/paid_prod_model.csv", header=None, index_col=0, names=["value"])

