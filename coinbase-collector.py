from cbpro.public_client import PublicClient
from datetime import datetime
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tool to download the order book and/or the trades data from Coinbase '
                                                 'Pro')
    parser.add_argument('-trades', '--t', required=False, help='Will save all the trades for a given product-id on the '
                                                               'bi-daily basis.', nargs='?')
    parser.add_argument('-orderbook', '--ob', required=False, help='Will save all levels of the order book for a given '
                                                                   'product-id on the freq basis.', nargs='?')
    parser.add_argument('-frequency', '--freq', required=False, help="This is the frequency at which a snapshot of the"
                                                                     " full order book is taken. This arg is to be "
                                                                     "used in conjunction with --ob or -orderbook."
                                                                     " The value is in milliseconds. So 1000 is 1 sec.",
                        nargs='?', default=1000, const=1000)
    parser.add_argument('-availableproducts', '--ap', required=False, help='Use this arg to list all the product-ids '
                                                                           'that you can use in --trades and '
                                                                           '--orderbook.', action='store_true')

    # https://stackoverflow.com/questions/18025646/python-argparse-conditional-requirements
    # To ensure frequency is supplied when orderbook is supplied

    args = parser.parse_args()

    if args.ap:
        client = PublicClient()
        r = client.get_products()
        r = [product['id'] for product in r]
        for product in r:
            print(product)

    # client = PublicClient()
    # r = client.get_product_trades('ETH-GBP')
    # print(r)
    # for trade in r:
    #     print(trade)
