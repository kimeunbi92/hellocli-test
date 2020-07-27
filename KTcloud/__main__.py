import sys
import os
import hashlib
import hmac
import base64
import requests
import urllib
import time
import art
import KTcloud_server
import creditConfiguration
import importlib

def main():
    ctype = ""
    parameters = {}
    request = {}
    
    if len(sys.argv) < 3 :

        if(len(sys.argv) == 1):
            Art  = art.text2art("KT",font="black")
            print(Art)
            Art  = art.text2art("CLOUD",font="black")
            print(Art)
            print(" ")
            print ("usage: KTcloud [type] [command] [parameters] \nor type 'KTcloud help'")

        else:
            print ("usage: KTcloud [type] [command] [parameters] \nor type 'KTcloud help'")
            exit(-1)
    else:
        ctype = sys.argv[1]
        request = {}

        if (ctype == "server"):
            for i in range(2,len(sys.argv)):
                # parameters.append(sys.argv[i])
                parameters[sys.argv[i].split('=')[0]] = sys.argv[i].split('=')[1]
            command_key = parameters['command']
            mod = importlib.import_module('.'+command_key, 'module')
            callapi = getattr(mod, command_key)
            request = callapi(parameters)

        elif (ctype == "configure"):
            c = creditConfiguration.configure(sys.argv[2])
            c.command_process_configure()
        else:
            print("unable to process type: ",ctype,"\n type 'KTcloud help' to view supported type")
            exit(-1)

        s = KTcloud_server.server(parameters)
        s.execute(request)

if __name__ == '__main__':
    main()