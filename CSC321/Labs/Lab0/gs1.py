#!/usr/bin/env python

from __future__ import division
import numpy as np
from heapdict import heapdict
import copy
import pprint
import itertools
from random import shuffle
from random import randint
import time
import sys
import random

def _Input(inpt):


	men = inpt
	women = men

	#making the list of integers denoting men and women
	_lstmen = list(range(0, men))
	_lstwomen = list(range(men, 2*men))
	_lstmen1 = list(range(0, men))
	_lstwomen1 = list(range(men, 2*men))
	
	def shuffleACopy(x):
        	b = x[:] # make a copy of the keys
        	random.shuffle(b) # shuffle the copy
        	return b # return the copy

	rank = dict()
	trial = 1

	while (trial):
	    trial = 0
	    start = time.time()
	    #Shuffling the two copies lists
	    for i in range(_men):
		    rank[i] = shuffleACopy(_lstwomen1)
		    rank[i + men] = shuffleACopy(_lstmen1)
	
	    N = int(len(rank)/2)
	    FreeMen = heapdict()
	    for i in range(len(_lstmen)):
		    FreeMen[_lstmen[i]] = i + N


	    matchedM = dict()
	    matchedW = dict()
	    count = np.zeros(N)     
	    while (FreeMen.__len__() != 0 and
                count[_lstmen.index(FreeMen.peekitem()[0])] < N):
    		m = FreeMen.popitem()[0]                    
    		w = rank[m][int(count[_lstmen.index(m)])]
    
    		if w not in matchedW:                       
    		    matchedM[m] = w     
    		    matchedW[w] = m                         
    		    count[_lstmen.index(m)] += 1
    		   
    		elif rank[w].index(m) < rank[w].index(matchedW[w]):   
    		    m1 = matchedW[w]                                
    		    FreeMen[m1] = N - np.sum(count)         
    		    FreeMen._min_heapify(0)
    		    matchedM[m] = w                         
    		    matchedW[w] = m                         
    		    count[_lst_men.index(m)] += 1
    		   
    		else:
    		    FreeMen[m] = N - np.sum(count)       
    		    FreeMen._min_heapify(0)
    		    count[_lstmen.index(m)] += 1

	    stop = time.time()
	    duration = stop - start
	    return '{}\t{}'.format(men, duration)
if __name__ == "__main__":
  print(_Input(5))
