import requests

response1 = requests.get("http://api.ipify.org/?format=json")

ip = response1.json()['ip']

response2 = requests.get(f"http://ipinfo.io/{ip}/geo")

print("Country : ",response2.json()['country'])
print("Region : ",response2.json()['region'])
print("City : ",response2.json()['city'])
print("Timezone : ",response2.json()['timezone'])