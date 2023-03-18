class Person:
    
    def __init__(self,name,phno,bldgrp,gen,add,dob):
       
        self.pname = name
        self.phone_no = phno
        self.blood_grp = bldgrp
        self.gender = gen
        self.address = add
        self.date_of_birth = dob

    def __str__(self):
        details = str(self.pname)+","+str(self.phone_no)+","+str(self.blood_grp)+","+str(self.gender)+","+str(self.address)+","+str(self.date_of_birth)
        return details

if(__name__ == "__main__"):
    p1 = Person("Nikita","9820169828","B+","F","Thane","29-6-1999")
    print(p1)