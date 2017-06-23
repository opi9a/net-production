import netprod
import numpy as np


def paid_prod(age=75, gen='F', qol=0.9, debug=False):
    '''X this new docstring here'''
    if gen=='F':
        wage = coeff_ser.Prod_wagepcm_F_byage[age]    
    else:
        wage = coeff_ser.Prod_wagepcm_M_byage[age]
    on_cost = coeff_ser.on_costs
    return productivity(age, qol, debug=False) * wage * (1 + on_cost)


def productivity(age, qol, debug=False):
    '''returns productivity, as % of time worked, for given age and QoL'''
    MCS = (coeff_ser.Prod_MCS_coeffs[0] * (age/10)) \
          + (coeff_ser.Prod_MCS_coeffs[1] * qol) \
            + coeff_ser.Prod_MCS_coeffs[2]

    PCS = (coeff_ser.Prod_PCS_coeffs[0] * (age/10)) \
          + (coeff_ser.Prod_PCS_coeffs[1] * qol) \
            + coeff_ser.Prod_PCS_coeffs[2]
    
    prod_sum = ((coeff_ser.Prod_prod_coeffs[0] * (age/10)) 
                + (coeff_ser.Prod_prod_coeffs[1] * ((age/10)**2)) 
                + (coeff_ser.Prod_prod_coeffs[2] * (MCS/10)) 
                + (coeff_ser.Prod_prod_coeffs[3] * ((MCS/10)**2)) 
                + (coeff_ser.Prod_prod_coeffs[4] * (PCS/10)) 
                + (coeff_ser.Prod_prod_coeffs[5] * ((PCS/10)**2)) 
                + coeff_ser.Prod_prod_coeffs[6])
    
    productivity = np.exp(prod_sum)/(1+np.exp(prod_sum))
    
    return productivity