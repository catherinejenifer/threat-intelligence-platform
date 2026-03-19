import re

input_file = "data/raw_ips.txt"
output_file = "data/clean_ips.txt"

ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

unique_ips = set()

with open(input_file, "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith("#") or line == "":
            continue

        if ip_pattern.match(line):
            unique_ips.add(line)

with open(output_file, "w") as file:
    for ip in unique_ips:
        file.write(ip + "\n")

print(f"Cleaned {len(unique_ips)} IPs")
