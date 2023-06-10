print("Hello and welcome to our hotel. We hope you have a wonderful experience staying at our place :) ")

import random
import mysql.connector
mydb=mysql.connector.connect(host='localhost',database='hotel',user='root',password='dps')
mycursor=mydb.cursor( )
guestno=random.randint(100,99999)
abv=input('Please enter your desired abbreviation (For exaple Mr. , Mrs. , Lt. etc)')
fname=input("Please enter your First name")
lname=input("Please enter your Last name")
name= abv+' '+fname+''+lname
print("Welcome", name, "your guest number is", guestno)
cidate=input("Enter Check-In Date in the format YYYY-MM-DD")
codate=input("Enter Check-Out Date in the format YYYY-MM-DD")
nod=int(input("enter number of days "))

car=input("Enter your car plate number")
vallet=int(input("did you opt for vallet parking ; press 1 for yes ; press 2 for no"))
if vallet==1:
    vp='Y'
else :
    vp='N'

print("Please choose a room type")
print("Please press 1 for our Premium Suites")
print("Please press 2 for our Ordinary room")
room=int(input("Please enter the type of room you wish for"))
if room==1:
    import random
    roomno=random.randint(100,999)
    print("You chose our Premium Suite")
    print("These rooms are considered the best in this country" )
    print("The per day price is 50,000 INR")
    print("Your room number is", roomno)
    print("Please proceed to your room. Your luggage will reach there safe and sound")
    floor= roomno//100
    print("Your room is on level", floor)
    b=50000*nod
elif room==2:
    import random
    roomno=random.randint(1000,9999)
    print("You chose our Ordinary Room")
    print("These rooms are considered the second best in this country" )
    print("..... only after our premium suites ofcourse")
    print("The per day price is 25,000 INR")
    print("Your room number is", roomno)
    print("Please proceed to your room. Your luggage will reach there safe and sound")
    floor= roomno//1000
    level= floor + 9
    print("Your room is on level", level)
    b=25000*nod


sql= "insert into guest_info (name,Guest_no,Car_Number_plate, Vallet_Parking, Room_No, checkin_date, checkout_date) values (%s, %s, %s, %s, %s, %s, %s)"
val= (name,guestno,car,vp,roomno,cidate,codate)
mycursor.execute(sql, val)
mydb.commit( )
print("record inserted")  



print("if you wish to proceed to the online casino and play lucky 7, press 1")
print("if you wish to play a game to kill time, press 2")
print("if you don't wish to play , press any other key")
n=int(input("Enter here"))
mydb=mysql.connector.connect(host='localhost',database='hotel',user='root',password='dps')
mycursor=mydb.cursor( )

