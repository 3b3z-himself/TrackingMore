import requests

url = "https://api.trackingmore.com/v4/couriers/all"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Tracking-Api-Key": "2cknap14-rgef-aooz-twdh-uaqs44kjm5hd"
}

response = requests.get(url, headers=headers)

print(response.json())