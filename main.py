# ?????????????????????????
# HOWTO write data.csv:
# [x of shop];[y of shop][\n (Enter)]
# [x of 1st house];[y of 1st house][\n]
# [x of 2nd house];[y of 2nd house][\n]
# [x of 3rd house];[y of 3rd house][\n]
# etc.
# ?????????????????????????

# data = [[float(w) for w in q.split(",")] for q in open("asasasa.csv").read().split("\n")]

def way(data,k,Debug=-1):
	path = []
	buildingsDone = 0
	fullLen=0

	lens = {}
	clusters={}
	for source in range(len(data)):
		lens[source]={}
		for destination in range(len(data)):
			# print(source,destination,clusters)
			if not source in clusters:clusters[source]=[]
			if source != destination:
				lens[source][destination] = ((data[source][0]-data[destination][0])
								** 2+(data[source][1]-data[destination][1])**2)**.5
				if source*destination!=0 \
					and lens[source][destination]\
						<lens[source][0]:
					clusters[source].append(destination)
	if Debug>=1:print("[log]:",lens,clusters)
	while buildingsDone < len(data)-1:
		path.append(0)
		if Debug>=0:print("[info]:now at shop")
		currentHouse = 0
		for boxGiven in range(k):
			bestDestination = None
			bestWeight = None
			currWeight=None
			kWayFromShop=abs(k/2-boxGiven) #/(k/2-boxGiven)
			for checkHouse in lens[currentHouse]:#Buildings checking 
				# if not (checkHouse==0 and len(data)-1-buildingsDone>=k):
				isEndWay=len(data)-1-buildingsDone<=k-boxGiven or currentHouse==0
				if isEndWay:shopWay=1
				elif checkHouse==0:shopWay = lens[currentHouse][0]
				else:shopWay = lens[checkHouse][0]-lens[currentHouse][0]

				#currWeight = (abs(lens[checkHouse][currentHouse])**(k/2-boxGiven))*shopWay/abs(shopWay)/lens[currentHouse][checkHouse]
				currWeight=kWayFromShop**(abs(shopWay))/lens[currentHouse][checkHouse]
				if ((bestWeight == None or currWeight >= bestWeight) and not (checkHouse != 0 and checkHouse in path) and not (checkHouse==0 and shopWay==1)):
					bestDestination = checkHouse
					bestWeight = currWeight
				if Debug>=1:print('[log]:',currentHouse,checkHouse,shopWay,currWeight,'|',bestDestination,bestWeight,isEndWay)
			if not isEndWay and currentHouse*bestDestination  and not bestDestination in clusters[currentHouse]:bestDestination=0
			if Debug>=0:print("[info]:gone to", bestDestination,",", len(data)-1-buildingsDone, "left")
			if bestDestination!=None:
				fullLen+=lens[currentHouse][bestDestination]
			if bestDestination in [None,0]:break
			buildingsDone+=1
			path.append(bestDestination)
			currentHouse = bestDestination
	if Debug>=0:print(path,fullLen)
	return path,fullLen
# def minWay(data,k):


# way(data=data,k=7,Debug=10)
