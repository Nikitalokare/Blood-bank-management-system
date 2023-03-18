from person import Person
import datetime

e = datetime.datetime.now()
class Donor(Person):
    count_id = 0
    def __init__(self,name,phno,bldgrp,gen,add,dob,date,quantity):
        super().__init__(name,phno,bldgrp,gen,add,dob)
        self.donation_date = date
        self.donation_time = e.strftime("%I:%M:%S %p")
        self.donated_quantity = quantity

        with open("donordata.txt","r") as fp:
            for line in fp:
                data = line.split(",")
            Donor.count_id += 1
            self.did = str(Donor.count_id + int(data[0]))

    def __str__(self):
        data =str(self.did)+","+str(self.pname)+","+str(self.phone_no)+","+str(self.blood_grp)+","+str(self.gender)+","+str(self.address)+","+str(self.date_of_birth)+","+ str(self.donation_date)+","+str(self.donation_time)+","+str(self.donated_quantity)
        return data 
    '''def RemoveDonatorData(self):
        pass

    def editDonatorData(self):
        pass

    def viewDonatorData(self):
        pass'''

