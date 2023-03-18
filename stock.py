from donor import Donor
from person import Person
from blood_mangnt import bloodManagement
from receiver import receiver
class Stock:
    def addStockDetails(self):
        newlist = []
        #found = False
        try:
            with open("donordata.txt","r") as fp:
                for line in fp:
                    #newlist = []
                    found = False
                    data = line.split(",")
                    if data[3] in ("A+","A-","O+","O-","B+","B-","AB+","AB-"):
                        found = True
                        li = str(data[0]) + "," + str(data[3]) + "," + str(data[9])
                        newlist.append(li)
                    #    newlist.append(data[3])
                    #    newlist.append(data[9])
                if(found):
                    with open("stockavailability.txt","w") as fp:
                        print("Details Added succesfully")
                        #fp.write(str("Donor ID")+str("Blood Group")+str("Quantity"))
                        for blood in newlist:
                            fp.write(blood)
                            #fp.write("\n")
                        
                else:
                    print("Record not found")
        except FileNotFoundError:
            print("File does not exist")

    def totalQuantity(self):
        blist = []
        rce = []
        #found = False
        try:
            with open("Receiverdata.txt","r") as fp:
                for line in fp:
                    rdata = line.split(",")
                    rdata[0]
                    
        except:
            print("File does not exist 1")
        
        try:
            with open("stockavailability.txt","r") as fp:
                for line in fp:
                    sdata = line.split(",")
                    #for i in range(rce):
                    if(sdata[0] == rdata[0]):
                        found = False
                        sdata[2] = int(sdata[2]) - int(rdata[6])
                        if(sdata[2] >= 0):
                            found = True
                            newdata = str(sdata[0]) +","+str(sdata[1])+","+str(sdata[2])
                            blist.append(newdata)
                            #blist.append(str(sdata[2]))
                        elif(sdata[2] <= 0):
                            print("Blood is not suffient")
                            break                        
                    else:
                        newdata = str(sdata[0]) +","+str(sdata[1])+","+str(sdata[2])
                        blist.append(newdata)
                        #blist.append(sdata[0])
                        #blist.append(sdata[1])
                        #blist.append(sdata[2])
                    #print(blist)
                if(found):
                    with open("stockavailability.txt","w") as fp:
                        print("successfully upgrade")
                        for i in blist:
                            fp.write(i)
                            #fp.write(",")  
                    
        except:
            print("File does not exist 2")

    def discardStockDetails(self):
        newstockData = []
        found = False
        try:
            with open("stockavailability.txt","r") as fp:
                for line in fp:
                    data = line.split(",")
                    #print(data[2])
                    if(str(data[2]) < str(45)):
                        ("yes")
                        found = True
                    else:
                        newstockData.append(line)
                if(found):
                    with open("stockavailability.txt","w") as fp:
                        print("Discard successufully")
                        for discarddata in newstockData:
                            fp.write(discarddata)
                            #break
                else:
                    print("Record not found")
        except FileNotFoundError:
            print("File does not exist")