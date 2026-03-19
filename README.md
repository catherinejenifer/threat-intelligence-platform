# Threat Intelligence Platform with Automated Firewall Blocking

## 📌 Overview
This project collects malicious IP addresses from public threat intelligence feeds, processes the data, stores it in MongoDB, and automatically blocks these IPs using Linux iptables.

## 🚀 Features
- Fetch real-world threat data (OSINT)
- Clean and extract valid IPs
- Store data in MongoDB
- Automatically block malicious IPs
- Dynamic firewall rule updates

## 🛠️ Tech Stack
- Python
- MongoDB
- Linux (iptables)
- OSINT Threat Feeds

## 📂 Project Structure
scripts/
  fetch_data.py
  clean_data.py
  store_db.py
  block_ips.py

data/
  raw_ips.txt
  clean_ips.txt
