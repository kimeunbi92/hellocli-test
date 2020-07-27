import sys
import os
import hashlib
import hmac
import base64
import requests
import urllib
import time
import art
import makeSignature

class server:
    def __init__(self,parameters={}):
        self.credit = []
        try:
            file = open("credit.txt","r")
        except:
            print("no credit file detected \nplease type 'KTcloud configure init' to create credit files")
            exit(-1)
        for line in file:
            line = line.replace("\n","")
            self.credit.append(line)
        self.apikey = self.credit[0]
        self.secret_key = self.credit[1] 
        self.Zone = self.credit[2]
        self.response = self.credit[3]
        self.parameters = parameters
        self.url = "https://api.ucloudbiz.olleh.com/server/v1/client/api?"
        if(self.Zone == "KOR-Seoul M2"):
            self.url= "https://api.ucloudbiz.olleh.com/server/v2/client/api?"
    
    def execute(self, request):
        request['apikey']=self.apikey
        req = makeSignature.makeSignature(request, self.url, self.secret_key)
        print("********** request URL **********")
        print(req)

        response = requests.get(req)
        res = response.json()
        
        print("********** Response **********")
        print(res)