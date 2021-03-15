#!/usr/bin/env python
import time

from config import *
from gather_keys_oauth2 import OAuth2Server

if __name__ == '__main__':
    server = OAuth2Server(client_id, client_secret)
    server.browser_authorize()

    fb = server.fitbit
    detail_level = '1min'
    intraday = f'https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/{detail_level}.json'

    while True:
        resp = fb.make_request(intraday)
        # latest = resp['activities-heart-intraday']['dataset'][-1]['value']
        latest = resp['activities-heart-intraday']['dataset'][-1]
        print(latest)
        with open('maxs-hr.txt', 'w') as f:
            f.write(f"{latest['value']}\n")

        time.sleep(60)
