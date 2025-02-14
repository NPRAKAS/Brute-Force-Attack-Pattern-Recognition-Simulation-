import pandas as pd

# Load the simulated logs
logs = pd.read_csv("simulated_logs.csv")

# Convert the timestamp column to datetime
logs["timestamp"] = pd.to_datetime(logs["timestamp"])

# Filter for failed login attempts and create a copy to avoid warnings
failed_attempts = logs[logs["status"] == "Failed"].copy()

# Round timestamps to the nearest minute
failed_attempts.loc[:, "timestamp_rounded"] = failed_attempts["timestamp"].dt.floor("min")

# Count failed attempts per minute per IP address
failed_attempts_count = failed_attempts.groupby(["timestamp_rounded", "ip_address"]).size().reset_index(name="attempt_count")

# Save to CSV
failed_attempts_count.to_csv("failed_attempts_count.csv", index=False)

print("Processed logs saved as 'failed_attempts_count.csv'")
