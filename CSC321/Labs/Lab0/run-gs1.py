#!/usr/bin/env python


import gs1
import numpy as np

lst = [100, 200, 300, 400, 500]

myfile = open('data.txt', 'w')

for i in lst:
    myfile.write("%s\n" % gs1._Input(i))
myfile.close()

'/usr/bin/gnuplot -persist model.gpt'


