import pandas as pd

# Load the processed failed attempts data
attempt_count_df = pd.read_csv("failed_attempts_count.csv")

# Convert timestamp column to datetime
attempt_count_df["timestamp_rounded"] = pd.to_datetime(attempt_count_df["timestamp_rounded"])

# Define brute-force attack threshold
ip_attempt_threshold = 3  # Minimum failed attempts within a minute to be considered an attack

# Identify brute-force attacks
brute_force_attacks = attempt_count_df[attempt_count_df["attempt_count"] >= ip_attempt_threshold]

# Print detected brute-force attacks
if not brute_force_attacks.empty:
    print("Detected Brute-Force Attacks:")
    print(brute_force_attacks.to_string(index=False))
else:
    print("No brute-force attacks detected.")
