# -*- coding: utf-8 -*-
"""

@author: alpcan
"""

import csv
import numpy as np
import json


def import_pricedata():
    ''' Imports wholesale electricity price from the AEMO file
        'GRAPH_5VIC1.csv' which should be in the same folder.
        returns the 30 min average prices as an array.

        This array should be aligned with the temperature data!
    '''

    filename = 'GRAPH_5VIC1.csv'
    prices = []
    with open(filename, 'r') as f:
        content = csv.reader(f)
        next(content)  # skip first row
        for row in content:
            prices.append(float(row[3]))  # retail price

    # convert to numpy array
    pricearray = np.array(prices)

    # calculate moving average of prices
    # to get 30mins out of 5 min data
    avg_prices = np.zeros(48)
    for i in range(48):
        avg_prices[i] = np.mean(pricearray[i * 6:(i + 1) * 6])

        # back to list from numpy array for convenience
    avg_pricelist = avg_prices.tolist()

    return avg_pricelist


## for debugging
## import prices
# prices=import_pricedata()
#
# print(prices)
# print(len(prices))





# imports RRP data from AEMO file
def import_tempdata():
    ''' Imports air temperature data from BOM file for Melbourne
        'IDV60901.94868.json' which should be in the same folder.
        returns the 30 min temperatures as an array.

        This array should be aligned with the AEMO price data!
    '''

    filename = 'IDV60901.94868.json'
    with open(filename, 'r', encoding='utf-8') as f:
        content = json.loads(f.read())

    # pretty print of the whole set to visualise it
    #
    # print(json.dumps(subset, sort_keys=True, indent=2, separators=(',', ': ')))

    # only interested in air temp
    subset = content['observations']['data']
    tempset = [item['air_temp'] for item in subset]

    # only first 44 match AEMO price data
    temperature = tempset[:44]

    return temperature

    ## for debugging
    # import temperature data
    # temperature=import_tempdata()
    #
    # print(len(temperature))
    # print(temperature)
