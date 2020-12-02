---
layout: post
title: "Latin Hypercube Sampling"
date: 2019-03-15
---

In a recent research project, modeling cell shape diversity arising from complex Rho GTPase dynamics (preprint available on the [bioRxiv]), I needed to generate a nearly uniform random sample of 5 dimensional parameter space.

A quick and easy way to do this is using [Latin hypercube sampling].

[bioRxiv]:https://www.biorxiv.org/content/10.1101/561373v1
[Latin hypercube sampling]:https://en.wikipedia.org/wiki/Latin_hypercube_sampling

The basic idea is that of a Latin square. A square grid containing sample positions is a Latin square if and only if there is only one sample in each row and in each column:
<p align="center">
  <img width="300px" src="{{ site. url }}/images/lhs.png">
</p>

It's super easy to cook up in MATLAB with the built in function `lhsdesign`. Since I'm working on my python skills, I thought I would code up a LHS generator in python and share it here.

[lhsdesign]:https://www.mathworks.com/help/stats/lhsdesign.html

```python
import numpy as np
import matplotlib.pyplot as plt

#makes a Latin Hyper Cube sample
#returns a matrix X of size n by p
#of a LHS of n values on each of p variables
#for each column of X, the n values are randomly
#chosen from the midpoints of from each interval
#(0,1/n), (1/n,2/n), ..., (1-1/n,1)

def lhssample(n=10,p=2):
    x = np.random.uniform(size=[n,p])
    for i in range(0,p):
        x[:,i] = (np.argsort(x[:,i])+0.5)/n
    return x

x = lhssample(20,2)
```
