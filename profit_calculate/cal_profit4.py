import os 
import time 
from collections import defaultdict


import datetime
import matplotlib.dates as mdates

import matplotlib.pyplot as plt 
import pandas as pd 
import matplotlib.transforms as mtransforms 
import time  
import os 


import datetime
pwd  = os.getcwd()

CURRENT_BALANCE =0

file_name_ = "paper_000BNBBTC.txt"
print (pwd)


def count_trades(trades_):
    BUY_X = 0
    SELL_X = 0
  #  print (trades_)
    BUYS_SUM = 0 
    SELLS_SUM = 0 




    for item in trades_:
        line = item.split()
        if line[4] ==  "BUY"  :
            BUY_X += 1 
        elif line[4] == "SELL":
            SELL_X += 1

        if BUY_X == SELL_X : 
            print (BUY_X , SELL_X)
    
    print ("########  BUY_X  " , BUY_X , "########  SELL_X  ", SELL_X)




def read_file (file_name_ , CURRENT_BALANCE):

    buy_dict = [] 
    sell_dict = [] 
    
    fee_sum = 0 

    x_ = 0
    y_ = 0


    with open (file_name_ , 'r') as f_handler:
        trades = f_handler.readlines()

    count_ = count_trades(trades_=trades)
    return 
    #print ( count_ )

    profit_dates = [] 
    profit_lst = [] 

   

    ALL_DATES = []
    ALL_TRADES = [] 

    SELLS_DATES = [] 
    BUYS_DATES = []
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
        ALL_TRADES.append(float(item[3]))


        if item[4] ==  "BUY"  and len(BUYS_) < count_:
            BUYS_DATES.append(dt)
            BUYS_.append(line[3])

            BUYS_SUM += float(float(item[3])) 
            total_value = float(item[2]) * float(item[3])   
            BUY_total.append (total_value)


            fee = 0.00075 
            AMT = float(item[2]) 
            fee_sum += float(AMT)* float(fee)
            total_value2 = total_value - ((float(AMT * fee )*float(item[3])))

            x_ +=1
             
  

        elif item[4] == "SELL"  and len(SELLS_) < count_:
            SELLS_DATES.append(dt)

            SELLS_.append(line[3])  
            SELLS_SUM += float(float(item[3]))

            fee = 0.00075 
            AMT = float(item[2]) 
            fee_sum += float(AMT * fee )

            y_ +=1


        if x_ == y_ :   
            xx = 10278
            x = SELLS_SUM - BUYS_SUM  
            print (x_ , y_)
            print ( SELLS_SUM - BUYS_SUM )
            print ("###################################################################")
            print ( " ####average buy price = " , BUYS_SUM/len(BUYS_) , "\n" , "####average sell price = ", SELLS_SUM/len(SELLS_) )
            print (" with fees : " , x - float(fee_sum*0.00253) , " BTC")
            print (" with fees : " , (x - float(fee_sum*0.00253))*xx , " US DOLLAR ")
            print ( "Total fee = ", fee_sum , " BNB")
            print (" Total amount of bought bitcoin " , BUYS_SUM)
            print ( " Total amount of bitcoin sold  " , SELLS_SUM)
            print ("###################################################################")      
            profit_lst.append(float(BUYS_SUM/len(BUYS_)))
            profit_dates.append(dt)


    plt.rcParams['axes.facecolor'] = 'grey'
    plt.grid(color='black')
    plt.matplotlib.pyplot.title(file_name_)



   # print (ALL_TRADES , ALL_DATES )
    #print ( profit_dates)
    plt.scatter(profit_dates , profit_lst, color='yellow' , label='profit_dates')
    plt.plot(   ALL_DATES , ALL_TRADES, color='blue' , label='market_price')
    

   # plt.show() 



    #plot2 = plt.figure(2)
   # plt.plot(SELLS_DATES , SELLS_, color='green' , label='BUY_trades ')
  #  plt.plot(BUYS_DATES , BUYS_, color='red' , label='SELL_trades')


  






read_file(file_name_=file_name_ , CURRENT_BALANCE=0 )




#balance = client.get_asset_balance(asset='BTC')