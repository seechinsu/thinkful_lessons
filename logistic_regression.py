import pandas as pd
import statsmodels.api as sm

cleandata = pd.read_csv('C:\Users\Seech\PycharmProjects\\thinkful\\thinkful_lessons\loansData_clean.csv')

cleandata['IR_TF'] = map(lambda s: 1 if(s>=0.12) else 0, cleandata['Interest.Rate'])
cleandata['constint'] = 1.0

print(cleandata)[0:10]
#print(cleandata[cleandata['Interest.Rate'] == 0.1]) # should all be True

ind_vars =