import requests
import json

import requests
import json

base_url = f"https://sandboxdnac2.cisco.com/dna/"
auth_endpoint = "system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

auth_response = requests.post(url=f"{base_url}{auth_endpoint}", 
                              auth=(user,password), 
                              verify=False).json()

token = auth_response['Token']

headers = {
    "x-auth-token": token,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

health_endpoint = "intent/api/v1/client-health"
query_string = {"timestamp": ""}
response = requests.get(url=f"{base_url}{health_endpoint}", 
                        headers=headers,
                        params=query_string,
                        verify=False).json()

print(json.dumps(response, indent=2));

print(f"Clients: {response['response'][0]['scoreDetail'][0]['clientCount']}")

scores = response['response'][0]['scoreDetail']

for score in scores:
    if score['scoreCategory']['value'] == 'WIRED':
        print(f"Wired Clients: {score['clientCount']}")
        score_values = score['scoreList']
        for score_value in score_values:
            print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")
    elif score['scoreCategory']['value'] == 'Wireless':
        print(f"Wireless Clients: {score['clientCount']}")
        for score_value in score_values:
            print(f"{score_value['scoreCategory']['value']}: {score_value['clientCount']}")