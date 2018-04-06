#!/usr/bin/env python3

from __future__ import division
import numpy as np
from heapdict import heapdict
import copy
import pprint
from random import shuffle
from random import randint
import time
import random

def Shapley():


	women = ['Amy','Bertha','Clare','Diane','Erika',
                 'Lily', 'Eva', 'Mira', 'Rose', 'Ruby']
	

	women1 = ['Amy','Bertha','Clare','Diane','Erika',
                      'Lily', 'Eva', 'Mira', 'Rose', 'Ruby'] 
	

	men = ['Victor','Wyatt','Xavier','Yancey','Zeus',
               'Alex', 'Tom', 'Adam', 'Ben', 'Carl']

    men1 = ['Victor','Wyatt','Xavier','Yancey','Zeus',
                    'Alex', 'Tom', 'Adam', 'Ben', 'Carl'] 

    print ("participants:")
	print ('suitors: {}'.format(' '.join(men)))
	print ('girls: {}'.format(' '.join(women)))

	def shuffleACopy(x):
        	b = x[:] # make a copy of the keys
        	random.shuffle(b) # shuffle the copy
        	return b # return the copy

	rank = dict()
	trial = 1

	while (trial):
	    trial = 0
	    start = time.time()

	    print ("preferences:")
	    for i in range(len(men)):
	      rank[men[i]] = shuffleACopy(women1)
	      rank[women[i]] = shuffleACopy(men1)
	      
	    N = int(len(rank)/2)
	    for key in rank:
		    print('{}: {}'.format(key, ' '.join(rank[key])))
		    
	    FreeMen = heapdict()
	    for i in range(len(men)):
		    FreeMen[men[i]] = i + N 

	    matchedM = dict()
	    matchedW = dict()
	    count = np.zeros(N)     

	    while (FreeMen.__len__() != 0 and
                count[men.index(FreeMen.peekitem()[0])] < N):
    		m = FreeMen.popitem()[0]                    
    		w = rank[m][int(count[men.index(m)])]            
    		print ('{} proposes to {}'.format(m,w))
    
    		if w not in matchedW:                       
    		    matchedM[m] = w                         
    		    matchedW[w] = m                         
    		    count[men.index(m)] += 1                
    		    print ('{} is engaged to {} '.format(m, w))
    
    		elif rank[w].index(m) < rank[w].index(matchedW[w]):   
    		    m1 = matchedW[w]                                
    		    FreeMen[m1] = N - np.sum(count)          
    		    FreeMen._min_heapify(0)
    		    matchedM[m] = w                         
    		    matchedW[w] = m                         
    		    count[men.index(m)] += 1                
    		    print ('{} dumps {} and accepts {}'.format(w, m1, m))
    		else:
    		    FreeMen[m] = N - np.sum(count)           
    		    FreeMen._min_heapify(0)
    		    count[men.index(m)] += 1                
    		    print ('{} rejects since she prefers {}'.format(w, matchedW[w]))
    		
		
	    print ('Pairing:')
	    pprint.pprint(matchedM, width= 1)
	    stop = time.time()
	    duration = stop - start
	    print('Time elapsed:', duration)
	    print("Stable matchup\n")
	    if (input("another trial? (y)es (n)0") not in ['no', 'n']):
		    trial = 1
if __name__ == "__main__":
  Shapley()





