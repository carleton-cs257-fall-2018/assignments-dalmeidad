'''
    api-test.py
    Dawson d'ALmeida, 1 October 2018

    Basic program for performing two operations:
    getting a list of stock info and getting details about a single stock
    using the IEX API.

    Adapted from Jeff Ondich's example code show how to retrieve results from
    an HTTP-based API.

'''

import sys
import argparse
import json
import urllib.request
import requests

def get_list_of_stocks():
    '''This method returns a list of dictionaries containing information about the stocks
       accesible through the EIX API'''

    base_url = 'https://api.iextrading.com/1.0/{0}'
    url = base_url.format('tops')
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    stock_info_list = json.loads(string_from_server)
    stock_dictionary_list_to_return = []

    for stock_dictionary in stock_info_list:
        symbol = stock_dictionary['symbol']
        sector = stock_dictionary['sector']
        security_type = stock_dictionary['securityType']
        last_sale_price = stock_dictionary['lastSalePrice']
        last_sale_size = stock_dictionary['lastSaleSize']
        volume = stock_dictionary['volume']
        market_percent = stock_dictionary['marketPercent']

        stock_dictionary_list_to_return.append({'symbol':symbol,
                                                'sector':sector,
                                                'security_type':security_type,
                                                'last_sale_price':last_sale_price,
                                                'last_sale_size':last_sale_size,
                                                'volume':volume,
                                                'market_percent':market_percent})


    return(stock_dictionary_list_to_return)

def get_details_of_single_stock(stock_symbol):
    '''This method returns a dictionary containing information about the stock
       symbol provided by the user through the EIX API'''

    if stock_symbol == 'none':
        raise ValueError('None as symbol for single stock')

    base_url = 'https://api.iextrading.com/1.0/stock/{0}/{1}'
    url = base_url.format(stock_symbol, 'book')
    try:
        data_from_server = urllib.request.urlopen(url).read()
    except urllib.error.HTTPError:
        print()
        print('The symbol you provided is incorrect or is not included in this API.')
        raise

    string_from_server = data_from_server.decode('utf-8')
    stock_info_dictionary = json.loads(string_from_server)
    stock_dictionary_to_return = []

    company_name = stock_info_dictionary['quote']['companyName']
    symbol = stock_info_dictionary['quote']['symbol']
    primary_exchange = stock_info_dictionary['quote']['primaryExchange']
    sector = stock_info_dictionary['quote']['sector']
    latest_time = stock_info_dictionary['quote']['latestTime']
    latest_volume = stock_info_dictionary['quote']['latestVolume']
    open = stock_info_dictionary['quote']['open']
    close = stock_info_dictionary['quote']['close']
    high = stock_info_dictionary['quote']['high']
    low = stock_info_dictionary['quote']['low']

    stock_dictionary_to_return = {'company_name': company_name,
                                  'symbol': symbol,
                                  'primary_exchange': primary_exchange,
                                  'sector':sector,
                                  'latest_time':latest_time,
                                  'latest_volume':latest_volume,
                                  'open':open,
                                  'close':close,
                                  'high':high,
                                  'low':low}

    return(stock_dictionary_to_return)


def main(args):
    if args.info_type == 'list':
        stock_list = get_list_of_stocks()

        for stock_info_dictionary in stock_list:

            symbol = stock_info_dictionary['symbol']
            sector = stock_info_dictionary['sector']
            security_type = stock_info_dictionary['security_type']
            last_sale_price = stock_info_dictionary['last_sale_price']
            last_sale_size = stock_info_dictionary['last_sale_size']
            volume = stock_info_dictionary['volume']
            market_percent = stock_info_dictionary['market_percent']

            print()
            print('{0} [Sector: {1}, Security Type: {2}, Last Sale Price: {3}, Last Sale Size: {4}, Volume: {5}, Market Percent: {6}]'
                                                 .format(symbol,
                                                         sector,
                                                         security_type,
                                                         last_sale_price,
                                                         last_sale_size,
                                                         volume,
                                                         market_percent))

    elif args.info_type == 'single_stock':
        stock_info = get_details_of_single_stock(args.stock_symbol)

        company_name = stock_info['company_name']
        symbol = stock_info['symbol']
        primary_exchange = stock_info['primary_exchange']
        sector = stock_info['sector']
        latest_time = stock_info['latest_time']
        latest_volume = stock_info['latest_volume']
        open = stock_info['open']
        close = stock_info['close']
        high = stock_info['high']
        low = stock_info['low']
        print()
        print('{0} ({1}) [Primary Exchange: {2}, Sector: {3}, Latest Time: {4}, Latest Volume: {5}, Open: {6}, Close: {7}, High: {8}, Low: {9}]'
                                             .format(company_name,
                                                     symbol,
                                                     primary_exchange,
                                                     sector,
                                                     latest_time,
                                                     latest_volume,
                                                     open,
                                                     close,
                                                     high,
                                                     low))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get stock info from IEX API')

    parser.add_argument('info_type',
                        metavar='info_type',
                        help='The type of info the user wants returned (list or single)',
                        choices=['list', 'single_stock'])

    parser.add_argument('stock_symbol',
                        metavar='stock_symbol',
                        help='The specific stock the user is interested in, will not affect a list request',
                        default='none')

    args = parser.parse_args()

    main(args)
