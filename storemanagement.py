"""
STORE MANAGEMENT SYSTEM

customer (cid,cname,cadd,cmob) 
product (pid,pname,price)
order (cid, pid , qty)

1. Add Customer
2. View All Customer
3. Delete A Customer
4. Add Product
5. View All Products
6. Update Product
7. Place An Order
8. View All Orders
9. View All Orders By CID
0. Exit

"""
# IMPORTING REQUIRED LIBRARIES
import pickle
import os

# A METHOD TO ADD A CUSTOMER INFORMATION
def addCustomer():
    file = open('customer.bin','ab')
    cid = input("\n\tEnter Customer ID : ")
    cname = input("\tEnter Customer Name : ")
    cadd = input("\tEnter Customer Address : ")
    cmob = input("\tEnter Customer Mobile : ")
    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmob,file)
    print("\n\tCustomer Added Successfully!")
    file.close()
    input("\tPress Enter To Continue...")

# A METHOD TO VIEW ALL CUSTOMER's INFORMAION
def viewAllCustomer():
    file = open('customer.bin','rb')
    try:
        while True:
            for i in range(4):
                data = pickle.load(file)
                print('\t',data,end="")
            print()
    except:
        print("\n\tHere is your all customer!")
    file.close()
    input("\tPress Enter To Continue...")

# A METHOD TO DELETE CUSTOMER's INFORMATION
def deleteCustomer():
    file1 = open('customer.bin','rb')
    file2 = open('temp.bin','ab')
    flag = 0
    cid = input("\n\tEnter Customer ID To Delete : ")
    try:
        while True:
            data = pickle.load(file1)
            if data==cid:
                pickle.load(file1)
                pickle.load(file1)
                pickle.load(file1)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==0:
            print("\n\tCustomer Not Found!")
        else:
            print("\n\tCustomer Deleted Successfully!")
    file1.close()
    file2.close()
    os.remove('customer.bin')
    os.rename('temp.bin','customer.bin')
    input("\tPress Enter To Continue...")

# A METHOD TO ADD A PRODUCT's INFORMATION
def addProduct():
    file = open('product.bin','ab')
    pid = input("\n\tEnter Product ID : ")
    pname = input("\tEnter Product Name : ")
    price = input("\tEnter Product Price : ")
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(price,file)
    print("\n\tProduct Added Successfully!")
    file.close()
    input("\tPress Enter To Continue...")

# A METHOD TO VIEW ALL PRODUCT's INFORMATION
def viewAllProducts():
    file = open("product.bin",'rb')
    try:
        while True:
            print("\n\tProduct ID :",pickle.load(file))
            print("\tProduct Name :",pickle.load(file))
            print("\tProduct Price :",pickle.load(file))
            print("\t*************************")
    except:
        print("\n\tHere is your all Products!")
    file.close()
    input("\tPress Enter To Continue...")

# A METHOD TO UPDATE A PRODUCT's INFORMATION
def updateProduct():
    file1 = open('product.bin','rb')
    file2 = open('temp.bin','ab')
    flag = 0
    pid = input("\n\tEnter Product ID To Update Price : ")
    try:
        while True:
            data = pickle.load(file1)
            if data==pid:
                pickle.dump(data,file2)
                name = pickle.load(file1)
                pickle.dump(name,file2)
                print("\tProduct Name : ",name)
                print("\tOld Price : ",pickle.load(file1))
                price = input("\tEnter New Price : ")
                pickle.dump(price,file2)
                flag = 1
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\tPrice Updated Successfully!")
        else:
            print("\n\tProduct Not Found!")
    file1.close()
    file2.close()
    os.remove('product.bin')
    os.rename('temp.bin','product.bin')
    input("\tPress Enter To Continue...")

