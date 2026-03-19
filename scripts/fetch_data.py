import requests

url = "https://feodotracker.abuse.ch/downloads/ipblocklist.txt"

response = requests.get(url)

if response.status_code == 200:
    with open("data/raw_ips.txt", "w") as file:
        file.write(response.text)
    print("Data fetched successfully!")
else:
    print("Failed to fetch data")
