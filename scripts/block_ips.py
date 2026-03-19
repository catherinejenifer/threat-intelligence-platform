from pymongo import MongoClient
import subprocess

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["threat_intel"]
collection = db["malicious_ips"]

# Fetch IPs
ips = collection.find()

for entry in ips:
    ip = entry["ip"]

    print(f"Blocking IP: {ip}")

    # Run iptables command
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

print("All IPs blocked!")
