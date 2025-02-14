# Brute-Force Attack Pattern Recognition Simulation

## 🔹 Overview
This project is designed to detect **brute-force attack patterns** by simulating login attempts, processing logs, and identifying suspicious activities based on threshold-based detection. It provides a **structured approach to cybersecurity** by analyzing failed login attempts and recognizing attack patterns.

## 🔹 Features
- **Simulated Log Generation** – Generates login attempt logs with both normal and brute-force attack patterns.
- **Log Processing** – Extracts and structures failed login attempts for analysis.
- **Brute-Force Detection** – Identifies IPs with repeated failed login attempts within a specific time frame.
- **Threshold-Based Analysis** – Uses a predefined threshold to detect brute-force attempts.
- **Scalable Design** – Can be extended to integrate with real-world authentication logs.


## 🔹 How It Works
1. **Simulated Logs**: The `simulated_logs.py` script generates **500+ login attempts** with random IPs, usernames, and passwords.
2. **Log Processing**: The `process_logs.py` script **extracts and structures** failed login attempts for analysis.
3. **Brute-Force Detection**: The `brute_force_detection.py` script **identifies brute-force attacks** using a threshold-based approach.
4. **Output Analysis**: The system **prints detected brute-force attacks**, which can be used for further security measures.

## 🔹 Installation & Usage
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/Brute-Force-Attack-Pattern-Recognition-Simulation.git
   cd Brute-Force-Attack-Pattern-Recognition-Simulation
2. **Install Dependencies:**
   ```sh
   pip install pandas numpy
3.**Run the scripts in order:**
    ```sh
    python simulated_logs.py
    python process_logs.py
    python brute_force_detection.py

## 🔹 Example Output
        Detected Brute-Force Attacks:
        timestamp             ip_address     attempt_count
        2025-02-14 12:35:00   192.168.1.101        5
        2025-02-14 12:36:00   192.168.1.102        7
## 🔹 Future Enhancements
  1.**Real-time monitoring with live authentication logs.**
  
  2.**Automated alerts for security teams.**
  
  3.**Machine learning-based detection for adaptive security.**
  
  4.**Dashboard visualization for attack tracking.**

## 🔹 License
This project is open-source under the MIT License. Feel free to contribute and improve it!

