# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)
#task1
p_a=len(df[df['fico']>700])/len(df)
p_b=len(df[df.purpose == 'debt_consolidation'])/len(df)
df1=df[df.purpose == 'debt_consolidation']
p_a_b=(len(df1[df1['fico']>700])/len(df1))
result=(p_a_b==p_a)
print(result)
#task2
prob_lp=len(df[df['paid.back.loan'] == 'Yes'])/len(df)
prob_cs=len(df[df['credit.policy'] == 'Yes'])/len(df)
new_df=df[df['paid.back.loan'] == 'Yes']
prob_pd_cs=len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)
bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)
#task3
df1=df[df['paid.back.loan'] == 'No']
df1.plot.bar(x='purpose')
#task4
inst_median=df["installment"].median()
inst_mean=df["installment"].mean()
df.hist(column="installment")
df.hist(column="log.annual.inc")
#Code starts here




