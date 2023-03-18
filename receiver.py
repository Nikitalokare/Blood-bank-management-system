from donor import Donor
from blood_mangnt import bloodManagement
from person import Person

mangt = bloodManagement()
import time
class receiver():
    count_rec = 100
    def __init__(self,donorid,rname,rgender,rdate,rtime,rqunt,rbldgrp,hosptname):
        #super().__init__(name,phno,bldgrp,gen,add,dob)
        self.donorid = donorid
        self.receivername = rname
        self.receivergender = rgender
        self.receivedate = rdate
        self.receivetime = time.strftime("%H:%M:%S")
        self.receivequantity = rqunt
        self.receivebloodgroup = rbldgrp
        self.hospitalname = hosptname
        with open("Receiverdata.txt","r") as fp:
            for line in fp:
                data = line.split(",")
            receiver.count_rec += 1
            self.receiverid = str(receiver.count_rec + int(data[3]))

    def __str__(self):
        rdata = str(self.donorid)+","+str(self.receivername)+","+str(self.receivergender)+","+str(self.receiverid)+","+str(self.receivedate)+","+str(self.receivetime)+","+str(self.receivequantity)+","+str(self.receivebloodgroup)+","+str(self.hospitalname)
        return rdata

    '''def addReceiverData(self,r1):
        with open("Receiverdata.txt","a") as fp:
            rdata = str(r1)
            fp.write(rdata)
            fp.write("\n")'''

    

