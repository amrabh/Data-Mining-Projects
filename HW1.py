"""
HW - 1 Fall 2019 CS636101
Author: Amruta Abhyankar njitid = aa2348
"""
import numpy as np


def correlation():
    # Getting the data from the csv files
    my_data1 = np.genfromtxt('AAPL.csv', delimiter=',')
    my_data2 = np.genfromtxt('AMZN.csv', delimiter=',')
    my_data3 = np.genfromtxt('FB.csv', delimiter=',')
    my_data4 = np.genfromtxt('GOOG.csv', delimiter=',')
    my_data5 = np.genfromtxt('IBM.csv', delimiter=',')
    my_data6 = np.genfromtxt('MSFT.csv', delimiter=',')

    # Getting the Adj Close
    AAPL1 = np.array(my_data1[:,5])
    AMZN1 = np.array(my_data2[:,5])
    FB1 = np.array(my_data3[:,5])
    GOOG1 = np.array(my_data4[:,5])
    IBM1 = np.array(my_data5[:,5])
    MSFT1 = np.array(my_data6[:,5])

    # Removing the headers
    AAPL2 = np.delete(AAPL1,0)
    AMZN2 = np.delete(AMZN1,0)
    FB2 = np.delete(FB1,0)
    IBM2 = np.delete(IBM1,0)
    GOOG2=np.delete(GOOG1,0)
    MSFT2 = np.delete(MSFT1,0)

    # Creating the dictionary using the
    allprices = {
        'IBM': IBM2,
        'MSFT': MSFT2,
        'GOOG': GOOG2,
        'AAPL': AAPL2,
        'AMZN': AMZN2,
        'FB': FB2
    }
    # keys are the names of the stocks
    keys_corrcoef = list(allprices.keys())
    corrcoefs = np.corrcoef(
        [allprices.get(x,0) for x in keys_corrcoef]
    )

    # Calculated Pearson Coefficients stored in a dictionary
    calc_coeff={}
    for i in range(0,len(keys_corrcoef)):
        for j in range(0, len(keys_corrcoef)):
            calc_coeff[keys_corrcoef[i],':',keys_corrcoef[j]] = round(corrcoefs[i][j],3)

    # Calculated Pearson coefficient finding uniques
    result = {}
    for key,value in calc_coeff.items():
        if value not in result.values():
            result[key] = value

    # removing coefficients of the same stocks
    result.pop(('IBM', ':', 'IBM'),None)
    result.pop(('MSFT', ':', 'MSFT'),None)
    result.pop(('GOOG', ':', 'GOOG'),None)
    result.pop(('AAPL', ':', 'AAPL'),None)
    result.pop(('AMZN', ':', 'AMZN'),None)
    result.pop(('FB', ':', 'FB'),None)


    # Printing the coefficients in descending order
    sorted_result = sorted(result, key=result.get, reverse=True)
    for r in sorted_result:
        print(r, '=', result[r])


correlation()