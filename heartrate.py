#!/usr/bin/env python
"""Script for fetching my min and max heart rate over the past 15 minutes."""
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
        dataset = resp['activities-heart-intraday']['dataset']
        # Get only data from the last 15 minutes.
        latest = [d['value'] for d in dataset[-16:]]

        with open('maxs-hr.txt', 'w') as f:
            f.write('{}–{}'.format(min(latest), max(latest)))

        time.sleep(60)
