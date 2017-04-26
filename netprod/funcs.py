import netprod
import numpy as np

def func_a():
    '''here is function A'''
    print("function A executing")
    return 1

def paid_prod(age=95, qol=0.9, debug=False):
    '''X this new docstring here'''
#    print(netprod.prod_model.iloc[0])
#    print('version 1')
    print("name: ", __name__)
    print('productivity is ', productivity(age, qol, debug))
    return 1

def productivity(age, qol, debug):
    '''returns productivity, as % of time worked, for given age and QoL'''
    print('in productivity function')
    MCS = (netprod.prod_model.loc["MCS_age_div_10"] * (age/10)) \
          + (netprod.prod_model.loc["MCS_EQ5D"] * qol) \
            + netprod.prod_model.loc["MCS_const"]

    PCS = (netprod.prod_model.loc["PCS_age_div_10"] * (age/10)) \
        + (netprod.prod_model.loc["PCS_EQ5D"] * qol) \
        + netprod.prod_model.loc["PCS_const"]
    
    prod_sum = ((netprod.prod_model.loc["prod_age_div_10"] * (age/10)) 
                + (netprod.prod_model.loc["prod_age_div_10_sq"] * ((age/10)**2)) 
                + (netprod.prod_model.loc["prod_MCS_div_10"] * (MCS/10)) 
                + (netprod.prod_model.loc["prod_MCS_div_10_sq"] * ((MCS/10)**2)) 
                + (netprod.prod_model.loc["prod_PCS_div_10"] * (PCS/10)) 
                + (netprod.prod_model.loc["prod_PCS_div_10_sq"] * ((PCS/10)**2)) 
                + netprod.prod_model.loc["prod_const"])
    
    productivity = np.exp(prod_sum)/(1+np.exp(prod_sum))
    
    return productivity