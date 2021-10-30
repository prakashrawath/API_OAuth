import requests
from requests.auth import HTTPBasicAuth
import json


def start():
 cred = open(
 'cus_config.json', )
 # json template: { "Username": "xxxx", "Password": "xxxx", "GET": "https://xx", "POST": "https://" }
 creden = json.load(cred)
 # Get the credentials/URIs from config file
 uname = creden['Username']
 passw = creden['Password']
 headers = creden['HEADER_GET'] # Populate request header params from the json config file
 # Trigger the GET operation, passing the URI from the file
 myresponse = requests.get(creden['GET'], headers=headers, auth=HTTPBasicAuth(uname, passw))
 # For successful API call, response code will be 200 (OK)
 if myresponse.ok:
 print('GET success. Status: ', myresponse.status_code)
 # head = myResponse.headers
 # POST
 payl = open('Create_SO_payload.json', )
 payload = json.load(payl)
 # Pass the XCSRF token from the GET call to the POST request header and set the cookies
 headers2 = creden['HEADER_POST'] # Populate request header params from the json config file
 headers2['x-csrf-token'] = myresponse.headers['x-csrf-token'] # Fill the XCSRF token from the GET response
 # Trigger the POST operation, passing the URI from the file
 myresponse2 = requests.post(creden['POST'], headers=headers2, cookies=myresponse.cookies,
 auth= HTTPBasicAuth(uname, passw), json=payload)
 myresponse3 = requests.post(creden['POST'], headers=headers2, cookies=myresponse.cookies,
 auth= HTTPBasicAuth(uname, passw), json=payload)
 print(myresponse2.content)
 print(myresponse3.content)
 if myresponse2.ok:
 print('Sales Order processed:', myresponse2.status_code)
 print(myresponse2.content)
 else:
 print("POST fail", myresponse2.status_code)
 print(myresponse2.content)
 else:
 print('GET fail', myresponse.status_code)


start()