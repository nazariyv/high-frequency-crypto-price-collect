from cbpro.public_client import PublicClient
from datetime import datetime
from logging import handlers
import traceback
import argparse
import asyncio
import logging
import json
import sys
import os

# Package level imports
from utils import cwow

# ==================================== COINBASE API SET UP + LOGGER ====================================================
ISO_DATE = '%Y-%m-%d'

# Coinbase API
client = PublicClient()
products = client.get_products()
products = [product['id'] for product in products]

# Logging
FORMATTER = logging.Formatter('[%(name)s]|[%(levelname)s]|[%(asctime)s]|%(message)s')
LOG_FILENAME = 'reuters_stock_scraper.out'
# Set up a specific logger with our desired output level
# Change level below if you want to log less stuff. For example, up it a notch to INFO.
logger = logging.getLogger(LOG_FILENAME)
logger.setLevel(logging.DEBUG)
logger_folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logs')
if not os.path.exists(logger_folder_path): os.makedirs(logger_folder_path)
# Add the log message handler to the logger. (20 MB * 5 = 100 MB Buffer)
handler = logging.handlers.RotatingFileHandler(
    os.path.join(logger_folder_path, LOG_FILENAME),
    maxBytes=20000000,
    backupCount=5,
)
handler.setFormatter(FORMATTER)
logger.addHandler(handler)
# ======================================================================================================================


def create_save_location(path_to_file: str) -> str:
    """
    Creates the dated files.
    :param path_to_file:
    :return:
    """
    now = datetime.now()
    now_date = now.strftime(ISO_DATE)
    save_file = now_date + '.json'

    if not os.path.exists(path_to_file):
        os.makedirs(path_to_file)

    full_save_path = os.path.join(path_to_file, save_file)

    if not os.path.exists(full_save_path):
        open(full_save_path, 'a', encoding='utf-8').close()

    return full_save_path


async def ob_collector(product_id: str, file) -> None:
    assert hasattr(file, 'write'), 'Provide a file to write to.'
    assert product_id in products, f'Your product {product_id} is not allowed. Allowed values: {products}.'

    await asyncio.sleep(1.0/(10**2))

    try:
        now = datetime.now()
        print(f'{now} - retrieving ob from COINBASE for {product_id}')
        ob_all = client.get_product_order_book(product_id, 3)
        ob_all['timestamp'] = str(now)
        print(f'{datetime.now()} - success...')
        json.dump(ob_all, file)
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        error_msg = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
        print(error_msg)
        logger.warning(f'[1]-Error encountered collecting ob data: {error_msg}')
        pass


async def trades_collector(product_id: str, file) -> None:
    pass


async def ob_main(product_id: str, freq: int) -> None:
    assert freq >= 1, f'The minimum frequency is 1s. Adjust your value: {freq}.'

    save_loc = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'ob', product_id)

    while True:
        try:
            full_save_path = create_save_location(save_loc)
            file = open(full_save_path, 'a', encoding='utf-8')
            await ob_collector(product_id, file)
            await asyncio.sleep(freq)
        except:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            error_msg = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
            print(error_msg)
            logger.warning(f'[1]-Error encountered collecting ob data: {error_msg}')


async def trades_main() -> None:
    pass


async def combined_main(product_id: str, freq: int) -> None:
    """
    Creates to concurrent coroutine tasks: collecting order book and collecting the trades. And awaits completion.
    :return:
    """
    asyncio.gather(ob_main(product_id, freq), trades_main())
    pass


if __name__ == '__main__':
    # ======================================= Arg Parser ===============================================================
    parser = argparse.ArgumentParser(description='Tool to download the order book and/or the trades data from Coinbase '
                                                 'Pro')
    parser.add_argument('-product', '--p', required=True, nargs='?', help='This is the product id for which to '
                                                                          'collect the data. Use --ap to get the '
                                                                          'list of available products.')
    parser.add_argument('-trades', '--t', required=False, help='Will save all the trades for a given product-id on the '
                                                               'bi-daily basis.', action='store_true')
    parser.add_argument('-orderbook', '--ob', required=False, help='Will save all levels of the order book for a given '
                                                                   'product-id on the freq basis.', action='store_true')
    parser.add_argument('-frequency', '--freq', required=False, help="This is the frequency at which a snapshot of the"
                                                                     " full order book is taken. This arg is to be "
                                                                     "used in conjunction with --ob or -orderbook."
                                                                     " The value is in seconds. So 1 is 1 sec.",
                        nargs='?', default=1, const=1, type=int)
    parser.add_argument('-availableproducts', '--ap', required=False, help='Use this arg to list all the product-ids '
                                                                           'that you can use in --trades and '
                                                                           '--orderbook.', action='store_true')
    args = parser.parse_args()
    # ==================================================================================================================

    loop = asyncio.get_event_loop()

    try:
        # print the available coinbase products
        if args.ap:
            for product in products:
                print(product)

        # collecting just the ob
        if args.ob:
            task = loop.create_task(ob_main(args.p, args.freq))
            loop.run_until_complete(task)

        # collecting ob + trades
        if args.t and args.ob:
            asyncio.run(combined_main(args.p, args.freq))

    except KeyboardInterrupt:
        cwow()
        exit(0)
    finally:
        loop.close()
