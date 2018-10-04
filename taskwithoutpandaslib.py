from collections import Counter
mylist=[]
col1=[]
col2=[]
fcol1=[]
fcol2=[]
finallist=[]
sorteddict1={}
sorteddict2={}
finaldic={}
with open("Crime.csv") as myfile:
	for line in myfile:		
		line = line.strip()
		line = line.split(',')		
		col1.append(line[-1]) 		#column 1 as Criem Name
		col2.append(line[-2]) 		#column 2 as Crime id
	col3 = dict((i, col2.count(i)) for i in col2) 		#column 3 as Crime Count

# built-in "Counter" function can also be used
#print(Counter(crime_count))

	col1n2=zip(col2,col1)
	mylist= list(col1n2)
	'''remove duplicate values of crime id and crime name'''
	for i in mylist:
#		print(i)
		if i not in finallist:
			finallist.append(i)
#	print(finallist)

	fcol1=dict(finallist[1:])		#removed header name
	fcol2=dict(list(col3.items())[1:])		#removed header name
#	print(fcol1)
#	print(fcol2)

	''' sort both dictionaries '''
	sorteddict1=dict(sorted((key1,val1) for key1,val1 in fcol1.items()))
	sorteddict2=dict(sorted((key2,val2) for key2,val2 in fcol2.items()))
#	print(sorteddict1)
#	print(sorteddict2)
#	print(type(sorteddict1))

	'''merge two dictonaries with 'crime name and id', 'id and count' based on key as 'crime id' '''
	for key in (sorteddict1.keys() or sorteddict2.keys()):
		if key in sorteddict1:
			finaldic.setdefault(key, []).append(sorteddict1[key])
		if key in sorteddict2:
			finaldic.setdefault(key, []).append(sorteddict2[key])
#	print(finaldic)

	'''Print output in table format'''
	print("{:<10} {:<23} {:<10}".format("Crime Id","Crime Name","Count"))
	for k,v in finaldic.items():
		print("{:<10} {:<23} {:<10}".format(k,v[0],v[1]))

		
		

