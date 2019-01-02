# -*- coding: utf-8 -*-
import matplotlib.pylab as pyl
import numpy as npy

#hist
data3 = npy.random.normal(10.0,1.0,10000)
# pyl.hist(data3)
# pyl.show()
data4 = npy.random.random_integers(1,25,1000)
# pyl.hist(data4)
sty = npy.arange(2,19,2)
# pyl.hist(data4,sty)
# pyl.show()
# pyl.subplot(2,2,2)#行，列，当前区域
# pyl.show()
pyl.subplot(2,2,1)

pyl.subplot(2,2,2)
pyl.subplot(2,1,2)
pyl.show()