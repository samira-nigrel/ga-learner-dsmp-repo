# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank= pd.read_csv(path,sep=",")

#Code starts here
#Step 1
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)

#Step 2
banks=bank.drop(columns='Loan_ID')
print(banks.isnull().sum())
bank_mode=banks.mode().iloc[0]
banks.fillna(bank_mode,inplace=True)
print(banks.isnull().sum())

#Step 3
avg_loan_amount=pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values=['LoanAmount'])

#Step 4
loan_approved_se=banks.loc[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y'),['Loan_Status']].count()
loan_approved_nse=banks.loc[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y'),['Loan_Status']].count()
percentage_se=(loan_approved_se*100)/614
percentage_se=percentage_se[0]
percentage_nse=(loan_approved_nse*100)/614
percentage_nse=percentage_nse[0]


#Step 5
loan_term = banks['Loan_Amount_Term'].apply(lambda x : int(x) / 12)
big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)

#Step 6
columns_to_show = ['ApplicantIncome', 'Credit_History']
loan_groupby=banks.groupby(['Loan_Status'])
 
loan_groupby=loan_groupby[columns_to_show]
 
# Check the mean value
mean_values=loan_groupby.agg([np.mean])
 
print(mean_values)

#Code Ends



