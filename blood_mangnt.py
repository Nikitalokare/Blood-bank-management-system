#from abc import abstractclassmethod,ABC
from donor import Donor
from person import Person
import pandas as pd
from datetime import date,datetime

from prettytable import PrettyTable
class bloodManagement:
    def addDonatorData(self,d1):
        with open("donordata.txt","a") as fp:
                #details = str(p1)
                data = str(d1)
                #fp.write(details)
                fp.write(data)
                fp.write("\n")
                print("Details added successfully!!")
    def ViewDonorData(self):
        try:
            with open("donordata.txt","r") as fp:
                '''df = pd.read_csv("donordata.txt")
                print(df.to_string())''' 
                '''d = fp.read()
                print(d)'''
                pt = PrettyTable(["Donor Id","Donor Name","Phone no.","Blood group","Gender","Donor address","Donor Date of birth","Donation date","donation time","blood quantity(ml)"])
                for line in fp:
                    data = line.split(",")
                    #for i in data:
                    pt.add_row([data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]])
                print(pt)
        except FileNotFoundError:
            print("File does not exist")
    def viewStock(self):
        try:
            with open("stockavailability.txt","r") as fp:
                pt = PrettyTable(["Donor ID", "Blood group", "Quantity"])
                for line in fp:
                    data = line.split(",")
                    pt.add_row([data[0],data[1],data[2]])
                print(pt)
        except FileNotFoundError:
            print("File does not exist")
        
    
    def addReceiverData(self,r1):
        with open("Receiverdata.txt","a") as fp:
            rdata = str(r1)
            fp.write(rdata)
            fp.write("\n")

    def ViewReceiverData(self):
        try:
            with open("Receiverdata.txt","r") as fp:
                pt = PrettyTable(["Donor ID","Receiver Name","Gender","Receiver ID","rev date","receive time","quantity","Blood group","Hospital name"])
                for line in fp:
                    data = line.split(",")
                    pt.add_row([data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8]])
                print(pt)
        except FileNotFoundError:
            print("File does not exist")
    
    def searchDonorbyId(self,id):
        try:
            with open("donordata.txt","r") as fp:
                for line in fp:
                    data = line.split(",")
                    if(data[0] == id):
                        print("Record Found")
                        pt = PrettyTable(["Donor Id","Donor Name","Phone no.","Blood group","Gender","Donor address","Donor Date of birth","Donation date","donation time","blood quantity(ml)"])
                    #for i in data:
                        pt.add_row([data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]])
                        print(pt)
                        break
                else:
                    print("Record Not found")
        except FileNotFoundError:
            print("File Does not exist")
    def searchDonorbyName(self,Name):
        try:
            with open("donordata.txt","r") as fp:
                for line in fp:
                    data = line.split(",")
                    if(data[1].lower() == Name):
                        print("Record Found")
                        pt = PrettyTable(["Donor Id","Donor Name","Phone no.","Blood group","Gender","Donor address","Donor Date of birth","Donation date","donation time","blood quantity(ml)"])
                    #for i in data:
                        pt.add_row([data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9]])
                        print(pt)
                        break
                else:
                    print("Record Not found")
        except FileNotFoundError:
            print("File Does not exist")
    def checkAvailofBlood(self,bloodgrp):
        bldlist = []
        idbldlist = []
        found = False
        try:
            with open("stockavailability.txt","r") as fp:
                for line in fp:
                    data = line.split(",")
                    bldlist.append(data[1])
                    idbldlist.append(data[0])
                if(bloodgrp == 'A+'):
                    if("A+" in bldlist):
                        for i,j in zip(bldlist,idbldlist):
                            if (i in 'A+A-O+O-'):
                                print("Its available, Donor id is: ",j)
                    else:
                        print("Blood is not available")
                elif(bloodgrp == "A-"):
                    if("A-" in bldlist):
                        for i,j in zip(bldlist,idbldlist):
                            if i in ("A-","O-"):
                                print("Its available, Donor id is: ",j)
                    else:
                        print("Blood is not available")
                elif(bloodgrp == "B+"):
                    if("B+" in bldlist):
                        for i,j in zip(bldlist,idbldlist):
                            if i in ("B+","B-","O+","O-"):
                                print("Its available, Donor id is: ",j)
                    else:
                        print("Blood is not available")
                elif(bloodgrp == "B-"):
                    if("B-" in bldlist):
                        for i,j in zip(bldlist,idbldlist):
                            if i in ("B-","O-"):
                                print("Its available, Donor id is: ",j)
                    else:
                        print("Blood is not available")
                                
                elif(bloodgrp == "AB+"):
                    if("AB+" in bldlist):
                        for i,j in zip(bldlist,idbldlist):
                            if i in ("A+","A-","B+","B-","AB+","AB-","O+","O-"):
                                print("Its available, Donor id is: ",j)
                    else:
                        print("Blood is not available")
                elif(bloodgrp == "AB-"):
                    if("AB-" in bldlist):
                        for i,j in zip(bldlist,idbldlist):
                            if i in ("A-","B-","AB-","O-"):
                                print("Its available, Donor id is: ",j)
                    else:
                        print("Blood is not available")
                elif(bloodgrp == "O+"):
                    if("O+" in bldlist):
                        for i,j in zip(bldlist,idbldlist):
                            if i in ("O+","O-"):
                                print("Its available, Donor id is: ",j)
                    else:
                        print("Blood is not available")
                elif(bloodgrp == "O-"):
                    if("O-" in bldlist):
                        for i,j in zip(bldlist,idbldlist):
                            if i in ("O-"):
                                print("Its available, Donor id is: ",j)
                    else:
                        print("Blood is not available")
                
        except FileNotFoundError:
            print("File Does not exist")

    def SearchbyReceivername(self,name):
        try:
            with open("Receiverdata.txt","r") as fp:
                for line in fp:
                    rdata = line.split(",")
                    if(rdata[1].lower() == name):
                        print("Record found")
                        pt = PrettyTable(["Donor ID","Receiver Name","Gender","Receiver ID","rev date","receive time","quantity","Blood group","Hospital name"])
                        pt.add_row([rdata[0],rdata[1],rdata[2],rdata[3],rdata[4],rdata[5],rdata[6],rdata[7],rdata[8]])
                        print(pt)
                        break
                else:
                    print("Record Not found")
        except FileNotFoundError:
            print("File does not exist")    

    def SearchbyReceiverID(self,id):
        try:
            with open("Receiverdata.txt","r") as fp:
                for line in fp:
                    rdata = line.split(",")
                    if(rdata[3] == id):
                        print("Record found")
                        pt = PrettyTable(["Donor ID","Receiver Name","Gender","Receiver ID","rev date","receive time","quantity","Blood group","Hospital name"])
                        pt.add_row([rdata[0],rdata[1],rdata[2],rdata[3],rdata[4],rdata[5],rdata[6],rdata[7],rdata[8]])
                        print(pt)
                        break
                else:
                    print("Record Not found")
        except FileNotFoundError:
            print("File does not exist") 

    def discardDonorDetails(self):
        newDonorData = []
        found = False
        today = date.today()
        self.discard_date = today.strftime("%d/%m/%Y")
        self.discard_date = self.discard_date.split("/")
        self.discard_date = date(int(self.discard_date[2]),int(self.discard_date[1]),int(self.discard_date[0]))
        #d1 = today.strftime("%d/%m/%Y")
        #print(self.discard_date)
        try:
            with open("donordata.txt","r") as fp:
                for line in fp:
                    data = line.split(",")
                    someday = data[7]
                    someday = someday.split("-")
                    #print(someday)
                    someday = date(int(someday[2]),int(someday[1]),int(someday[0]))
                    discard_period = (self.discard_date-someday)
                    print(discard_period)
                    if(str(discard_period) > str(42)):
                        found = False
                    else:
                        newDonorData.append(line)
                        found = True
                if(found):
                    with open("donordata.txt","w") as fp:
                        print("Discard successufully")
                        for discarddata in newDonorData:
                            print(discarddata)
                            fp.write(discarddata)
                            #break
                else:
                    print("Record not found")
        except FileNotFoundError:
            print("File does not exist")