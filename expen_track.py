expdict={}
initial=0
add_initial={}   
k=0
current=0
#  print(add_initial)

for i in range(1,50):
    print()
    print('                 <<<<<<<<<<-------- EXPENCE TRACKER ------->>>>>>>>>>')
    print()
    print('1. INITIAL AMOUNT')
    print('2. ADD INITIAL AMOUNT')
    print('3. VIEW EXPENCE')
    print('4. ENTER EXPENCE ')
    print('5. EDIT EXPENCE')
    print('6. DELETE EXPENCE')
    print('7. EXIT')
    print()
    try:
        n=int(input("😎<<<<ENTER CHOICE :"))
    except:
        print("***somthing went wrong input ****")    
    
    if(n==1):
        print()
        f="amount"
        initial=int(input('<<---- ENTER YOUR INITIAL AMOUNT : '))
        add_initial[f]=initial
        v1=add_initial[f]
#  ---->>>  print(add_initial)
    if(n==2):
        print()
        if(initial==0):
            print()
            print('😡😡* MUST ENTER INITIAL AMOUNT *😡😡')
        else:   
            print('*** ADD YOUR INITIAL AMOUNT *** ')
            print()
            m = add_initial[f] #--> m for store 2 dict old value
            del add_initial[f] # --> delete value from 2 dict
            del v1
            k=int(input('<<<<HOW MUCH AMOUNT YOU WANT TO ADD:')) #--> input new value
            print()
            G=m+k    # G is a variable for store old value + new value
            add_initial[f]=G #--> 2nd dict to store updated value
            v1=G

# view  --------------
    if(n==3):
        if(initial==0):
            print()
            print('😡😡* MUST ENTER INITIAL AMOUNT *😡😡')
         
        else:   
            print()
            print('INITIAL AMOUNT:',add_initial[f])
            print('               -------')
            print()
            for y,z in expdict.items():
                print('---------------------')
                print('.',y,'     - ',z)
            
            print()
            v=0
            for x in expdict.values():
                v = v+x            
            print('TOTAL EXPENSE:',v)
            print('               -----')
            print()
            current=v1-v #--> for calculate current balane 
            if(v1<=0):
                print('🤪🤪🤪🤪🤪 MACHANE PANI PAALI BALANCE THEERNNU 🤪🤪🤪🤪🤪')
                print()
            else:
                print('CURRENT BALANCE:',current)
                print('                -----')
                print()        
# enter expence ------------
    if(n==4):
        print()
        if v1<=0:
            print(" YOUR BALANCE IS LOW ADD INITIAL AMOUNT !! ")
        else:    
            if v1<=0:
                print(" LOW BALANCE .... ")
            else:
                name=input("Enter expence :")
                if(name not in expdict):
                    value=int(input("Enter expence amount :"))
                    if (current-value<=0):
                        print("** INSUFICIENT BALANCE **")
                    else:    
                        expdict[name]=value
                    
                else:
                    print()
                    R=expdict[name]
                    del expdict[name]
                    value1=int(input('-- ENTER YOUR EXPENCE AMOUNT:'))
                    W=R+value1
                    if (current-value1<=0):
                        print("** INSUFICIENT BALANCE **")
                    else:
                        expdict[name]=W
        #print('🫣🫣* THIS NAME ALLREADY EXISTED *🫣🫣')                     

    if(n==5):
        print()
        print('<<<<<<<<<< EDIT EXPENSE >>>>>>>>>>')
        print()
        print("1.CHANGE EXPENSE NAME")
        print("2.CHANGE EXPENCE AMOUNT")
        print()
        n1=int(input("<<<<< ENTER YOUR CHOICE : "))
        if(n1==1):
            print()
            for y,z in expdict.items():
                print('---------------------')
                print('.',y,'     - ',z)
            c=input('WHICH EXPENCE NAME YOU WANT TO CHANGE:')
            print()
            if(c in expdict):
                print()
                x=expdict[c]
#***
                del expdict[c] 
                name_1=input("CHNAGE  NAME : ")
                expdict[name_1]=x
                
            else:
                print()
                print('🫣🫣🫣* THIS NAME NOT EXIST IN EXPENCE TRACKER *🫣🫣🫣')
                
        else:
            if(n1==2):
                print()
                for y,z in expdict.items():
                    print('---------------------')
                    print('.',y,'     - ',z)
                c1=input('WHICH EXPENCE NAME AMOUNT YOU WANT TO CHANGE:')
                if(c1 in expdict):
                    print()
                    number_1=int(input("CHANGE AMOUNT : "))
                    expdict[c1]=number_1    
                    
                else:
                    print()
                    print('🫣🫣🫣* THIS NAME NOT EXISTED *🫣🫣🫣')
                    
            else:
                
                print('🥺🥺*WRONG SELECTION *🥺🥺')
                            

        
    if(n==6):
        print()
        print('<<<<<<< DELETE EXPENCE >>>>>>>')
        print()
        for y,z in expdict.items():
            print('---------------------')
            print('.',y,'     - ',z)
        c2=input('WHICH EXPENCE NAME  YOU WANT TO DELETE:')
        print()
        if(c2 in expdict):
            del expdict[c2]  
            print()                       
            print("🫣🫣-DELETE SUCCESFULLY-🫣🫣")
            
        else:
            print("🫣🫣🫣<< THIS NAME NOT EXIST >>🫣🫣🫣")
    if(n==7):
        print()
        print('👋🏽👋🏽👋🏽👋🏽👋🏽<< TAATA GUD BY >>👋🏽👋🏽👋🏽👋🏽👋🏽')
        exit() 
            
    if(n>=8):
        print()
        print('🥺🥺🥺<<YOUR WRONG SELECTION>>🥺🥺🥺')
        print()
        