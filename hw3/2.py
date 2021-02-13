import numpy as np
import math
sigma=1
mu_d_list = []
rpt = 5000

for d in range(1,51,1):
	mu_d = 0
	for r in range(rpt):
		g = np.random.normal(0,1,d)
		mu_d += math.sqrt(np.sum(g**2))
	avg_mu_d = mu_d / rpt
	mu_d_list.append( abs(avg_mu_d-math.sqrt(d))/avg_mu_d )

import matplotlib.pyplot as plt
d = np.linspace(1,50,50)
plt.plot(d,mu_d_list)
plt.xlabel('d')
plt.ylabel(r'$\frac{\left|{\mu_d-\sqrt{d}}\right|}{\mu_d}$')
plt.show()