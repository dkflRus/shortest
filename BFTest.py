from main import way, lensAndClusters
from random import random
from copy import deepcopy
from json import dump

allCheckCnt=10

def binSearch(a,g):#with sorted a
    if a[-1]<g:return len(a)+1
    
    i=len(a)//2
    s=i//2
    buff=[None]
    while i!=buff[0]:
        if a[i]>g:i-=s
        else:i+=s
        if a[i]==g:return i
        if s>1:s//=2
        if i<0:i=0
        buff=buff[-2:]+[i]
    return buff[1]

def pathsGen(cnt,k):
    paths=[[0]]
    # cnt+=1
    for q in range(cnt,0,-1):
        for w in range(len(paths)):
            for e in range(1,cnt):
                if not e in paths[w]:
                    if 0 in paths[w][-k:]:
                        paths.append(paths[w]+[e])
                        # if e==1:paths.append(paths[-1]+[0])
                    # print(paths[w]+[e])
                    if q!=1:paths.append(paths[w]+[e,0])
    
    ans=[]
    for q in reversed(paths):
        if q in ans:break
        ans.append(q)
    return ans

cnt=3
k=2
data=[]
try:
    cnt+=1
    while True:
        print(cnt,k)
        paths=pathsGen(cnt, k)
        # print("\n".join([str(w) for w in paths]))
        data.append([[cnt,k,[],[]]])
        # print(paths)
        for _ in range(allCheckCnt):
            coords=[[random()*100 for _ in range(2)] for _ in range(cnt)]
            lens,_=lensAndClusters(coords)
            # print(lens)
            i=way(coords,k)
            if not i[0] in paths:print(f"FAIL {i[0]} in {paths}")
            # data[-1][2].append(coords)
            data[-1].append([i[1],[]])
            for q in paths:
                # print(q)
                currLen=0
                for w in range(len(q)-1):
                    currLen+=lens[q[w]][q[w+1]]
                data[-1][-1][-1].append(currLen)
                # print(data[-1][-1],currLen)
            # res=sorted(data[-1][-1][-1])
            data[-1][-1][-1].sort()
            data[-1][0][-1].append(binSearch(data[-1][-1][-1], data[-1][-1][0]))
        k+=1
        if k==cnt:
            cnt+=1
            k=2
        # if cnt==4:raise KeyboardInterrupt()
except KeyboardInterrupt:
    with open("/home/dkfl/Prog/Python/shortest/raw.json","w") as wf:dump(data, wf, indent=4)