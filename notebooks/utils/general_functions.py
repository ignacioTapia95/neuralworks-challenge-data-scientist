import pandas as pd
import numpy as np

def woe(data, variable, target):
    
    df_temp = data.groupby([variable])[[target]].mean()
    WOE = np.log(df_temp[target] / (1-df_temp[target]+0.0000001))

    return WOE.to_dict()


def get_sign_stars(pvalue):
    
    if pvalue < 0.001:
        return '***'
    elif pvalue < 0.01:
        return '**'
    elif pvalue < 0.05:
        return '*'
    else:
        return ''