#!/usr/bin/env python
# coding: utf-8

# CONFIDENCE INTERVAL FUNDAMENTALS WITH ONE DATASET

# In[36]:


#import packages
import math as m
import numpy as np
import scipy.stats as st
#from scipy import stats as st

#create dataset
dataset = []
for i in range(-50,51,1):
    dataset.append(i)

print(dataset)

#descriptive statistics
len_dataset = len(dataset)
mean_dataset = np.mean(dataset)
std_dev_dataset = np.std(dataset)
std_err_dataset = std_dev / (m.sqrt(len_dataset))

print('')
print('length of dataset : ', len_dataset)
print('mean of dataset : ', mean_dataset)
print('standard deviation of dataset : ', std_dev_dataset)
print('standard error of dataset : ', std_err_dataset)

#z-table : known population variance, sample size > 30, gauss distribution
#st.norm.ppf(.975) #from library 1.959963984540054
#st.norm.ppf(.025) #from library -1.960063984540054

#z-table : known population variance, sample size > 30, gauss distribution
z_value = 1.96 #please check z-table value for %95 or @=0.05

#margin of error
moe = z_value * std_err_dataset
print ('margin of error : ', moe)

ci = (mean_dataset-moe, mean_dataset+moe)
print('confidence interval for %95 : ', ci)


# CONFIDENCE INTERVAL FOR TWO DEPENDENT DATASETS

# In[47]:


#packages
import math as m
import numpy as np
import scipy.stats as st
#from scipy import stats as st

#datasets
patient_before_weight = [103.68, 110.68, 119.05, 101.75, 91.69, 112.03, 88.84, 105.18, 110.37, 120.99]
patient_after_weight = [92.87, 101.58, 105.66, 96.18, 86.97, 105.90, 80.56, 97.00, 99.27, 107.44]
print ('before weight : ', patient_before_weight)
print('')
print('*********************************************')
print('')
print ('after weight : ', patient_after_weight)
print('*********************************************')
print('')

#diffenrence between before and after
patient_difference_weight = list(np.array(patient_after_weight) - np.array(patient_before_weight))
print ('differences weights : ', patient_difference_weight)
print('*********************************************')
print('')

#descriptive statistics
len_dataset = len(patient_difference_weight)
mean_dataset = np.mean(patient_difference_weight)
std_dev_dataset = np.std(patient_difference_weight)
std_err_dataset = std_dev_dataset / (m.sqrt(len_dataset))

print('')
print('length of dataset : ', len_dataset)
print('mean of dataset : ', mean_dataset)
print('standard deviation of dataset : ', std_dev_dataset)
print('standard error of dataset : ', std_err_dataset)
print('*********************************************')
print('')

#t-table : unknown population variance, sample size < 30, gauss distribution
#t_value = st.t.ppf(1-0.05, 30) #n=30, @=0.05, one-sided
#t_value = st.t.ppf(1-0.025, 30) #n=30, @=0.05, two-sided
#print('t-value two-sided: ', t_value)
#print('*********************************')
#print('')
t_value = 2.262 #please check t-table value for %95 or @=0.05

#margin of error
moe = t_value * std_err_dataset
print ('margin of error : ', moe)
print('*********************************************')
print('')

#confidence interval
ci = (mean_dataset-moe, mean_dataset+moe)
print('confidence interval for %95 : ', ci)

#RESULT
#This program is successful.
#Because people lost weight: [-11.194220586792486, -6.971779413207518].
#This result for interval %95.


# You want to calculate confidence interval for two independent dataset, you should apply formula.
