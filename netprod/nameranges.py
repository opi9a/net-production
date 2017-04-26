# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:04:03 2017

@author: GRoberta
"""

from openpyxl import load_workbook
from openpyxl.workbook import defined_name

def get_named_ranges(target, names):
    
    wb = load_workbook(target)
    out_dict = {}
    for name in names:
        out_dict[name] = list(wb.defined_names[name].destinations)[0]
    return out_dict

#filetarget = '../Copy of Wider Societal Impacts - tools and reference estimates v0.1.3 - temp - adding models.xlsm'
#inlist = ['PCS_coeffs', 'MCS_coeffs']

#if __name__ == '__main__':
#    import sys
#    get_named_ranges(sys.argv[0:2])