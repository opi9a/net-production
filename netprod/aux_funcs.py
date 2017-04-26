# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:04:03 2017

@author: GRoberta
"""

from openpyxl import load_workbook
from openpyxl.workbook import defined_name

def get_named_ranges(target, names):
    '''Returns a dictionary with the locations of the named ranges 'names'
    in the target xls'''
    
    wb = load_workbook(target)
    out_dict = {}
    for name in names:
        out_dict[name] = list(wb.defined_names[name].destinations)[0]
    return out_dict

