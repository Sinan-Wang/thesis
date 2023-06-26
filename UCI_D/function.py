from sklearn.metrics import f1_score, roc_auc_score
from imblearn.metrics import geometric_mean_score
from sklearn import metrics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def evaluation(y_tr,X_tr,y_va,X_va,model):
    #print("AUC training dataset:",roc_auc_score(y_tr, model.predict_proba(X_tr)[:,1]).round(3))
    #GOOD:0(N) BAD:1(POS)
    #TN FP
    #FN TP
    return roc_auc_score(y_tr, model.predict_proba(X_tr)[:,1]).round(3),\
           roc_auc_score(y_va, model.predict_proba(X_va)[:,1]).round(3),\
           metrics.precision_score(y_va, model.predict(X_va)).round(3),\
           metrics.recall_score(y_va, model.predict(X_va)).round(3),\
           geometric_mean_score(np.ravel(y_va), model.predict(X_va)).round(3),\
           f1_score(y_va, model.predict(X_va)).round(3),\
           metrics.confusion_matrix(y_va, model.predict(X_va))



def evaluation_nn(y_tr, X_tr, y_va,X_va, model):
    return roc_auc_score(y_tr, model.predict(X_tr)).round(3),\
           roc_auc_score(y_va, model.predict(X_va)).round(3),\
           metrics.precision_score(y_va, np.where(model.predict(X_va) >= 0.5, 1, 0)).round(3),\
           metrics.recall_score(y_va, np.where(model.predict(X_va) >= 0.5, 1, 0)).round(3),\
           geometric_mean_score(np.ravel(y_va), np.ravel(np.where(model.predict(X_va) >= 0.5, 1, 0))).round(3),\
           f1_score(y_va, np.where(model.predict(X_va) >= 0.5, 1, 0)).round(3),\
           metrics.confusion_matrix(y_va, np.where(model.predict(X_va) >= 0.5, 1, 0))