# A METHOD TO GET THE INFORMATION OF A CUSTOMER
def getCustomer(id_):
    cus = []
    file = open('customer.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==id_:
                cus.append(data)
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
    except:
        pass
    file.close()
    return cus

# A METHOD TO GET THE INFORMATION OF A PRODUCT
def getProduct(id_):
    pro = []
    file = open('product.bin','rb')
    try:
        while True:
            data = pickle.load(file)
            if data==id_:
                pro.append(data)
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
    except:
        pass
    file.close()
    return pro

# A METHOD TO PLACE AN ORDER
def placeAnOrder():
    cid = input("\n\tEnter CID To Place Order : ")
    cus = getCustomer(cid)
    if len(cus)>0:
        print("\tCustomer Name :",cus[1])
        print("\tCustomer Address :",cus[2])
        pid = input("\n\tEnter Product ID To Order : ")
        pro = getProduct(pid)
        if len(pro)>0:
            print("\tProduct Name :",pro[1],)
            print("\tProduct Price :",pro[2],)
            qty = input("\n\tEnter Quantity : ")
            print("\tTotal Bill :",int(pro[2])*int(qty))
            print("\n\tOrder Placed Successfully!")
            file = open('order.bin','ab')
            pickle.dump(cid,file)
            pickle.dump(pid,file)
            pickle.dump(qty,file)
            file.close()
        else:
            print("\n\tProduct Not Found!")
    else:
        print("\n\tCustomer Not Found!")
    input("\tPress Enter To Continue...")

# A METHOD TO VIEW ALL ORDER's DETAILS
def viewAllOrders():
    file = open('order.bin','rb')
    oid = 1001
    try:
        while True:
            cus = getCustomer(pickle.load(file))
            pro = getProduct(pickle.load(file))
            qty = int(pickle.load(file))
            print("\tOrder ID :",oid)
            print("\tCustomer Name :",cus[1])
            print("\tCustomer Address :",cus[2])
            print("\tProduct Name :",pro[1])
            print("\tProduct Price :",pro[2])
            print("\tQuantity :",qty)
            print("\n\tTotal Bill :",int(pro[2])*qty,'/-')
            print("\t-----------------------\n")
            oid+=1
    except:
        print("\n\tHere is all the details")
    file.close()
    input("\tPress Enter To Continue...")

# A METHOD TO VIEW ORDERS BY CID
def viewOrderByCID():
    file = open('order.bin','rb')
    cid = input("\n\tEnter CID To Display Orders : ")
    try:
        while True:
            cus = getCustomer(pickle.load(file))
            pro = getProduct(pickle.load(file))
            qty = int(pickle.load(file))
            if cus[0]==cid:
                print("\tCustomer Name :",cus[1])
                print("\tCustomer Address :",cus[2])
                print("\tProduct Name :",pro[1])
                print("\tProduct Price :",pro[2])
                print("\tQuantity :",qty)
                print("\n\tTotal Bill :",int(pro[2])*qty,'/-')
                print("\t-----------------------\n")
    except:
        print("\n\tHere is all the details")
    file.close()
    input("\tPress Enter To Continue...")

# DASHBOARD / HOMEPAGE
while True:
    print("\n\t\tSTORE MANAGEMENT SYSTEM")
    print('''
        1. Add Customer
        2. View All Customer
        3. Delete A Customer
        4. Add Product
        5. View All Products
        6. Update Product
        7. Place An Order
        8. View All Orders
        9. View All Orders By CID
        0. Exit
    ''')
    ch = int(input("\tEnter Your Choice : "))
    if ch==0:
        print("\n\t\tBYE-BYE ADMIN!")
        break
    elif ch==1:
        addCustomer()
    elif ch==2:
        viewAllCustomer()
    elif ch==3:
        deleteCustomer()
    elif ch==4:
        addProduct()
    elif ch==5:
        viewAllProducts()
    elif ch==6:
        updateProduct()
    elif ch==7:
        placeAnOrder()
    elif ch==8:
        viewAllOrders()
    elif ch==9:
        viewOrderByCID()
    else:
        input("\n\tWrong Entered! Try Again!")
