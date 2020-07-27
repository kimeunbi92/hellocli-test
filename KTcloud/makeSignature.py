import hashlib
import hmac
import base64
import requests
import urllib

def makeSignature(request, baseurl, secret_key):
    secret_key = bytes(secret_key, 'UTF-8')
    
    request_str = '&'.join(['='.join([k,urllib.parse.quote_plus(request[k])]) for k in sorted(request.keys(), key=str.lower)])
    make_request = bytes(request_str, 'UTF-8')

    signatureKey = urllib.parse.quote_plus(base64.b64encode(hmac.new(secret_key, make_request.lower(), digestmod=hashlib.sha1).digest()))

    req=baseurl+request_str+'&signature='+signatureKey

    return req