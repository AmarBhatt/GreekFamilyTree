import csv
from FamilyTree import *
import operator
from math import floor

## Classes ##
'''
Class: member

Used to store each member read out of the Roll.

Attributes:
    big:            STRING:     name of big
    bigRoll:        INTEGER:    Roll number of big
    status:         INTEGER:    status of member (Active, Alumni, etc.)
    pledgeClass:    STRING:     name of pledge class
    roll:           INTEGER:    Roll number of member
    name:           STRING:     name of member
'''
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
'''
Class: node

Used to store tree (member links).

Attributes:
    head:   NODE:           Node object of big
    child:  ARRAY<NODE>:    list of children (littles)     
    data:   INTEGER:        Roll number
'''
class node:
    def __init__(self, head, child, data):
        self.head = head
        self.child = child
        self.data = data
    def addChild(self, c):
        child.append(c)
    def toString(self):
        print(str(self.data) + str(self.head) + str(self.child))


filterOutMember = ['S','D'] #Filter list for Sweethearts (Sx) and Dogs (Dx)

setStatus = {"Active":1,"Alumni":0,"Disassociated":2, "Transferred/ Left School":1} #status dictionary

memberLookup = {} #dictionary mapping roll number to member object

nodeList = [] #List of nodes (trees)

memberDict = {} #dictionary mapping littles to bigs by roll number

colonyMap = {"Colony":0,
"Alpha":1,
"Beta":2,
"Gamma":3,
"Delta":4,
"Epsilon":5,
"Zeta":6,
"Eta":7,
"Theta":8,
"Iota":9,
"Kappa":10,
"Georgia Tech":0}

brotherList = [];

'''
readRoll(STRING)

Opens external .csv file to read Roll.  Creates member objects from Roll information.

Parameters: Roll - STRING - file name of roll csv
'''
def readRoll(Roll):
    with open(Roll, newline='') as csvfile: # open file
        reader = csv.reader(csvfile, delimiter='\t') # Split comma seperated values
        count = 0 
        nodeList = []
        for row in reader:
            if count != 0: # skip first row for column headers
                if (not row[0][0] in filterOutMember):
                     row[2] = setStatus.get(row[2]) #set status of member
                     if(row[15] == "N/A"): # if empty string then no Big present for member
                         row[15] = -1;
                     n = member(row[5],int(row[15]),row[2],row[7],int(row[0]),row[1]) #create object
                     #set dictionary look ups
                     memberLookup[int(row[0])] = n
                     memberDict[int(row[0])]=int(row[15])
                     n.toString()
            count = count + 1 #just to skip first one

'''
getHeads()

Finds all heads of trees (Members with bigRoll = -1 (no big)

Parameters: NONE

Return: Array<node>: list of all heads as nodes
'''
def getHeads():
    heads = [brother for brother, big in memberDict.items() if big == -1]
    count = 0
    for h in heads:
        heads[count] = node(None, [], h)
        count += 1
    return heads

'''
populateTree()

Recursively creates linked nodes to create a tree

Parameters: Node

'''
def populateTree(n):
    children = [brother for brother, big in memberDict.items() if big == n.data]
    if (children == []):
        return
    for c in children:
        c = node(n,[],c)
        n.child.append(c)
        populateTree(c)
        
'''
printTree(NODE)

Recursively prints a tree (node link) starting from node

Parameters: Node
'''    
def printTree(n):
    print(memberLookup.get(n.data).name + "->", end='')
    if (n.child == []):
        return
    for c in n.child:
        printTree(c)

'''
formatTree(NODE, INTEGER)

Formats tree for printing

Parameters: Node to format, INTEGER tree number, INTEGER current row
'''  
def formatTree(n,t,row,column,bigColumn):
    #tree, row, column, bigColumn, status, pledgeClass, roll, name
    #r4 = Brother(4,0,0,0,0,0,4,"Nick Pillon")
    #Head of tree always starts in center
    m = memberLookup.get(n.data)
    #if(m.bigRoll != -1):
        #column = column + (floor(len(n.child)/2))*2
    b = Brother(t,row,column,bigColumn,m.status,colonyMap.get(m.pledgeClass),m.roll,m.name)
    brotherList.append(b)
    bigColumn = column
    #label each based on number of children
    for c in n.child:
        col = n.child.index(c)*2-(len(n.child)-1) + bigColumn
        formatTree(c, t, row+1, col, bigColumn)
    return brotherList;

              

'''
main()

Reads Roll, then populates and prints trees

Parameters: NONE

'''   
def main():
    readRoll('Roll - Brothers.tsv')
    print(memberLookup)
    count = 1
    global brotherList
    for h in getHeads():
        populateTree(h)
        print("Tree ",count,": ",memberLookup.get(h.data).name)
        printTree(h)
        print()
        brotherList = [];
        brotherList = formatTree(h,count,0,0,0);
        brotherList.sort(key=operator.attrgetter('row'))
        print("Printing Tree: ",count);
        print(brotherList);
        printTreeGraphic(brotherList);
        count+=1
                

main()
        

