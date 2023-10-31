import requests

url = "https://api.trackingmore.com/v4/trackings/batch"

payload = [
    {
        "courier_code": "fedex",
        "tracking_number": "984654984523165"
    }
]
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Tracking-Api-Key": "2cknap14-rgef-aooz-twdh-uaqs44kjm5hd"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())