import socket
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_ip_address(url):
    try:
        # Get the IP address of the website
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror as e:
        logging.error(f"Error: {str(e)}")
        return None

def scan_ports(ip_address, start_port, end_port):
    # Perform a port scan
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object for each port
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            client_socket.settimeout(1)
            # Connect to the target host and port
            client_socket.connect((ip_address, port))
            logging.info(f"Port {port} is open on {ip_address}")
            client_socket.close()  # Close the socket after successful connection
        except socket.timeout:
            pass
        except socket.error as e:
            logging.error(f"Error connecting to port {port} on {ip_address}: {str(e)}")
            client_socket.close()  # Close the socket if an error occurs

# Main execution
if __name__ == "__main__":
    # Set the target website URL
    website_url = "redditasic m.com"

    # Get the IP address of the website
    ip_address = get_ip_address(website_url)

    if ip_address:
        logging.info(f"The IP address of {website_url} is: {ip_address}")
        # Scan the IP address for open ports
        scan_ports(ip_address, 1, 1024)
    else:
        logging.info(f"Failed to resolve the IP address for {website_url}")