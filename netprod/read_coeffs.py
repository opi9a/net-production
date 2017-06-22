# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:04:03 2017

@author: GRoberta
"""

from openpyxl import load_workbook
import pandas as pd

def get_coeffs(wb, names_list):
    '''Returns a dictionary with data from named ranges specified by names_list
    from the xls passed as wb'''

    # First load up the data - all named ranges    
    raw_dict = {}
    for name in names_list:
        raw_dict[name] = list(wb.defined_names[name].destinations)[0]

    # Now put them in a dictionary
    coeffs = {}
    for coeff in raw_dict: #must be more elegant way to iterate thru this dictionary
        sheet, rng = raw_dict[coeff]
        ws = wb[sheet]
        vals = []

        # iterate through the range if it's more than one value, otherwise just take the single value
        if type(ws[rng]) is tuple:
            for cell in ws[rng]:
                vals.append(cell[0].value)
        else:
            vals.append(cell[0].value)
        
        coeffs[coeff] = vals
    
    return coeffs

def make_pdseries(in_dict):
    '''Turns a dictionary into a pandas Series'''
    ser = pd.Series()
    # populate by appending to the empty series.  Note index of tuples
    for key in in_dict:
        for i,datum in enumerate(in_dict[key]):
            ser = ser.append(pd.Series({(key,i):datum}))
    # now just turn the index into a proper multi-index
    ser.index = pd.MultiIndex.from_tuples(ser.index)
    return ser


if __name__=='__main__':
    # USAGE
    # First load in the workbook (data only, i.e. not formulas)
    wb = load_workbook('data/wsi_v0.1.31.xlsx', data_only=True)
    
    # Make the list of coefficient sets - must be the same as in the xls
    names_list = ['Prod_MCS_coeffs',
                  'Prod_PCS_coeffs',
                  'Prod_prod_coeffs',
                  'Prod_wagepcm_M_byage',
                  'Prod_wagepcm_F_byage',
                  'on_costs']
    
    # Finally run it
    coeff_ser = make_pdseries(get_coeffs(wb, names_list))
    