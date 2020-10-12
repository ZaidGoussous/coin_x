import os 
import time 
from collections import defaultdict


import datetime
pwd  = os.getcwd()

CURRENT_BALANCE =0

print (pwd)


def count_trades(trades_):
    BUY_X = 0
    SELL_X = 0
  #  print (trades_)
    for item in trades_:
        line = item.split()
        if line[4] ==  "BUY"  :
            BUY_X += 1 
        elif line[4] == "SELL":
            SELL_X += 1
    print ("########  BUY_X  " , BUY_X , "########  SELL_X  ", SELL_X)

    if BUY_X > SELL_X:
        return SELL_X
    elif SELL_X > BUY_X:
        return BUY_X
    elif BUY_X == SELL_X:
        return BUY_X

def read_file (file_name_ , CURRENT_BALANCE):

    buy_dict = [] 
    sell_dict = [] 
    
    fee_sum = 0 

    x_ = 0
    y_ = 0


    with open (file_name_ , 'r') as f_handler:
        trades = f_handler.readlines()

   # count_ = count_trades(trades_=trades)


    

    ALL_DATES = []
    BUYS_ = [] 
    SELLS_ = []


    BUY_total = []
    SELL_total = []




    BUYS_SUM = 0 

    SELLS_SUM = 0 


    print ( len(trades))
    for line in trades:


        item = line.split()
        ### ADD TIME TO ALL_DATES LST 
        dt = item[0] + ' ' + item[1]
        dt = datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M:%S')
        ALL_DATES.append(dt)


        ### ADD BUY ORDERS TO BUYS_ LST     
        

        if item[4] ==  "BUY"  :#and len(BUYS_) < count_:

            BUYS_.append(line[3])

            BUYS_SUM += float(float(item[3])) 
            total_value = float(item[2]) * float(item[3])   
            BUY_total.append (total_value)

            ### fee calculation   ( AMT * fee ) 
            # the fee is 0.00075 for bnb pairs 

            fee = 0.00075 
            AMT = float(item[2]) 
            fee_sum += float(AMT)* float(fee)
            total_value2 = total_value - ((float(AMT * fee )*float(item[3])))

            x_ +=1
             
         ### ADD SELL ORDERS TO SELLS_ LST 

        elif item[4] == "SELL" :# and len(SELLS_) < count_:

            SELLS_.append(line[3])  
            SELLS_SUM += float(float(item[3]))

            fee = 0.00075 
            AMT = float(item[2]) 
            fee_sum += float(AMT * fee )

            y_ +=1



        




    print (len(ALL_DATES) , " len(ALL_DATES)" )
    print (len(BUYS_) , " len(BUYS_) ")
    print (len(SELLS_) , " len(SELLS_) ")

  #  print ( len(BUYS_) / len(ALL_DATES), " len(BUYS_) / len(ALL_DATES)   <---- this is the BUY percentage ")

  #  print ( len(SELLS_) / len(ALL_DATES), " len(SELLS_) / len(ALL_DATES) <---- this is the SELL percentage ")

    ### out put the average buy price and the average sell price 

    



    print ( len(SELLS_) - len(BUYS_) , "len(SELLS_) - len(BUYS_)")

    print ( len(BUYS_) - len(SELLS_) , "len(BUYS_) - len(SELLS_)")


    ### buy percentage is len(BUYS_) / len(ALL_DATES)
    ### sell percentage is len(SELLS_) / len(ALL_DATES)
    
    



    xx = 10278
    x = SELLS_SUM - BUYS_SUM  
    print ( x , ":   ABS  value SELLS_SUM - BUYS_SUM ")


 #  print (( BUYS_SUM - SELLS_SUM)*xx )

    print ("###################################################################")
    print ( " ####average buy price = " , BUYS_SUM/len(BUYS_) , "\n" , "####average sell price = ", SELLS_SUM/len(SELLS_) )
    print (" with fees : " , x - float(fee_sum*0.00227) , " BTC")
    print (" with fees : " , (x - float(fee_sum*0.00227))*xx , " US DOLLAR ")
    print ( "Total fee = ", fee_sum , " BNB")
    print (" Total amount of bought bitcoin " , BUYS_SUM)
    print ( " Total amount of bitcoin sold  " , SELLS_SUM)
    print ("###################################################################")


    print (x_ , y_)
    