##########################################################
#
# Copyright (C) 2024-PRESENT: Keivan Ipchi Hagh
#
# Email:    keivanipchihagh@gmail.com
# GitHub:   https://github.com/keivanipchihagh
#
##########################################################

import requests
from time import sleep
from datetime import datetime

from utils import logger
from config import (
    AUTH_TOKEN,
    TAB_COUNT,
    AVAILABLE_TAB_COUNT,
    SLEEP_TIME,
)

CURRENT_N_COINS = 0

def send_request():
    global CURRENT_N_COINS

    # Headers
    headers = {
        'Host': 'api.hamsterkombat.io',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:125.0) Gecko/20100101 Firefox/125.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://hamsterkombat.io/',
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Content-Type': 'application/json',
        'Origin': 'https://hamsterkombat.io',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'close',
    }
    # Data
    payload = {
        'count': TAB_COUNT,
        'availableTaps': AVAILABLE_TAB_COUNT,
        'timestamp': int(str(datetime.now().timestamp()).split(".")[0])
    }

    try:
        response = requests.post(
            url = 'https://api.hamsterkombat.io/clicker/tap',
            headers = headers,
            json = payload,
        )

        info: dict           = response.json()
        totalCoins: int      = info['clickerUser']['totalCoins']
        level: int           = info['clickerUser']['level']
        availableTaps: int   = info['clickerUser']['availableTaps']

        logger.info(f'Total Coins: {totalCoins} (+{totalCoins-CURRENT_N_COINS}) | Level: {level} | Avaialble Taps: {availableTaps} | Sleep: {SLEEP_TIME}s')

        # Update current N.coins
        CURRENT_N_COINS = totalCoins

    except Exception as ex:
        logger.error(ex)



if __name__ == "__main__":
    while True:
        send_request()
        sleep(SLEEP_TIME)
