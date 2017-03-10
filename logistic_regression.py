import pandas as pd
import statsmodels.api as sm
import numpy as np

cleandata = pd.read_csv('C:\Users\Seech\PycharmProjects\\thinkful\\thinkful_lessons\loansData_clean.csv')

cleandata['IR_TF'] = map(lambda s: 1 if(s>=0.12) else 0, cleandata['Interest.Rate'])

#intrate = loansData['Interest.Rate']
irtf = cleandata['IR_TF']
loanamt = cleandata['Amount.Requested']
fico = cleandata['FICO.Score']

y = np.matrix(irtf).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1, x2])
ind_vars = sm.add_constant(x)

#print(cleandata)[0:10]
#print x
#print(ind_vars)

logit = sm.Logit(cleandata['IR_TF'], ind_vars)
result = logit.fit()
coeff = result.params
print(coeff)

