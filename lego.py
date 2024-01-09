import requests
from requests.auth import HTTPDigestAuth
import json
import os
from PIL import Image
from io import BytesIO

key='36aba154fa54efff09feb87da7510356'
mainurl = 'https://rebrickable.com/api/v3/lego/'
kitID = '40625'

def getPartsList(url):
    #return(temp_part)

    #It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtine 
    myResponse =  requests.get(url,params={'key': key, 'inc_part_details': '1'})

    if(myResponse.ok):

        #Loading the response data into a dict variable
        #json.loads takes in only binary or string variables so using content to fetch binary content
        #Loads (Load String) takes a Ison file and converts into python data structure (dict or list, depending on 350N)
        jData = json.loads(myResponse.content)
    else:
        # If response code is not ok (200), print the resulting http error code with description 
        myResponse.raise_for_status()
        #print (jData)
    return jData

def partsImportLDRAW():

    url = mainurl + 'sets/' + kitID + '-1/parts/'
    parts = []
    partsList = getPartsList(url)

    for piece in partsList['results']:
        #print(piece['part']['part_num'])
        parts.append(piece['part']['part_num'])
    return parts

def makeLDRAWfile():
    LDRAW_file = open("LDRAW_file.ldr", "w")
    parts = partsImportLDRAW()

    for piece in parts:
        line =  '1 4 0 0 0 1 0 0 0 1 0 0 0 1 ' + str(piece) + '.dat'
        LDRAW_file.write(line)
        LDRAW_file.write("\n")
    LDRAW_file.close()

makeLDRAWfile()