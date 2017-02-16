import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import collections
import scipy.stats as stats

# Part 1
"""
mean = 0
variance = 1
sigma = np.sqrt(variance) # this is the standard deviation
x = np.linspace(-3,3,100)
plt.plot(x, mlab.normpdf(x,mean,sigma))

plt.show()

#Part 2

testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)

print(c)

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.items():
  print("The frequency of number %s is %s" % (k, (float(v) / count_sum)*100))
"""

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)

# calculate the number of instances in the list
count_sum = sum(c.values())

for k,v in c.items():
  print("The frequency of number %s is %s%%" % (k, (float(v) / count_sum)*100))

#Part 3
plt.boxplot(x)
#plt.show()
plt.savefig('boxplot.png')

plt.hist(x, histtype='bar')
#plt.show()
plt.savefig('histo.png')

plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
#plt.show() #this will generate the first graph
plt.savefig('normalqq.png')

plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
#plt.show() #this will generate the second graph
plt.savefig('uniformqq.png')