import json
import logging
import os
import requests

from base64 import b64decode
from urllib.parse import parse_qs

expected_token = os.environ['expected_token']
surl = os.environ["slack_url"]

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    
    b64params = event["body"]
    params = b64decode(b64params)
    params = params.decode("utf-8")
    params = parse_qs(params)
    token = params["token"][0]
    if token != expected_token:
        logger.error("Request token (%s) does not match expected", token)
        return respond(Exception('Invalid request token'))

    url = "https://catfact.ninja/fact"
    r = requests.get(url)
    fact = json.loads(r.text)["fact"]
    myobj = {}
    myobj['text'] = params["user_name"][0] + "says: " + fact

    p = requests.post(surl, json = myobj)

    return respond(None, )