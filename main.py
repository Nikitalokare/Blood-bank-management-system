from blood_mangnt import bloodManagement
from person import Person
from donor import Donor
from receiver import receiver
from stock import Stock

username = str("Emp1")
password = str("123Emp")

if(__name__ == "__main__"):
    ch = 0
    mangt = bloodManagement()
    stck = Stock()
    
    while(ch != str(4)):
        print('''
        1.Employees Login
        2.Looking for Blood
        3.Want to Donate Blood
        4.Exit    
        ''')
        try:
            ch = str(int(input("Enter your choice: ")))
            if(ch == str(1)):
                user_name = input("Enter a Username: ")
                pass_word = input("Enter a  password: ")
                if(user_name == username and pass_word == password):
                    while(ch != str(12)):
                        print('''
                        1. Add Donor Data
                        2. View Donor Details
                        3. add stock Details
                        4. view Stock Details
                        5. check availability of blood by (blood group and Quantity)
                        6. Add receiver Data
                        7. View Receiver Data
                        8. Search Donor Details by id
                        9. Search Donor Details by name
                        10. Search receiver Details by id
                        11. Search receiver Details by name
                        12. Exit
                        ''')
                        try:
                            ch = str(int(input("Enter your choice: ")))
                            if(ch in str('1234567891011121314')):
                                if(ch == str(1)):
                                    name = input("Enter a donor name: ")
                                    phno = str(input("Enter a phone no: "))
                                    if(len(phno)== 10):
                                        phno
                                    else:
                                        print("Please enter valid phone no!!")
                                        phno = str(int(input("Enter a phone no: ")))
                                    bldgrp = input("Enter a blood grp: ")
                                    if(bldgrp in 'A+A-B+B-AB+AB-O+O-'):
                                        bldgrp
                                    else:
                                        print("please Enter Correct blood group: ")
                                        bldgrp = input("Enter a blood grp: ")
                                    gen = input("Enter a gender: ")
                                    add = input("Enter a city: ")
                                    dob = input("Enter a date of birth: ")
                                    date = input("Enter Donation date: ")
                                    #time = input("Enter a time: ")
                                    quantity = input("Enter a quantity (1bag quantity:45ml or 2bag quantity 90ml): ")
                                    if(quantity in str('4590')):
                                        quantity
                                    else:
                                        print("please enter 1 bag quantity")
                                        quantity = input("Enter a quantity (1bag quantity:45ml): ")
                                    #p1 = Person(name,phno,bldgrp,gen,add,dob)
                                    d1 = Donor(name,phno,bldgrp,gen,add,dob,date,quantity)
                                    #mangt.addDonatorData(p1)
                                    mangt.addDonatorData(d1)
                                    mangt.discardDonorDetails()
                                elif(ch == str(2)):
                                    mangt.ViewDonorData()
                                elif(ch == str(3)):
                                    stck.addStockDetails()
                                    stck.totalQuantity()
                                    stck.discardStockDetails()
                                elif(ch == str(4)):
                                    mangt.viewStock()
                                elif(ch == str(5)):
                                    bloodgrp = input("blood grp to check its avilable or not: ")
                                    if(bloodgrp in 'A+','A-','B+','B-','AB+','AB-','O+','O-'):
                                        mangt.checkAvailofBlood(bloodgrp)
                                    else:
                                        print("please Enter Correct blood group: ")
                                        bloodgrp = input("blood grp to check its avilable or not: ")
                                elif(ch == str(6)):
                                    rname = input("Enter Receiver name: ")
                                    rgender = input("Enter receiver Gender: ")
                                    rdate = input("Enter Blood Receive date: ")   
                                    rtime = input("Enter Blood Receive time: ")
                                    rqunt = input("Enter Blood receive in ml quantity: ")
                                    rbldgrp = input("enter which blood grp is receive: ")
                                    if(rbldgrp in 'A+','A-','B+','B-','AB+','AB-','O+','O-'):
                                        rbldgrp
                                    else:
                                        print("please Enter Correct blood group: ")
                                        rbldgrp = input("enter which blood grp is receive")
                                    pid = input("Enter id of Donator: ")
                                    hosptname = input("Enter Hospital name: ")
                                    '''time = input()
                                    date = input()
                                    quantity = input()'''
                                    r1 = receiver(pid,rname,rgender,rdate,rtime,rqunt,rbldgrp,hosptname)
                                    mangt.addReceiverData(r1)
                                elif(ch == str(7)):
                                    mangt.ViewReceiverData()
                                elif(ch == str(8)):
                                    id = str(input("Enter a Donor id to be search: "))
                                    mangt.searchDonorbyId(id)
                                elif(ch == str(9)):
                                    Name = input("Enter a Donor name to be search: ")
                                    mangt.searchDonorbyName(Name)
                                elif(ch == str(10)):
                                    id = input("Enter a receiver ID to be search: ")
                                    mangt.SearchbyReceiverID(id)
                                elif(ch == str(11)):
                                    name = input("Enter a receiver name to be search: ")
                                    mangt.SearchbyReceivername(name)
                                elif(ch == str(12)):
                                    print("Thank You!!")
                            else:
                                print("please enter number between 1 to 14!!")
                        except ValueError:
                            print("Please enter only number!!")
                else:
                    print("Please enter valid authentication details!!")
                    #user_name = input("Enter a Username: ")
                    #pass_word = input("Enter a  password: ")
            #Looking for Blood
            if(ch == str(2)):
                while(ch != str(5)):
                    print('''
                    1. view Stock Details
                    2. check availability of blood by (blood group and Quantity)
                    3. Search Donor Details by id
                    4. Search Donor Details by name
                    5. Exit
                    ''')
                    try:
                        ch = str(int(input("Enter your choice: ")))
                        if(ch == str(1)):
                            mangt.ViewDonorData()
                        elif(ch == str(2)):
                            bloodgrp = input("blood grp to check its avilable or not: ")
                            if(bloodgrp in 'A+','A-','B+','B-','AB+','AB-','O+','O-'):
                                mangt.checkAvailofBlood(bloodgrp)
                            else:
                                print("please Enter Correct blood group: ")
                                bloodgrp = input("blood grp to check its avilable or not: ")
                        elif(ch == str(3)):
                                id = str(input("Enter a Donor id to be search: "))
                                mangt.searchDonorbyId(id)
                        elif(ch == str(4)):
                            Name = input("Enter a Donor name to be search: ")
                            mangt.searchDonorbyName(Name)
                        elif(ch == str(5)):
                            print("Thnaku")
                    except ValueError:
                        print("Please enter only!!")
            #Want to Donate Blood
            if(ch == str(3)):
                #while(ch != str(2)):
                print('''
                    Please contact on xxxxxxxxxx
                            or
                    email id - xxxxxxxx@gmail.com''')
            if(ch == str(4)):
                print("Thank you!!")
        except ValueError:
            print("Please enter only number!!")