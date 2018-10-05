col1=[]
col2=[]
date=[]
newdate=[]

with open("Crime.csv") as myfile:
	for line in myfile:		
		line = line.strip()
		line = line.split(',')		
		col1.append(line[-1]) 		#column 1 as Criem Name
		col2.append(line[-2]) 		#column 2 as Crime id
		date.append(line[-4])

# 	"""remove the time from date as it doen't contain any information"""
	for item in date:
		item = item.split('T')[0]		
		newdate.append(item)
#	print(newdate)

	col1n2=list(zip(col1,col2))
	mylist1 = list(zip(newdate,col1n2))
	mylist= sorted(mylist1[1:]) 		# sort data as per date
#		printing the ouput in a format	
	print("{:<15} {:<20} {:<20}".format('CRIME DATE','CRIME NAME','CRIME ID'))
	for i in range(len(mylist)):
		print("{:<15} {:<20} {:<20}".format(mylist[i][0],mylist[i][1][0],mylist[i][1][1]))
	
