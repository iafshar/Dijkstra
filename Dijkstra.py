import heapdict
import random

def Dijkstra(V, E, s):
    dist = []
    for vIndex in range(len(V)):
        if V[vIndex] == s:
            dist.append(0)
        else:
            dist.append(100000)

    H = heapdict.heapdict()
    for vIndex in range(len(V)):
        H[vIndex] = dist[vIndex]
    count = 0
    while len(H.items()) > 0:
        vIndex = H.popitem()[0]
        for uIndex in range(len(E[vIndex])):
            if dist[uIndex] > dist[vIndex] + E[vIndex][uIndex] and E[vIndex][uIndex] > 0:
                dist[uIndex] = dist[vIndex] + E[vIndex][uIndex]
                H[uIndex] = dist[uIndex]
                count += 1
    
    return count

V = []
E = []
s = 0

for x in [8,16,32,64,128,256,512,1024,2048,4096]:
    for i in range(x):
        V.append(i)
        E.append([])
        for j in range(x):
            E[i].append(random.random())

    s = V[random.randint(0,x-1)]

    print(Dijkstra(V,E,s))
