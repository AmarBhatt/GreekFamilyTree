import csv

class member:
    def __init__(self, big, bigRoll, status, pledgeClass, roll, name):
        self.roll = roll
        self.bigRoll = bigRoll
        self.name = name
        self.big = big
        self.status = status
        self.pledgeClass = pledgeClass
    def toString(self):
        print(str(self.roll) + "\t" + self.name + "\t" + str(self.status) + "\t" + self.pledgeClass + "\t" + self.big + "\t" + str(self.bigRoll))

class node:
    def __init__(self, head, child, data):
        self.head = head
        self.child = child
        self.data = data
    def addChild(self, c):
        child.append(c)
    def toString(self):
        print(str(self.data) + str(self.head) + str(self.child))

filterOutMember = ['S','D']
setStatus = {"Active":0,"Alumni":1,"Disassociated":2, "Transferred/ Left School":1}
memberLookup = {}
nodeList = []
memberDict = {}
def readRoll(Roll):
    with open(Roll, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        count = 0
        nodeList = []
        for row in reader:
            if count != 0:
                if (not row[0][0] in filterOutMember):
                     row[2] = setStatus.get(row[2])
                     if(row[5] == ""):
                         row[5] = -1;
                     n = member(row[6],int(row[5]),row[2],row[6],int(row[0]),row[1])
                     memberLookup[int(row[0])] = n
                     memberDict[int(row[0])]=int(row[5])
                     n.toString()
            count = count + 1

def getHeads():
    heads = [brother for brother, big in memberDict.items() if big == -1]
    count = 0
    for h in heads:
        heads[count] = node(None, [], h)
        count += 1
    return heads

def populateTree(n):
    children = [brother for brother, big in memberDict.items() if big == n.data]
    if (children == []):
        return
    for c in children:
        c = node(n,[],c)
        n.child.append(c)
        populateTree(c)
        
    
    
def printTree(n):
    print(memberLookup.get(n.data).name + "->", end='')
    if (n.child == []):
        return
    for c in n.child:
        printTree(c)

def main():
    readRoll('Roll - Brothers.csv')
    print(memberLookup)
    count = 1
    for h in getHeads():
        populateTree(h)
        print("Tree ",count,": ",memberLookup.get(h.data).name)
        printTree(h)
        print()
        count+=1
                

main()
        

