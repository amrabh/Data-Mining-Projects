import pandas as pd
import numpy as np
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:41:28 2019

@author: Amruta Abhyankar NJITID-aa2348
"""
import pandas as pd
data1 = pd.read_csv("AAPL.csv")
data2 = pd.read_csv("AMZN.csv")
data3 = pd.read_csv("FB.csv")
data4 = pd.read_csv("GOOG.csv")
data5 = pd.read_csv("IBM.csv")
data6 = pd.read_csv("MSFT.csv")

print('Apple Dividend')
#Dividend Calculation for AAPL#
data1['CloseRatio']=data1['Close'].div(data1['Close'].shift(1))
data1['AdjCloseRatio']=data1['Adj Close'].div(data1['Adj Close'].shift(1))
data1['Dividend']=(data1['CloseRatio']-data1['AdjCloseRatio'])*(data1['Close'])
aapl_Dividend=data1[['Date','Dividend']].copy()
aapl_Dividend = aapl_Dividend[aapl_Dividend['Dividend']>0.000000000]
print(aapl_Dividend)

print('Amazon Dividend')
#Dividend Calculation for AMZN#
data2['CloseRatio']=data2['Close'].div(data2['Close'].shift(1))
data2['AdjCloseRatio']=data2['Adj Close'].div(data2['Adj Close'].shift(1))
data2['Dividend']=(data2['CloseRatio']-data2['AdjCloseRatio'])*(data2['Close'])
amzn_Dividend=data2[['Date','Dividend']].copy()
amzn_Dividend = amzn_Dividend[amzn_Dividend['Dividend']>0.000000000]
print(amzn_Dividend)

print('Facebook Dividend')
#Dividend Calculation for FB#
data3['CloseRatio']=data3['Close'].div(data3['Close'].shift(1))
data3['AdjCloseRatio']=data3['Adj Close'].div(data3['Adj Close'].shift(1))
data3['Dividend']=(data3['CloseRatio']-data3['AdjCloseRatio'])*(data3['Close'])
fb_Dividend=data3[['Date','Dividend']].copy()
fb_Dividend = fb_Dividend[fb_Dividend['Dividend']>0.000000000]
print(fb_Dividend)

print('Google Dividend')
#Dividend Calculation for GOOG#
data4['CloseRatio']=data4['Close'].div(data4['Close'].shift(1))
data4['AdjCloseRatio']=data4['Adj Close'].div(data4['Adj Close'].shift(1))
data4['Dividend']=(data4['CloseRatio']-data4['AdjCloseRatio'])*(data4['Close'])
goog_Dividend=data4[['Date','Dividend']].copy()
goog_Dividend = goog_Dividend[goog_Dividend['Dividend']>0.00000000000000]
print(goog_Dividend)

print('IBM Dividend')
#Dividend Calculation for IBM#
data5['CloseRatio']=data5['Close'].div(data5['Close'].shift(1))
data5['AdjCloseRatio']=data5['Adj Close'].div(data5['Adj Close'].shift(1))
data5['Dividend']=(data5['CloseRatio']-data5['AdjCloseRatio'])*(data5['Close'])
ibm_Dividend=data5[['Date','Dividend']].copy()
ibm_Dividend = ibm_Dividend[ibm_Dividend['Dividend']>0.000000000]
print(ibm_Dividend)

print('MicrSoft Dividend')
#Dividend Calculation for MSFT#
data6['CloseRatio']=data6['Close'].div(data6['Close'].shift(1))
data6['AdjCloseRatio']=data6['Adj Close'].div(data6['Adj Close'].shift(1))
data6['Dividend']=(data6['CloseRatio']-data6['AdjCloseRatio'])*(data6['Close'])
msft_Dividend=data6[['Date','Dividend']].copy()
msft_Dividend = msft_Dividend[msft_Dividend['Dividend']>0.000000000]
print(msft_Dividend)