from scipy import stats
import collections
import pandas as pd

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)
#print loansData

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

print freq
print len(freq)
print max(freq, key=freq.get)
print max(freq.values())

#plt.figure()
#plt.bar(freq.keys(), freq.values(), width=1)
#plt.show()