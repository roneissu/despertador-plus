import matplotlib.pyplot as plt
import numpy as np
adct = np.arange(0, 1e6)
t1 = 27504
t2 = 26435
t3 = -1000

var1 = ((((adct/8) - ((t1*2))) * ((t2)) /2048))

var2 = ((adct/131072) - (t1/8192))*((adct/131072) - (t1/8192))*(t3)

eq = (var1 + var2)/5120


val = (((((519888>>3) - ((t1<<1))) * ((t2)) >> 11)) + ((519888/131072) - (t1/8192))*((519888/131072) - (t1/8192))*(t3))/5120

var11 = ((((adct/8) - ((1*2))) * ((1)) /2048))

var21 = ((adct/131072) - (1/8192))*((adct/131072) - (1/8192))*(1)

eq2 = (var11 + var21)/5120

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(adct, eq)
# ax.plot(adct, eq2)
ax.plot([519888], [val], 'ro')



plt.show()