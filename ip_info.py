import os
import re
import socket
import time
import requests

def get_hostname(ip_address):
    try:
        hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip_address)
        return hostname
    except (socket.herror, socket.gaierror):
        return "No hostname found"

def get_ipinfo(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.RequestException:
        return None

def get_ip_details(ip_address):
    hostname = get_hostname(ip_address)
    ipinfo = get_ipinfo(ip_address)
    
    details = {
        "IP Address": ip_address,
        "Hostname": hostname,
        "City": ipinfo.get('city', 'N/A') if ipinfo else 'N/A',
        "Region": ipinfo.get('region', 'N/A') if ipinfo else 'N/A',
        "Country": ipinfo.get('country', 'N/A') if ipinfo else 'N/A',
        "Organization": ipinfo.get('org', 'N/A') if ipinfo else 'N/A'
    }
    
    return details

def format_details(details):
    formatted_details = (
        f"IP Address  : {details['IP Address']}\n"
        f"Hostname    : {details['Hostname']}\n"
        f"City        : {details['City']}\n"
        f"Region      : {details['Region']}\n"
        f"Country     : {details['Country']}\n"
        f"Organization: {details['Organization']}\n"
        "--------------------------------------------\n"
    )
    return formatted_details

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True

def process_threats_log(log_path, output_path):
    processed_ips = set()

    while True:
        if not os.path.exists(log_path):
            print(f"{log_path} not found. Waiting for the file to be created...")
            time.sleep(60)
            continue

        with open(log_path, 'r') as file:
            lines = file.readlines()

        new_ips = set()

        for line in lines:
            ip_matches = re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
            for ip in ip_matches:
                if is_valid_ip(ip) and ip not in processed_ips:
                    new_ips.add(ip)

        if new_ips:
            with open(output_path, 'a') as output_file:
                for ip in new_ips:
                    details = get_ip_details(ip)
                    formatted_details = format_details(details)
                    output_file.write(formatted_details)
                    processed_ips.add(ip)
                    print(formatted_details)

        time.sleep(60)

if __name__ == "__main__":
    log_path = "logs/ip_addresses.log"
    output_path = "logs/ip_info.log"
    process_threats_log(log_path, output_path)
