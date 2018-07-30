import sys
import numpy as np

age = np.loadtxt(sys.argv[1], skiprows=1, usecols=1)

mean_age = sum(age)/len(age)

np.savetxt("demeaned_" + sys.argv[1], age-mean_age)

assert age < 100
assert age > 10

print("done!")