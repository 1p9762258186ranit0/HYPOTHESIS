# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:23:13 2023

@author: lenovo
"""
1) Problem

File: Cutlets.csv

import pandas as pd
import matplotlib.pylab as plt
import statsmodels.stats.descriptivestats as sd
from statsmodels.stats import weightstats as stests

Problem Statement:-

H0:-There is no significant differnce between diameter of two cutlet unit..
H1:-There is significant differnce between diameter of two cutlet unit..


# LOAD THE DATASET
df=pd.read_csv("C:/Users/lenovo/OneDrive/Documents/assignments/hypothesis,z-t test/hypothesis/dataset/Cutlets.csv")

#DATA CLEANING

df1=df.iloc[0:35]

#CHECK NORMALITY TEST..USING SHAPIRO NORMALITY TEST

stats.shapiro(df1['Unit A'])
pvalue=0.3199819028377533>0.05

stats.shapiro(df1['Unit B'])
pvalue=pvalue=0.5224985480308533>0.05

FROM ABOVE == WE CONCLUDE THAT..DATA ARE NORMAL

#AGAIN CHECK NORMALITY BY,GRAPHICAL REPRESENTATION
stats.probplot(df1['Unit B'],plot=pylab,dist='norm')
stats.probplot(df1['Unit B'],plot=pylab,dist='norm')

#CHECK VARAIENCE EQUAL OR NOT

stats.levene(df1['Unit A'],df1['Unit B'])
pvalue=0.4176162212502553>0.05
FROM ABOVE-WE CONCLUDE THAT,VARIENCE ARE EQUAL

#SO FINALLY WE USE:--2 SAMPLE 'T-TEST' FOR EQUAL VARIENCE

stats.ttest_ind(df1['Unit A'],df1['Unit B'])

pval=0.4722>0.05
p high null fly....select null hypothesis(H0)

Conclusion==There is no significant differnce between diameter of two cutlet unit..







2)Problem

File: LabTAT.csv


import pandas as pd
import scipy
from scipy import stats


Problem Statement:
    
H0:-There is NO difference in the (TAT) of reports of the laboratories on their preferred list. 
H1=There is difference in the (TAT) of reports of the laboratories on their preferred list. 


#LOAD THE DATASET
df=pd.read_csv("C:/Users/lenovo/OneDrive/Documents/assignments/hypothesis,z-t test/hypothesis/dataset/lab_tat_updated.csv")

#EDA
#Rename the columns

df=df.rename(columns={'Laboratory_1':'lab1','Laboratory_2':'lab2','Laboratory_3':'lab3','Laboratory_4':'lab4'})
df.info()

#CHECK WHETHER DATA IS NORMAL OR NOT USING SHAPIRO TEST

stats.shapiro(df.lab1) 
pvalue=0.42317795753479004>0.05

stats.shapiro(df.lab2) 
pvalue=0.8637524843215942>0.05)
              
stats.shapiro(df.lab3)
pvalue=0.06547004729509354>0.05

stats.shapiro(df.lab4) 
pvalue=0.6618951559066772>0.05

HO=Data are Normal
H1=Data are not Normal
P high null fly..Data are normal(for all column)..Accept Ho

#Check Varience

stats.levene(df['lab1'],df['lab2'],df['lab3'],df['lab4'])
HO=Equal Varience
H1=Not Equal Varience

pvalue=0.38107781677304564>0.05...Accept Ho

#APPLY ONE WAY ANOVA TEST
stats.f_oneway(df['lab1'],df['lab2'],df['lab3'],df['lab4'])
pvalue=2.143740909435053e-58<0.05
Reject Ho..
Accept H1..


conclusion=(H1)There is difference in the (TAT) of reports of the laboratories on their preferred list. 






3)Problem
    
File = Buyer Ratio.csv



import pandas as pd
import scipy
from scipy import stats
from scipy.stats import chi2_contingency


Problem Statement:-

H0:- Male and female are similar
H1:- Male and female are not similar 

#LOAD THE DATSET

df=pd.read_csv("C:/Users/lenovo/OneDrive/Documents/assignments/hypothesis,z-t test/hypothesis/dataset/BuyerRatio.csv")

#DFINING THE TABLE
data=[[50,142,131,70],[435,1523,1356,750]]

#APPLY THE CHI_CONTINGENCY TEST

stat,p,dof,expected=scipy.stats.chi2_contingency(data)

pvalue= 0.6603094907091882>0.05
Hence,we accept null hypothesis(HO)

Conclusion=Male and Female ratio are similar across regions





4)Problem
              
File: CustomerOrderForm.mtw
              
HO=Defective varies
H1=Defective Not varies

#Load the dataset

df1=pd.read_csv("C:/Users/lenovo/OneDrive/Documents/excler assignments/hypothesis/Costomer+OrderForm.csv")

#Data Organizing

India=df1.India.value_counts()
Phillippines=df1.Phillippines.value_counts()
Indonesia=df1.Indonesia.value_counts()
Malta=df1.Malta.value_counts()

#AFTER ANALYZING ABOVE,,DFEINING THE TABLE
data=[[280,271,267,269],[20,29,33,31]]

#APPLY CHI2
stat,p,dof,expected = scipy.stats.chi2_contingency(data)

pvalue=0.2771020991233135>0.05
ACCPET HO..

Conclusion=Defective Varies(ACCEPT HO)