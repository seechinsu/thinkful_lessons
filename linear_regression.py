import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData['Interest.Rate'] = map(lambda s: round(float(s.replace('%',''))/100,4),loansData['Interest.Rate'])
loansData['Loan.Length'] = map(lambda s: int(s.replace('months','')),loansData['Loan.Length'])
loansData['FICO.Score'] = map(lambda s: int(s[0]),map(lambda s: str(s).split('-'),loansData['FICO.Range']))

#print loansData['Interest.Rate'][0:5]
#print loansData['Loan.Length'][0:5]
#print loansData['FICO.Score'][0:5]
#print loansData[0:5]

#plt.figure()
#p = loansData['FICO.Score'].hist()
#plt.show()

#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
#plt.show()

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1, x2])
X = sm.add_constant(x)
model = sm.OLS(y, X)

f = model.fit()
print f.params
print f.pvalues
print f.summary()

plt.scatter(x1, y)
plt.show()
