import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import friedmanchisquare, wilcoxon
from scipy.stats import rankdata
from scipy import stats
import scikit_posthocs as sp
import statsmodels.stats.multitest as smt

#calculate ranks
def rank_cal(df):
    ranks= rankdata(df.to_numpy(), axis =1)
    ranks_d= len(ranks[0])+1-ranks
    print(df.columns)
    return np.mean(ranks_d, axis=0).round(3)

# conduct the Nemenyi post-hoc test
def nemenyi_test(df):
    p_values = sp.posthoc_nemenyi_friedman(df).round(3)
    p_sig = p_values < 0.05
    print(p_values)
    return p_sig