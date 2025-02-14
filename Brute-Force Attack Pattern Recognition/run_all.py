import subprocess

# Run simulated logs generation
print("\n🚀 Generating Simulated Logs...")
subprocess.run(["python", "simulated_logs.py"], check=True)

# Run log processing
print("\n📊 Processing Logs...")
subprocess.run(["python", "process_logs.py"], check=True)

# Run brute-force detection
print("\n🔍 Detecting Brute-Force Attacks...")
subprocess.run(["python", "brute_force_detection.py"], check=True)
