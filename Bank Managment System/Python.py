import mysql.connector as a
con=a.connect(host="localhost",
              user="root",
              password="1234",
              database="bank")
print("_*_*_*_*_*_*_*_*_*_*__*_*_*_*_*")
print("       Banking Managment       ")
print("_*_*_*_*_*_*_*_*_*_*__*_*_*_*_*")

def openacc():
    n=input("enter name:")
    ac=input("enter account no:")
    db=input("enter D.o.B:")
    p=input("enter Phone:")
    ad=input("enter Address:")
    ob=int(input("enter opening balance:"))
    data1 = (n,ac,db,p,ad,ob)
    data2=(n,ac,ob)
    sql='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert amount value(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data1)
    c.execute(sql2,data2)
    con.commit()
    print("Data Entered Successfully")
    main()
def depoamo():
    am=int(input("Enter Amount:"))
    ac=input("Enter Account No:")
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]+am
    sql="update amount set balance=%s where acno =%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("Amount deposited Successfully")
    main()
def witham():
    am=int(input("Enter Amount:"))
    ac=input("Enter Account No:")
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql="update amount set balance=%s where acno =%s"
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print("Amount withdraw successfully")
    main()
def balance():
    ac=input("Enter Acount NO:")
    a="select balance from amount where acno =%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("Balance for Amount:",ac,"is",myresult[0])
    main()
def dispacc():
    ac= input("Enter AcountNo:")
    a="select*from account where acno=%s"
    data =(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i,end=" ")
    main()
def closeac():
    ac=input("Enter Account No;")
    sql1="delete from account where acno =%s"
    sql2="delete from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    main()
def main():
    print('''
    1. OPEN NEW ACCOUNT
    2. DEPOSITE AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE ENQUIRY
    5. DISPLAY CUSTOMER DETAILS
    6. CLOSE AN ACCOUNT
          ''')
    choice =input("enter task no:")
    if(choice=='1'):
       openacc()
    elif(choice=='2'):
        depoamo()
    elif(choice=='3'):
        witham()
    elif(choice=='4'):
        balance()
    elif(choice=='5'):
        dispacc()
    elif(choice=='6'):
        closeac()
    else:
        print("wrong choice......")
        main()
main()
        
        
            
    
