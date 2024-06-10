# TLS Scan Screenshot Project

This project is designed to run `sslscan` on a list of IP:ports from a CSV file and take screenshots of the command output on a Linux system.

## Requirements

- Python 3
- `x11-apps` and `ImageMagick` for taking screenshots
- Python libraries: `pandas`

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/tls_scan_project.git
    cd tls_scan_project
    ```

2. Install required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install `x11-apps` and `ImageMagick`:
    ```sh
    sudo apt-get install x11-apps imagemagick
    ```

## Usage

1. Create a CSV file named `machines.csv` with a column named `ip_port` containing the list of IP:port entries.

2. Run the script:
    ```sh
    python3 tls_scan_screenshots.py machines.csv
    ```

3. Screenshots will be saved in the `screenshots` directory.

## Example

Example `machines.csv`:
```csv
ip_port
192.168.1.1:443
192.168.1.2:443
