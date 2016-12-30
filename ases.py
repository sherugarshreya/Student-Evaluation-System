
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from numpy import *
import numpy as np 
import operator 
 


data = np.genfromtxt('C:\Users\Rahul\Desktop\LBS\student_eval.txt', delimiter = ',')
Y=np.array( [x[7] for x in data] )
X=np.array( [x[1:7] for x in data] )
from sklearn import tree
  
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)


acads=float(sys.argv[1])    
sports=int(sys.argv[2])   
debdis=int(sys.argv[3])   
dance=int(sys.argv[4])    
tpp= int(sys.argv[5])     
wexp= int(sys.argv[6])   

ars=clf.predict([[acads,sports,debdis,dance,tpp,wexp]])
if ars==[1.] :
 print '\n \n You are all round student'
else :
 print 'You are not an  all round student.You need to improve \n suggested profiles are:'
 data = np.genfromtxt('C:\Users\Rahul\Desktop\LBS\suggestion.txt', delimiter = ',') 
 group =np.array( [x[0:6] for x in data] )
 inX=[acads,sports,debdis,dance,tpp,wexp]
 title=['Improve your Academics','Excell in sports','Debates','Involve in Dance/music/etc','Publish  papers','Do some Work/Internships']
 groupSize = group.shape[0]
 diffMat = tile(inX, (groupSize,1)) - group
 sqDiffMat = diffMat**2
 sqDistances = sqDiffMat.sum(axis=1)
 distances = sqDistances**0.5
 sortedDistIndicies = distances.argsort()  
 print  'your profile is:' 
 print '<div class="csstable1" ><table><tr>'
 print   '<th>Acads </th>'
 print   '<th>Sports </th>'
 print   '<th>DebDisc </th>'
 print   '<th>DramDance </th>'
 print   '<th>tpp </th>'
 print   '<th>wexp </th>'
 print   '</tr>'
 print '<tr><th>'
 print acads
 print '</th>'
 print '<th>'
 if sports==4.0:
  print 'Inter School/College'	
 elif sports==6.0:
  print 'District Level'
 elif sports==8.0:
  print 'State Level'
 elif sports==10.0:
  print 'National Level'
 else:
  print '&#10005'	
 print'</th>'
 print '<th>'
 if debdis==3.0:
  print 'Inter School/College'	
 elif debdis==5.0:
  print 'District Level'
 elif debdis==10:
  print 'State/National Level'
 else:
  print '&#10005'	
 print'</th>'
 print '<th>'
 print dance
 print '</th>'
 print '<th>'
 if tpp==1.0:
  print '&#10004';
 elif tpp==0.0:
  print '&#10005'
 print'</th>'
 print '<th>'
 if wexp==1.0:
  print '&#10004';
 elif wexp==0.0:
  print '&#10005'
 print'</th></tr></table></div>'
 print "The Suggested Profiles are " 
 print '<div class="csstable" ><table><tr>'
 print   '<th>Acads </th>'
 print   '<th>Sports </th>'
 print   '<th>DebDisc </th>'
 print   '<th>DramDance </th>'
 print   '<th>tpp </th>'
 print   '<th>wexp </th>'
 print   '<th>You Should Focus on</th>'
 print   '</tr>'
 count=0
 for i in range(30):
  if group[sortedDistIndicies[i],0]>=acads and group[sortedDistIndicies[i],1]>=sports and group[sortedDistIndicies[i],2]>=debdis and group[sortedDistIndicies[i],3]>=dance and group[sortedDistIndicies[i],4]>=tpp and group[sortedDistIndicies[i],5]>=wexp and count<=5:
    count+=1
  if group[sortedDistIndicies[i],0]>=acads and group[sortedDistIndicies[i],1]>=sports and group[sortedDistIndicies[i],2]>=debdis and group[sortedDistIndicies[i],3]>=dance and group[sortedDistIndicies[i],4]>=tpp and group[sortedDistIndicies[i],5]>=wexp and count<=5:	 
    print '<tr><th>'
    print group[sortedDistIndicies[i],0] 
    print '</th>'
    print '<th>'
    if group[sortedDistIndicies[i],1]==4.0:
     print 'Inter School/College'	
    elif group[sortedDistIndicies[i],1]==6.0:
     print 'District Level'
    elif group[sortedDistIndicies[i],1]==8.0:
     print 'State Level'
    elif group[sortedDistIndicies[i],1]==10.0:
     print 'National Level'
    else:
     print '&#10005'	
    print'</th>'
    print '<th>'
    if group[sortedDistIndicies[i],2]==3.0:
     print 'Inter School/College'	
    elif group[sortedDistIndicies[i],2]==5.0:
     print 'District Level'
    elif group[sortedDistIndicies[i],2]==10:
     print 'State/National Level'
    else:
     print '&#10005'	
    print'</th>'
    print '<th>'
    print group[sortedDistIndicies[i],3]
    print '</th>'
    print '<th>'
    if group[sortedDistIndicies[i],4]==1.0:
	 print '&#10004';
    elif group[sortedDistIndicies[i],4]==0.0:
     print 	'&#10005'
    print'</th>'
    print '<th>'
    if group[sortedDistIndicies[i],5]==1.0:
	 print '&#10004';
    elif group[sortedDistIndicies[i],5]==0.0:
     print 	'&#10005'
    print'</th>'
    print '<th>'	
    arr=array([(group[sortedDistIndicies[i],0]-acads)**2,(group[sortedDistIndicies[i],1]-sports)**2,(group[sortedDistIndicies[i],2]-debdis)**2,(group[sortedDistIndicies[i],3]-dance)**2,(group[sortedDistIndicies[i],4]-tpp)**2,(group[sortedDistIndicies[i],5]-wexp)**2])
   
    recom=arr.argsort()
    
    recvalue=recom[5]
    recvalue1=recom[4]
    print title[recvalue],'and',title[recvalue1]
    print '</th>'
    print '</tr>'
	 
 print '</table></div>'	