if(n==1):
    print(" welcome to the game of Lucky 7. Please enjoy with social distancing from the comforts of your room")
    print(" if the diece lands at the same place as you have placed the money, you win")
    print(" if you win, you will recieve twice the money you placed as bet")
    print(" if you lose, you will lose the money you placed as bet")
    print("The money will be dispayed on the table and you can cash it when you check out")
    print(" LET'S PLAY!!!")
    
    bet=int(input("enter the amount that you wish to bet"))
    
    import random
    print("if below 7, then enter a number less than 7 ")
    print("if above 7, then enter a number more than 7")
    print("if 7, enter 7 ")
    luck=int(input("where do you wish to place your money??"))
    b=random.randint(2,12)
    a=1
    i=0
    while a==1:
        if(b>7):
            print("the dice showed",b,"which is above 7")
            if(luck>7):
                print("you put your money on above 7")
                if(b<7) and (luck<7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b>7) and (luck>7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b==7) and (luck==7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                else:
                    print("sorry, you lost ", bet)
                    k=bet * -1
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))

            elif(luck==7):
                print("you put your money on 7")
                if(b<7) and (luck<7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b>7) and (luck>7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b==7) and (luck==7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                else:
                    print("sorry, you lost ", bet)
                    k=bet * -1
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))


            elif(luck<7):
                print("you put your money on below 7")
                if(b<7) and (luck<7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b>7) and (luck>7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b==7) and (luck==7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                else:
                    print("sorry, you lost ", bet)
                    k=bet * -1
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))


        elif(b==7):
            print("the dice showed",b,"which is 7")

            if(luck>7):
                print("you put your money on above 7")
                if(b<7) and (luck<7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b>7) and (luck>7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b==7) and (luck==7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                else:
                    print("sorry, you lost ", bet)
                    k=bet * -1
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))


            elif(luck==7):
                print("you put your money on 7")
                if(b<7) and (luck<7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b>7) and (luck>7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b==7) and (luck==7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                else:
                    print("sorry, you lost ", bet)
                    k=bet * -1
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))

            elif(luck<7):
                print("you put your money on below 7")
                if(b<7) and (luck<7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b>7) and (luck>7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b==7) and (luck==7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                else:
                    print("sorry, you lost ", bet)
                    k=bet * -1
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
        
        elif (b<7):
            print("the dice showed",b,"which is below 7")

            if(luck>7):
                print("you put your money on above 7")
                if(b<7) and (luck<7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b>7) and (luck>7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b==7) and (luck==7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                else:
                    print("sorry, you lost ", bet)
                    k=bet * -1
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))

            elif(luck==7):
                print("you put your money on 7")
                if(b<7) and (luck<7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                   
                elif(b>7) and (luck>7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                   
                    
                elif(b==7) and (luck==7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    
                else:
                    print("sorry, you lost ", bet)
                    k=bet * -1
                    i=i+k
                    

            elif(luck<7):
                print("you put your money on below 7")
                if(b<7) and (luck<7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b>7) and (luck>7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                elif(b==7) and (luck==7):
                    print("congractulations, you won ", 2*bet)
                    k=2*bet
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))
                else:
                    print("sorry, you lost ", bet)
                    k=bet * -1
                    i=i+k
                    a=int(input("If you wish to play again, press 1, else press any other number"))

    

    money=i
    Game_no=1
    e= "insert into games (Guest_no,Game_no,money) values (%s, %s, %s,)"
    g= (Guest_no,Game_no,money)
    mycursor.execute(e, g)
    mydb.commit( )
    print("record inserted")  
elif(n==2):
    bet=int(input("enter the amount that you wish to bet"))
    print(" welcome to the game of capitals")
    print(" Guess the name of the capital of the countries correctly to win!")
    print(" for every correct answer, you gain 1.5 times the amount you bet")
    print(" for every incorrect answer, you lose the amount you placed as bet along with 200 as interest")
    a=1
    l=0
    while a==1:
        print(" LET'S PLAY!")
        print("write the first letter of the city in capital")
        p=input("what is the capital of Australia?")
        if(p=="Sydney") or (p=="sydney"):
            prize1=bet/2
            amt1=bet+prize1
            print("correct, you won ", amt1)
            
        else:
            print("Sorry, wrong answer, you lost ", bet)
            amt1=-200

        q=input("what is the capital of France?")
        if(q=="Paris") or (q=="paris"):
            prize2=bet/2
            amt2=bet+prize2
            print("correct, you won ", amt2)

        else:
            print("Sorry, wrong answer, you lost ", bet)
            amt2=-200

        r=input("what is the capital of Germany?")
        if(r=="Berlin") or (r=="berlin"):
            prize3=bet/2
            amt3=bet+prize3
            print("correct, you won ", amt3)

        else:
            print("Sorry, wrong answer, you lost ", bet)
            amt3=-200

        s=input("what is the capital of The United Kingdom?")
        if(s=="London") or (s=="london"):
            prize4=bet/2
            amt4=bet+prize4
            print("correct, you won ", amt4)

        else:
            print("Sorry, wrong answer, you lost ", bet)
            amt4=-200

        tamt=amt1+amt2+amt3+amt4
        if tamt>0:
            print("You gained",tamt)
            k= tamt
        else:
            print("You lost",-1*tamt) 
            k= (-1*bet) + (-1*tamt)
        l=l+k
        a=int(input("If you wish to play again, press 1, else press any other number"))

    money=l
    Game_no=2
    e= "insert into games (Guest_no,Game_no,money) values (%s, %s, %s,)"
    g= (Guest_no,Game_no,money)
    mycursor.execute(e, g)
    mydb.commit( )
    print("record inserted") 



else :pass
        
    






h=0



m=int(input("If you wish to order anything from our menu press 1, else press any other key"))
if m== 1:
    a=1
    while a==1:
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost',database='hotel',user='root',password='dps')
        mycursor=mydb.cursor( )
        
        print("please select what do you wish to order")
        print("press 1 to order green tea for Rs. 100")
        print("press 2 to order cappuccino for Rs. 100")
        print("press 3 to order cold drink for Rs. 50")
        print("press 4 to order mac n cheese for Rs. 250")
        print("press 5 to order non veg pizza for Rs. 600")
        print("press 6 to order mozzarella cheese pizza for Rs. 550")
        print("press 7 to order veg fried rice for Rs. 300")
        print("press 8 to order chicken fried rice for Rs. 350")
        print("press 9 to order veg hakka noodles for Rs. 400")
        print("press 10 to order chicken hakka noodles for Rs. 450")
        print("press 11 to order veg manchurian for Rs. 200")
        print("press 12 to order non veg manchurian for Rs. 250")
        print("press 13 to order chilli chicken for Rs. 350")
        print("press 14 to order chilli paneer for Rs. 300")
        order=input("what do you wish to order")
        if (order ==1):
            item = "green tea"
            money ="100"
            r=100
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==2):
            item = "cappuccino"
            money ="100"
            r=100
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==3):
            item = "cold drink"
            money ="50"
            r=50
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==4):
            item = "mac n cheese"
            money ="250"
            r=250
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==5):
            item = "non veg pizza"
            money ="600"
            r=600
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==6):
            item = "mozzarella cheese pizza"
            money ="550"
            r=550
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==7):
            item = "veg fried rice"
            money ="300"
            r=300
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==8):
            item = "chicken fried rice"
            money ="350"
            r=350
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==9):
            item = "veg hakka noodles"
            money ="400"
            r=400
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==10):
            item = "chicken hakka noodles"
            money ="450"
            r=450
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==11):
            item = "veg manchurian"
            money ="200"
            r=200
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==12):
            item = "non veg manchurian"
            money ="250"
            r=250
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==13):
            item = "chilli chicken"
            money ="350"
            r=350
            x= "insert into menu (Guest_no,item,money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        elif(order ==14):
            item = "chilli paneer"
            money ="300"
            r=300
            x= "insert into menu (Guest_no,Item,Money) values ( '%s', '%s','%s')"
            y= (name,guestno,item,money)
            mycursor.execute(x, y)
            mydb.commit( )
            print("record inserted")
            h=h+r
        
       
        a=int(input("If you wish to order anything else, press 1, else pressany other numeric key"))
    

