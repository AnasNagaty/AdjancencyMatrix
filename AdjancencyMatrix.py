import copy

Hn = []

def getindex(city):
    count = 0
    for i in Hn:
        if(city == i.name):
            return count
        count+=1


class city:
    def __init__(self,name,h):
        self.name = name
        self.h = h


def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j].h > arr[j+1].h : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 


f = open("Hn.txt","r")
for i in f:
    x = i.split(",")
    Hn.append(city(x[0],int(x[1])))
sortedHn = copy.deepcopy(Hn)
bubbleSort(sortedHn)


adjMatrix = [[0 for i in range(20)] for j in range(20)] 
u = open("Table.txt","r")
for xx in u:
    y = xx.split(",")
    adjMatrix[int(getindex(y[0]))][int(getindex(y[1]))] = int(y[2])
    adjMatrix[int(getindex(y[1]))][int(getindex(y[0]))] = int(y[2])


header = "\t"
for i in range(20):
    header += Hn[i].name[0] + "   "
print(header)

for i in range(20):
    row = ""
    for j in range(20):
        if(adjMatrix[i][j] == 0):
            row += str(adjMatrix[i][j]) + " | "
        else:
            row += str(adjMatrix[i][j]) + "|"
    
    print(Hn[i].name[0] + "\t" + row)
    
    print("--------------------------------------------------------------------------------------")


print("\nSorted Ascending: \n")
for i in sortedHn:
    print(i.name + " " + str(i.h))
print("\n\n")

print("Enter city")
x = input()
for i in range(20):
    if(Hn[i].name[0] == x):
        for j in range(20):
              if(adjMatrix[i][j] != 0):
                  print("\n")
                  print(Hn[j].name)