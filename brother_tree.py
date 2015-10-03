import csv

class node:
    def __init__(self, big, active, pledgeClass, roll, name):
        self.roll = roll
        self.name = name
        self.big = big
        self.active = active
        self.pledgeClass = pledgeClass
    def toString(self):
        print(str(self.roll) + "\t" + self.name + "\t" + str(self.active) + "\t" + self.pledgeClass + "\t" + self.big)



filterOutMember = ['S','D']
setActive = {"Active":0,"Alumni":1,"Disassociated":2, "Transferred/ Left School":1}

with open('Roll - Brothers.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    count = 0
    nodeList = []
    for row in reader:
        if count != 0:
            if (not row[0][0] in filterOutMember):
                 row[2] = setActive.get(row[2])
                 n = node(row[5],row[2],row[6],int(row[0]),row[1])
                 nodeList.append(n)
                 n.toString()
        count = count + 1


    



        

