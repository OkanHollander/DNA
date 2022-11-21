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

cred_cli_endpoint = "intent/api/v1/global-credential?credentialSubType=CLI"
cli_response = requests.get(url=f"{base_url}{cred_cli_endpoint}", headers=headers, verify=False).json()['response'][0]
# print(json.dumps(cli_response, indent=2))
cli_cred = cli_response['id']

cred_snmp_endpoint = "intent/api/v1/global-credential?credentialSubType=SNMPV2_WRITE_COMMUNITY"
snmp_response = requests.get(url=f"{base_url}{cred_snmp_endpoint}", headers=headers, verify=False).json()['response'][0]
# print(json.dumps(snmp_response, indent=2))
snmp_cred = snmp_response['id']

payload = {
    "name": "TEST DISCOVERY",
    "discoveryType": "Range",
    "ipAddressList": "10.10.20.30-10.10.20.254",
    "timeout":1,
    "protocolOrder": "ssh,telnet",
    "preferredMgmtIpMethod": "None",
    "globalCredentialList": [cli_cred]
}

discovery_endpoint = "intent/api/v1/discovery"
discovery_response = requests.post(url=f"{base_url}{discovery_endpoint}", headers=headers, verify=False, data=json.dumps(payload))
print(discovery_response)
print(discovery_response.text)