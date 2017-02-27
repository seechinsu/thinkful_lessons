import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData['Interest.Rate'] = map(lambda s: round(float(s.replace('%',''))/100,4),loansData['Interest.Rate'])
loansData['Loan.Length'] = map(lambda s: int(s.replace('months','')),loansData['Loan.Length'])
loansData['FICO.Score'] = map(lambda s: int(s[0]),map(lambda s: str(s).split('-'),loansData['FICO.Range']))

#print loansData['Interest.Rate'][0:5]
#print loansData['Loan.Length'][0:5]
#print loansData['FICO.Score'][0:5]

print loansData[0:5]

#plt.figure()
#p = loansData['FICO.Score'].hist()
#plt.show()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()