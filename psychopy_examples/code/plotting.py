import matplotlib.pyplot as plt
import numpy as np
# Many ways to do plotting (even within matplotlib)

# import seaborn to make nice clean plots
import seaborn as sb
# OR run this function to make XKCD-style plots
# but that isn't so effective on small plots like this
#plt.xkcd()

# create some made-up data
x = np.arange(0, 100)
y = np.random.rand(100)  # 100 random numbers

fig, ax = plt.subplots(2,2)

ax[0, 0].hist(y)
ax[0, 1].scatter(x, y)
ax[1, 0].boxplot(y)
ax[1, 1].loglog(x, y)

plt.show()