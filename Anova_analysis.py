# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 07:04:41 2020

@author: Ritwick
"""
#
#    ANOVA analysis
#
import pandas as pd
#
#  read sample data and perform Anova analysis.
#
#  Read input Excel file
#  Each sample/group is a column with first row containing
#  the sample name. The data is assumed to be in Sheet1
#  each group is expected to have the same sample size
#
#
def Anv_GroupMean(df):
    #
    #  Compute mean of each group
    #
    grp_mean = []
    for column in df:
        grp_mean.append(df[column].mean())
    return grp_mean
#
def Anv_GrandMean(grp_mean, ngrp):
    #
    #  Compute grand mean
    # 
    sum_grp_mean = sum(grp_mean)
    grand_mean = sum_grp_mean/ngrp
    return grand_mean
#
def Anv_SSB(grp_mean, grand_mean, ngrp):
    #
    #  Compute Sum of squares between groups
    #   
    SSB = 0.0
    for i in range(ngrp):
        SSB += ndata*(grp_mean[i] - grand_mean)**2
    return SSB
#
def Anv_SSW(df, grp_mean, ndata):
    #
    #  Compute Sum of squares within groups
    #
    SSW = 0.0
    iC = 0
    for column in df:
        for j in range(ndata):
            SSW += (df.loc[j,column] - grp_mean[iC])**2
        iC += 1
    return SSW
#
def Anv_SST(df,ndata,grand_mean):
    #
    #  Compute Sum of squares Total 
    #
    SST = 0.0
    for column in df:
        for j in range(ndata):
            SST += (df.loc[j,column] - grand_mean)**2
    return SST
#
#################################################################    
#
#    Main body of execution steps
#    1. REad Sample data from spreadsheet into a DataFrme
#    2. Compute group mean for samples
#    3. Compute grand mean for all samples
#    4. Compute SSB
#    5. Compute SSW
#    6. Compute SST (This is for cross checking: SST = SSB+SSW )
#    7. Compute MSB and MSW
#    8. Compute F_statistics
#################################################################
#
u_str = input('enter Excel filename: ')

df = pd.read_excel(u_str, sheet_name = 'Sheet1')  

ndata, ngrp = df.shape    # Sample size and number of samples/groups (returned as tuple)
grp_mean = Anv_GroupMean(df)
grand_mean = Anv_GrandMean(grp_mean, ngrp)
SSB = Anv_SSB(grp_mean, grand_mean, ngrp)
SSW = Anv_SSW(df, grp_mean, ndata)
SST = Anv_SST(df, ndata, grand_mean)
#
#  Compute F_stat
#    
MSB = SSB / (ngrp -1)
MSW = SSW / ((ndata*ngrp) - ngrp)
F_Stat = MSB/MSW
#
#  Output statistics
#
print()
print('######### ANOVA analysis output ##########')
print()
print('Number of smaples/group       (k)    : ', ngrp)
print('Sample size per group         (n)    : ', ndata)
print('Population size               (N)    : ', ndata*ngrp)
print('Grand mean                           : ',grand_mean)
print('Sum of squares between groups (SSB)  : ',SSB)
print('Sum of squares within groups  (SSW)  : ',SSW)
print('Sum of squares total          (SST)  : ',SST)
print('Mean square between groups    (MSB)  : ',MSB)
print('Mean square within groups     (MSW)  : ',MSW)
print('F_Stat                               : ',F_Stat)