else:pass










s=0

l=int(input("If you wish to give anything for laundry, please press 1, else press any other key"))
if l== 1:
    a=1
    while a==1:
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost',database='hotel',user='root',password='dps')
        mycursor=mydb.cursor( )
        print("please select what do you wish to give for laundry. We will have the item washed/drycleaned and delivered to your room")
        print("press 1 to give a top for Rs. 100")
        print("press 2 to give a lower for Rs. 200")
        print("press 3 to give a suit for Rs. 300")
        print("press 4 to give a saree for Rs. 500")
        print("press 5 to give a jacket for Rs. 100")
        order=input("what do you wish give for laundry")
        if (order ==1):
            item = "top"
            money ="100"
            f=100
            x= '''insert into laundry values ( '%s', '%s','%s')'''%(Guest_no,Item,Money)
            mycursor.execute(x)
            mydb.commit( )
            print("record inserted")
            s=s+f
        elif(order ==2):
            item = "lower"
            money ="200"
            f=200
            x= '''insert into laundry values ( '%s', '%s','%s')'''%(Guest_no,Item,Money)
            mycursor.execute(x)
            mydb.commit( )
            print("record inserted")
            s=s+f
        elif(order ==3):
            item = "suit"
            money ="300"
            f=300
            x= '''insert into laundry values ( '%s', '%s','%s')'''%(Guest_no,Item,Money)
            mycursor.execute(x)
            mydb.commit( )
            print("record inserted")
            s=s+f
        elif(order ==4):
            item = "saree"
            money ="500"
            f=500
            x= '''insert into laundry values ( '%s', '%s','%s')'''%(Guest_no,Item,Money)
            mycursor.execute(x)
            mydb.commit( )
            print("record inserted")
            s=s+f
        elif(order ==5):
            item = "jacket"
            money ="100"
            f=100
            x= '''insert into laundry values ( '%s', '%s','%s')'''%(Guest_no,Item,Money)
            mycursor.execute(x)
            mydb.commit( )
            print("record inserted")
            s=s+f
        
        
       
        
        a=int(input("If you wish to order anything else, press 1, else pressany other numeric key"))
        
        

else: pass


bills=b+l+h+s


u= '''insert into bills values ('%s', '%s', '%s')'''%(name,guestno,bills)
mycursor.execute(u)
mydb.commit( )
print("record inserted") 
print("Thank you. We hope you enjoyed your stay with us as much as we did")
print("Your Bill is", bills)





    
