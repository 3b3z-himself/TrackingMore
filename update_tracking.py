import requests

url = "https://api.trackingmore.com/v4/trackings/update/9a7ef5e14d6fcb28c7872fbf2d99caeb"

payload = {
    # "tracking_destination_country": "eg",
    # "tracking_origin_country": "us",
    "title": "Welcome Testing Track"
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Tracking-Api-Key": "2cknap14-rgef-aooz-twdh-uaqs44kjm5hd"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())