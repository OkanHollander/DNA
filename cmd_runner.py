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

device_url = "intent/api/v1/network-device?family=Switches and Hubs&type=Cisco Catalyst 9300 Switch"
dev_response = requests.get(url=f"{base_url}{device_url}", headers=headers, verify=False).json()
print(json.dumps(dev_response, indent=2))

device_ids = []
for device in dev_response['response']:
    device_id = device['id']
    device_ids.append(device_id)
    
payload = {
    "commands": [
        "show version"
    ],
    "deviceUuids": device_ids 
}

command_endpoint = "intent/api/v1/network-device-poller/cli/read-request"

cli_response = requests.get(url=f"{base_url}{command_endpoint}", data=json.dumps(payload), verify=False)
print(cli_response.text)