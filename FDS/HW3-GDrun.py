import matplotlib.pyplot as plt
import numpy as np
import csv

IDlib = __import__("1772953-lib")

f = open('wine.csv')
X = list(csv.reader(f, delimiter=','))
f.close()

header = X[0]
X = np.asarray(X[1:]).astype(np.float)

y = X[:, header.index('Price')]
X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
X[:, header.index('Price')] = y

XAGST = X[:, [header.index('AGST')]]
theta = IDlib.descent(y, XAGST, alpha=1e-2, itr=1e6, eps=1e-6)
print('Features: AGST')
print('Coefficients:', theta)
print('R2:', IDlib.r2(y, theta, XAGST))
print()

plt.scatter(XAGST, y)

indexPred = np.argsort(X[:, header.index('AGST')])
predictions = IDlib.predict(XAGST, theta)
plt.plot(XAGST[indexPred, 0], predictions[indexPred],
         color='red', linewidth=3)
plt.savefig('1772953.png')

features = ['AGST', 'WinterRain', 'HarvestRain', 'Age']
Xmulti = X[:, [header.index(f) for f in features]]
theta = IDlib.descent(y, Xmulti, alpha=1e-2, itr=1e6, eps=1e-6)

print('Features: AGST, WinterRain, HarvestRain, Age')
print('Coefficients:', theta)
print('R2:', IDlib.r2(y, theta, Xmulti))
print()
