import requests
import json
import urllib.parse
from django.conf import settings

import binascii
from Crypto.Cipher import AES

class ControlCenterUtils():

    @staticmethod
    def addAccessPointInControlCenter(self, macaddress ):
        
        wifilanServerId = getattr(settings, 'WIFILAN_SERVER_ID')
        wifilan_server_auth_key = getattr(settings,'WIFILAN_SERVER_AUTH_KEY')
        
        apData = { 
            'action' : "ADD",
            'macaddress' : macaddress,
            'authkey' : wifilan_server_auth_key,
            'serialnumber' : None,
            'model' : None,
            'firmware' : None,
            'wifilancustomerid' : None,
            'smartapcustomerid' : None
        }

        print("Updated Dict is: ", apData)
        json_object = json.dumps(apData, indent = 4)   
        print("Json ", apData)

        """
         Encrypt using AES-256-CBC with random/shared iv
        'passphrase' must be in hex, generate with 'openssl rand -hex 32'
        """
        """
        try:
            passphrase = 'aes128'
            key = binascii.unhexlify(passphrase)
            pad = lambda s : s+chr(16-len(s)%16)*(16-len(s)%16)
            iv = wifilan_server_auth_key
            
            cipher = AES.new(key, AES.MODE_CBC, iv)

            encrypted_64 = base64.b64encode(cipher.encrypt(pad(apData))).decode('ascii')

            iv_64 = base64.b64encode(iv).decode('ascii')

            json_data = {}
            json_data['iv'] = iv_64
            json_data['data'] = encrypted_64
            encryptedApData = base64.b64encode(json.dumps(json_data).encode('ascii'))
        except Exception as e:
            print("Cannot decrypt datas...")
            print(e)"""
       #encryptedApData = openssl_encrypt(json_encode($apData) , "aes128" , WIFILAN_SERVER_AUTH_KEY);
        encryptedApData = ""
        print("data in function",macaddress, wifilanServerId)

        postData = {
            'callingserver' : 'wifilan',
            'serverid' : wifilanServerId,
            'data' : encryptedApData,
        }
        
        controlCenterResponse = self.handleControlCenterAPICall(postData);
        
        if(controlCenterResponse['status'] == 'success'):
            return True
        else:
            return controlCenterResponse['message']


    @staticmethod
    def deleteAccessPointInControlCenter(self, mac ):
        pass


    def handleControlCenterAPICall(self, postData ):
        
        url = getattr(settings, 'CONTROL_CENTER_URL')

        postString = urllib.parse.urlencode(postData)
        headers = { 'Content-Type':'application/json' }

        try:
            response = requests.get(url)
            response = requests.post( url, headers=headers, params=postString)
            if response.status_code is 200:
                return response
            
        except Exception as e:
            print('ControlCenterAPICall Exception >>>>>',e)
            return {}