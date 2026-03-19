from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create database and collection
db = client["threat_intel"]
collection = db["malicious_ips"]

# Read cleaned IPs
with open("data/clean_ips.txt", "r") as file:
    for line in file:
        ip = line.strip()

        if ip:
            collection.insert_one({"ip": ip})

print("IPs stored in MongoDB successfully!")
