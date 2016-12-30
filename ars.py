
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from numpy import *
import numpy as np 
import operator 
 #print "The passed arguments are ", sys.argv
#print ssys.argv[1];


data = np.genfromtxt('C:\Users\Rahul\Desktop\LBS\student_eval.txt', delimiter = ',')
Y=np.array( [x[7] for x in data] )
X=np.array( [x[1:7] for x in data] )
from sklearn import tree
  
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
'''import StringIO
from sklearn.ensemble import*  
import pydot 
dot_data = StringIO.StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data( dot_data.getvalue())
graph.write_png('visualtree.png') 
#graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
#graph.write_pdf("ara.pdf") '''

result=[]
data1 = np.genfromtxt('C:\Users\Rahul\Desktop\LBS\stest.txt', delimiter = ',')
for x in data1 :
 ars=clf.predict(x[0:])
 if ars==[1.] :
#  print '\n \n You are all round student'
  result=np.append(result,ars )
  
 else :
#  print 'You are not an  all round student.You need to improve \n suggested profiles are:'
  result=np.append(result,ars ) 
#print result
'''acads=input("ENTER YOU ACADS \n")
sports=input("SPORTS \n")
debdis=input("DEBDISC \n")
dance=input("dance: \n")
tpp=input("tpp \n")
wexp=input("wexp \n")'''
#np.delete(result,0)
for x in data1:
 acads=np.array([x[0] for x in data1])
acads=np.sort(acads) 
from collections import Counter
c = Counter(result)
import matplotlib.pyplot as plt
from pylab import *
labels=['ars','no']

mi=[c[1],c[0]]
plt.pie(mi,labels=labels,autopct='%1.1f%%')
title('Percentage of All round Students',bbox={'facecolor':'0.8', 'pad':5})
plt.show()

#print clf.predict([[acads,sports,debdis,dance,tpp,wexp]])
 

 