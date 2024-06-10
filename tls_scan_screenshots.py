import os
import subprocess
import argparse
import pandas as pd
import time

def run_sslscan(ip_ports):
    # Directory to save screenshots
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    for ip_port in ip_ports:
        command = f"sslscan --no-cipher-details --no-ciphersuites --no-compression --no-fallback --no-groups --no-heartbleed --no-renegotiation {ip_port}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Create a new console window with the command output
        os.system('clear')
        print(result.stdout)
        
        # Ensure the output has time to be printed
        time.sleep(2)
        
        # Capture the current terminal window
        png_file = f"{screenshot_dir}/{ip_port.replace(':', '_')}.png"
        os.system(f"xwd -root -silent | convert xwd:- {png_file}")

        # Clear the console again for the next iteration
        os.system('clear')
        time.sleep(1)  # Adding a short delay to ensure proper screenshot capture

def main():
    parser = argparse.ArgumentParser(description="Run sslscan on a list of IP:ports from a CSV file and take screenshots.")
    parser.add_argument("csv_file", help="Path to the CSV file containing IP:port list.")
    
    args = parser.parse_args()

    # Read the CSV file
    ip_ports_df = pd.read_csv(args.csv_file)
    
    # Assuming the CSV file has a column named 'ip_port'
    ip_ports = ip_ports_df['ip_port'].tolist()

    run_sslscan(ip_ports)

if __name__ == "__main__":
    main()
