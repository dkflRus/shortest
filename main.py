# ?????????????????????????
# HOWTO write data.csv:
# [x of home];[y of home][\n (Enter)]
# [x of 1st house];[y of 1st house][\n]
# [x of 2nd house];[y of 2nd house][\n]
# [x of 3rd house];[y of 3rd house][\n]
# etc.
# ?????????????????????????

# data = [[float(w) for w in q.split(",")] for q in open("data.csv").read().split("\n")]

def way(data,k,Debug=-1):
	path = []
	buildingsDone = 0
	fullLen=0

	lens = {}
	for source in range(len(data)):
		h = {}
		for destination in range(len(data)):
			if source != destination:
				h[destination] = ((data[source][0]-data[destination][0])
								** 2+(data[source][1]-data[destination][1])**2)**.5
		lens[source] = h
	if Debug>=1:print("[log]:",lens)
	while buildingsDone < len(data)-1:
		path.append(0)
		if Debug>=0:print("[info]:now at home")
		currentHouse = 0
		for boxGiven in range(k):
			bestDestination = None
			bestWeight = None
			currWeight=None
			for checkHouse in lens[currentHouse]:
				# if not (checkHouse==0 and len(data)-1-buildingsDone>=k):
				if len(data)-1-buildingsDone<=k or currentHouse==0:homeWay=1	
				else:homeWay = lens[currentHouse][0]

				currWeight = (homeWay**(k/2-boxGiven))/lens[currentHouse][checkHouse]
				if ((bestWeight == None or currWeight >= bestWeight) and not (checkHouse != 0 and checkHouse in path) and not (checkHouse==0 and homeWay==1)):
					bestDestination = checkHouse
					bestWeight = currWeight
				if Debug>=1:print('[log]:',currentHouse,checkHouse,homeWay,currWeight,'|',bestDestination,bestWeight)
					
			if Debug>=0:print("[info]:gone to", bestDestination,",", len(data)-1-buildingsDone, "left")
			if bestDestination!=None:
				fullLen+=lens[currentHouse][bestDestination]
			if bestDestination == None or bestDestination == 0:break
			path.append(bestDestination)
			buildingsDone += 1
			currentHouse = bestDestination
	if Debug>=0:print(path,fullLen)
	return path,fullLen

# way(data=data,k=5,Debug=10)