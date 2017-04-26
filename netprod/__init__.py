import pandas as pd
from netprod.funcs import *

# Read in the reference data to an object 

#  - first need to get the right path (current)
dirpath = netprod.__file__.split("__init__")[0]

#  - now read in the data to pandas dfs
prod_model = pd.read_csv(dirpath + "data/paid_prod_model.csv", header=None, index_col=0, names=["value"])
on_costs = pd.read_csv(dirpath + "data/on_costs.csv", header=None, index_col=0, names=["value"])
