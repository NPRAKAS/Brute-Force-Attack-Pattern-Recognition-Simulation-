import pandas as pd
import random
from datetime import datetime, timedelta

# Parameters
num_logs = 500
unique_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5", "192.168.1.6", "192.168.1.7"]
brute_force_ips = random.sample(unique_ips, 5)  # Select 4-5 IPs for brute-force behavior
usernames = ["admin", "user1", "test", "root", "guest", "operator", "sysadmin"]
passwords = ["12345", "password", "admin", "qwerty", "letmein", "pass123", "welcome"]
start_time = datetime.now()

# Generate log entries
logs = []
for _ in range(num_logs):
    timestamp = start_time + timedelta(seconds=random.randint(0, 3600))  # Random timestamps in 1-hour range
    ip_address = random.choice(unique_ips)
    username = random.choice(usernames)
    password = random.choice(passwords)
    status = "Failed" if ip_address in brute_force_ips and random.random() < 0.7 else "Success"  # 70% failure rate for brute-force IPs
    logs.append([timestamp.strftime("%Y-%m-%d %H:%M:%S"), ip_address, username, password, status])

# Create DataFrame
log_df = pd.DataFrame(logs, columns=["timestamp", "ip_address", "username", "password", "status"])

# Save to CSV
log_df.to_csv("simulated_logs.csv", index=False)

print("Simulated log file 'simulated_logs.csv' generated with 500 entries.")
