import csv
import pprint as pp
import networkx as nx
import itertools as it
import math
import scipy.sparse
import random




def pagerank(M, N, nodelist, alpha=0.85, personalization=None, max_iter=100, tol=1.0e-6, dangling=None):
	if N == 0:
		return {}
	S = scipy.array(M.sum(axis=1)).flatten()
	S[S != 0] = 1.0 / S[S != 0]
	Q = scipy.sparse.spdiags(S.T, 0, *M.shape, format='csr')
	M = Q * M
	
	# initial vector
	x = scipy.repeat(1.0 / N, N)
	
	# Personalization vector
	if personalization is None:
		p = scipy.repeat(1.0 / N, N)
	else:
		missing = set(nodelist) - set(personalization)
		if missing:
			#raise NetworkXError('Personalization vector dictionary must have a value for every node. Missing nodes %s' % missing)
			print
			print ('Error: personalization vector dictionary must have a value for every node')
			print
			exit(-1)
		p = scipy.array([personalization[n] for n in nodelist], dtype=float)
		#p = p / p.sum()
		sum_of_all_components = p.sum()
		if sum_of_all_components > 1.001 or sum_of_all_components < 0.999:
			print
			print ("Error: the personalization vector does not represent a probability distribution :(")
			print
			exit(-1)
	
	# Dangling nodes
	if dangling is None:
		dangling_weights = p
	else:
		missing = set(nodelist) - set(dangling)
		if missing:
			#raise NetworkXError('Dangling node dictionary must have a value for every node. Missing nodes %s' % missing)
			print
			print ('Error: dangling node dictionary must have a value for every node.')
			print
			exit(-1)
		# Convert the dangling dictionary into an array in nodelist order
		dangling_weights = scipy.array([dangling[n] for n in nodelist], dtype=float)
		dangling_weights /= dangling_weights.sum()
	is_dangling = scipy.where(S == 0)[0]

	# power iteration: make up to max_iter iterations
	for _ in range(max_iter):
		xlast = x
		x = alpha * (x * M + sum(x[is_dangling]) * dangling_weights) + (1 - alpha) * p
		# check convergence, l1 norm
		err = scipy.absolute(x - xlast).sum()
		if err < N * tol:
			return dict(zip(nodelist, map(float, x)))
	#raise NetworkXError('power iteration failed to converge in %d iterations.' % max_iter)
	print
	print ('Error: power iteration failed to converge in '+str(max_iter)+' iterations.')
	print
	exit(-1)
