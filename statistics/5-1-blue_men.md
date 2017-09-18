[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> For the desired height range, the fraction of the US male population in the range is: 34.2%. The following code was used:
```
import thinkstats2
import scipy.stats

mu = 178
sigma = 7.7
normal_height_dist = scipy.stats.norm(loc=mu, scale=sigma)
cdf_height1 = normal_height_dist.cdf(177.8) 
cdf_height2 = normal_height_dist.cdf(185.4) 
print('The fraction of US male population in the low-high height range is:')
print(100*(cdf_height2-cdf_height1))
```
