from coin__x import *
import time 
import os 
import random 
import requests



### the bot will have
### a score and every sucessful buy/sell pair 
### the bot get 1 point when it loses -3 points to the bot score



score = 0 

max_open_trades = 50


def log_trades(coin , time_date , quant , buy_sell  , order_type , current_price , t_ticker ):
    ### this function takes all the test orders and calculates the profit 
    res  = str(time_date) +"    "+ str(quant)+"    "+str(buy_sell)+"    "+ str(order_type)+"    "+ str(current_price) +"    "+ str(t_ticker)

    print (os.getcwd())
    print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    ### saves in the following format 
    ### time_date , quant , buy_sell (price) , type , current_price  

    with open("paper_000"+coin+".txt" , "a") as f_handle:
        f_handle.write(res)
        f_handle.write("\n")


    print ("logged result to paper_frame_work file ")
    print ("^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^^#^")
    return





def intro(item):
    
    n3w_coin = fetch_coin(coin=item)
    print (str(n3w_coin.coin) +"  "+ str(n3w_coin.coin_price))
    

    ## a list to hold all the predicted prices and prints out the average 

    predict_lsst = [] 

    #for i in range (2):    
    balance_ = n3w_coin.check_balance()
    n3w_coin.forecast_coin()

    n3w_coin.make_data() 
    
    coin_ticker , t_price,  L0SS = n3w_coin.predict_symbol(balance=balance_)

    predict_lsst.append(float(t_price))
    time.sleep(30)
    print ( "coin_ticker " , " t_price " )
   # print ( coin_ticker , "  " , t_price , "  ")
    print ("current price ", coin_ticker)
    print ("predicted price " , t_price)
    
#    print ( predict_lsst ) 


#    sum_ = 0 
#    for item in predict_lsst :
#        sum_ += float(item)

#    print ( " average prediction price :" , sum_/len(predict_lsst))

    print ("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    
#    t_price = float(sum_/len(predict_lsst))





    if n3w_coin.check_orders() < max_open_trades :



        try:
            #quant =  n3w_coin.MIN_QTY *  int (random.randrange(10, 20)) *10
            #quant = round(quant , 2)
            if float(coin_ticker) < float(t_price)and   ( float(t_price)/float(coin_ticker)-1) > float(0.002):

            ### if the current price is bigger than the target_price then coin_price is red 
            ### going down 



                try:
                    
                    ### i use this to test if the program executes orders at market price 
                    #n3w_coin.test_order(order_type="BUY" , predicted_price=str(coin_ticker))


                    n3w_coin.market_BUY()

    
                    log_trades(coin=n3w_coin.coin,
                        time_date=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(time.time())))),
                        quant='0.2',
                        buy_sell=coin_ticker,
                        order_type="BUY",
                        current_price=coin_ticker,
                        t_ticker=t_price )

                    print ("##############  logged trade to paper_000 file  ##############")

                    ### pass the order type , amt , price , predicted price 


                    TYPE_ = "BUY"
                    AMT_  = "0.2"
                    PRICE_ = str(coin_ticker)
                    PRED_PRICE  = str(t_price)






                except : 
                    print ("%%%%%%%%%%%%%%% DID NOT EXECUTE TEST ORDER %%%%%%%%%%%%%%% ")

                    print ("%%%%%%%%%%%%%%%         TYPE BUY           %%%%%%%%%%%%%%% ")





            elif float(t_price) <  float(coin_ticker) and  ( float(coin_ticker)/float(t_price)-1) > float(0.002):
                
            ### if the current price is lower than the target_price then coin_price is green 
            ### going up 


                try:
                    

                    ### i use this to test if the program executes orders at market price 
                  #  n3w_coin.test_order(order_type="SELL" , predicted_price=str(coin_ticker))
                    n3w_coin.market_SELL()

                    log_trades(coin=n3w_coin.coin,
                        time_date=(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(time.time())))),
                        quant='0.2',
                        buy_sell=coin_ticker,
                        order_type="SELL",
                        current_price=coin_ticker , 
                        t_ticker=t_price )

                    print ("##############  logged trade to paper_000 file  ##############")



                    ### pass the order type , amt , price , predicted price 


                    TYPE_ = "SELL"
                    AMT_  = "0.2"
                    PRICE_ = str(coin_ticker)
                    PRED_PRICE  = str(t_price)






                except : 
                    print ("%%%%%%%%%%%%%%% DID NOT EXECUTE TEST ORDER %%%%%%%%%%%%%%% ")
                     
                    print ("%%%%%%%%%%%%%%%         TYPE SELL          %%%%%%%%%%%%%%% ")
#





            else:
                return
        except BinanceAPIException as binance_error:

            print (binance_error)

        #time.sleep(10)






while True:

    #time.sleep(60)
    for item in my_coins:
        
        try:

            intro(item) 



        except requests.exceptions.Timeout as Time_out  :
            print ("Timeout occurred")
            print (Time_out)
            time.sleep(60)
        except requests.exceptions.ConnectionError as binance_error_2:
            print (binance_error_2)
            time.sleep(120)

    
