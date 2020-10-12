
import time 
import os 

import smtplib

from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import sys 

coin1 = 'BTC'
coin2 = 'BNB'

bitcoin_price = 0
binance_price = 0




# setting up headless option for faster execution
options = Options()
options.headless = True

xpath_lst = [ 
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[1]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[2]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[3]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[4]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[5]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[6]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[7]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[8]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[9]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[10]',
    
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[12]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[13]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[14]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[15]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[16]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[17]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[18]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[19]',
    '/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[20]',

    
]

all_assets = [] 



"/html/body/div/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[1]"

sting_ = '/html/body/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div/table/tbody/tr'

lst_lst = [sting_+"["+str(item)+"]" for item in range (1 ,  21) ]

for n , item in enumerate(lst_lst):
    if n ==10:
        pass
    else:
    #    print (item) 
        pass
#sys.exit()






def send_alert(price ):
    


    usr_mail = "stormdesert12@gmail.com"
    pass_wrd = "1937putin"
    handle = smtplib.SMTP('smtp.gmail.com', 587)
    handle.starttls()
    handle.login(usr_mail , pass_wrd)
    handle.sendmail(usr_mail , usr_mail , price)
    handle.quit()


    print ( " Successfully sent email to :: " +  usr_mail)
    return 










def technical_cap():

    browser = (webdriver.Firefox(options=options, executable_path='E:/py_stuff/BIN_API_v3/python-binance-master/geckodriver'))
    browser.get('https://coinmarketcap.com/')

    print (browser.title)
   


    assert 'Cryptocurrency Prices, Charts And Market Capitalizations | CoinMarketCap' in browser.title

    for x_path in xpath_lst:
        tmp = [item.text.split('\n') for item in browser.find_elements_by_xpath(xpath=x_path)] 
        all_assets.append(tmp)



    browser.quit() 
    try:
        os.system("taskkill /IM firefox.exe /F")
    except:
        pass

#    return all_assets
### a function to calculate coin price and sends a mail to me 

#while True:

#    technical_cap()



#    for item in all_assets:
#        print (item)

       

#        print (item[0] , item[1], item[3].split(" ")[0])
#        print ("\n")    

#        if item[1] == coin1:
#            bitcoin_price = float(str(item[3].split(" ")[0]).replace("$", "").replace(",",""))
#        elif item[1] == coin2: 
#            binance_price = float(str(item[3].split(" ")[0]).replace("$", "").replace(",",""))
    

#    try:

#        res =  binance_price/bitcoin_price
#        print (str(res)," current Binance exhange rate  !!!!!!!!!!!!!!!!!!")
#    except:
#        pass

#    technical_cap()
    #send_alert(price=str(round(res , 9 )))

technical_cap()

for item in all_assets:
        #print (item[0])

       

        #print (item[0][0], item[0][1],item[0][2],item[0][3],item[0][4])
     #   print ("\n")    

        if item[0][2] == coin1:
            bitcoin_price = str(item[0][4]).replace('$', '').replace(',','')
        elif item[0][2] == coin2: 
            binance_price = str(item[0][4]).replace('$', '')
    


print ( bitcoin_price , binance_price) 
      #  print (binance_price.replace('$' , '' ) , bitcoin_price.replace('$', '' ))
res =  float(binance_price)/float(bitcoin_price)


print (str(res)," current Binance exhange rate  !!!!!!!!!!!!!!!!!!")
print ( " Bitcoin price = " , bitcoin_price , "\n" , "Binance price = " , binance_price  ) 



