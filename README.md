# IP Address Log Processor

This Python script processes a log file containing IP addresses, retrieves detailed information about each IP address, and logs the information in a formatted manner to an output file. It continuously monitors the log file for new IP addresses and updates the output file accordingly.

## Features

- Extracts IP addresses from a log file.
- Fetches hostname and additional information (city, region, country, organization) for each IP address.
- Logs the detailed information in a human-readable format.
- Monitors the log file continuously and processes new IP addresses as they appear.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the script.
2. Install the required Python library using pip:
    ```bash
    pip install requests
    ```

## Usage

1. Ensure that you have a log file (`logs/threats.log`) that the script can read from.
2. Run the script:
    ```bash
    python ip_threat_log_processor.py
    ```
3. The script will process the log file and append detailed information about each IP address to the output file (`logs/ip_scan.log`).

## Script Details

### Functions

- `get_hostname(ip_address)`: Retrieves the hostname for a given IP address.
- `get_ipinfo(ip_address)`: Fetches detailed information about the IP address from the `ipinfo.io` service.
- `get_ip_details(ip_address)`: Combines hostname and IP information into a dictionary.
- `format_details(details)`: Formats the details dictionary into a human-readable string.
- `is_valid_ip(ip)`: Validates if a given string is a valid IP address.
- `process_threats_log(log_path, output_path)`: Main function that monitors the log file, processes new IP addresses, and writes the details to the output file.

### Continuous Monitoring

The script continuously monitors the log file (`logs/threats.log`) every 60 seconds for new IP addresses. If the log file does not exist, it waits until the file is created. When new IP addresses are found, it retrieves and logs their details.

### Example Output

The output in the `logs/ip_scan.log` file will look like this:

IP Address : 8.8.8.8
Hostname : dns.google
City : Mountain View
Region : California
Country : US
Organization: Google LLC


## Customization

- To change the log file paths, modify the `log_path` and `output_path` variables in the `__main__` block.
- The sleep duration between log checks can be adjusted by changing the value in `time.sleep(60)` in the `process_threats_log` function.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute to this project by submitting issues or pull requests. Your feedback is highly appreciated!

