# --------------
#Importing header files
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.weightstats import ztest
from statsmodels.stats.weightstats import ztest
from scipy.stats import chi2_contingency

import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

# Critical Value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1


#Reading file
data=pd.read_csv(path)

#Code starts here

data_sample = data.sample(n=sample_size,random_state=0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()
margin_of_error = z_critical*(sample_std/math.sqrt(sample_size))
confidence_interval = (sample_mean-margin_of_error,sample_mean+margin_of_error)
true_mean = data['installment'].mean()
#print(confidence_interval[0])
 
if (true_mean >= confidence_interval[0]) and(true_mean <=confidence_interval[1]):
   print( " is in the range")
else :
   print("is outside the given range.")


#Different sample sizes to take
sample_size1=np.array([20,50,100])
#Code starts here
fig ,axes = plt.subplots(nrows = 3 , ncols = 1)
for i in range(len(sample_size1)):
   m=[]
   for j in range(1000):
       a1=data['installment'].sample(n=sample_size1[i])
       m.append(a1.mean())
   mean_series= pd.Series(m)
   axes[i].plot(mean_series)

data['int.rate']=(data['int.rate'].str[:-1].astype(float))/100
#data.head(2)
z_statistic_1 , p_value_1 = ztest(data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative='larger')
print(z_statistic_1,p_value_1)
 
if p_value_1<0.05:
   print("reject null hypothesis")
else:
   print("Accept null hypothesis")

z_statistic_2 , p_value_2 = ztest(data[data['paid.back.loan']=='No']['installment'],data[data['paid.back.loan']=='Yes']['installment'])
print(z_statistic_2,p_value_2)
if p_value_2<0.05:
  print("reject null hypothesis")
else:
  print("Accept null hypothesis")

#Critical value
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                     df = 6)   # Df = number of variable categories(in purpose) - 1
 
#Code starts here
yes= data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()
observed = pd.concat([yes.transpose(),no.transpose()],axis=1,keys= ['Yes','No'])
chi2, p, dof, ex = chi2_contingency(observed)
if chi2 > critical_value:
   print("reject the null hypothesis since the two distributions are the same")
else:
   print("null hypothesis cannot be rejected")




