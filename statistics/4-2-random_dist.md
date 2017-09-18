[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> The PMF and CDF distributions for the random numbers were plotted, and the solution has been included as PNG files in the parent folder. The following code was used:
```
import thinkstats2
import random
import thinkplot

rndm = [int(random.random()*1000) for x in range(0,1000)]
print(rndm)

pmf = thinkstats2.Pmf(rndm, label='PMF of Random Numbers')
cdf=thinkstats2.Cdf(rndm, label='CDF of Random Numbers')

thinkplot.Pmf(pmf)
thinkplot.show(xlabel='Number',ylabel='pmf',axis=[0,1000,0,0.5])
thinkplot.Cdf(cdf)
thinkplot.show(xlabel='Number',ylabel='cdf')
``` 
