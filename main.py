#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# usage:
# CHATWORK_API_TOKEN="fdsafasldkfjasdkkfaksdka"\
#   TASK_ROOM_ID=12345\
#   TASK_USER_ID="99988,92882"\
#   TASK_BODY="一週間以内にやってほしいこと！"\
#   TASK_LIMIT=1534489879\
#   python ./main.py

from __future__ import print_function, unicode_literals
import os
import time
from datetime import datetime, date, timedelta
import requests
from pprint import pprint

ENDPOINT = 'https://api.chatwork.com/v2'

CHATWORK_API_TOKEN = os.environ["CHATWORK_API_TOKEN"]
TASK_ROOM_ID = os.environ["TASK_ROOM_ID"]
TASK_USER_ID = os.environ["TASK_USER_ID"]
TASK_BODY = os.environ["TASK_BODY"]
TASK_LIMIT = os.environ["TASK_LIMIT"]

resp = requests.post(
        '{}/rooms/{}/tasks'.format(ENDPOINT, TASK_ROOM_ID),
        headers = { 'X-ChatWorkToken': CHATWORK_API_TOKEN },
        params = {
            'body': TASK_BODY,
            'limit': TASK_LIMIT,
            'to_ids': TASK_USER_ID,
        }
)

pprint(resp.content)
