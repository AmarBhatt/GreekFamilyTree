class node:
    number = 0
    little=[]


raw = open('Roll - Brothers.csv','r')

count = 0
for line in raw:
    if count != 0:        
        item = line.split(",",2)
        '''item[0] = int(item[0])
        item[2] = item[2].rstrip('\n')
        item[2] = item[2].rstrip('"')'''
        print(item)
    count = count + 1



    
