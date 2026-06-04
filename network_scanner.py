import socket
import subprocess
import platform

# -----------------------------
# Task 1: Get Local IP Address
# -----------------------------
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print("=== Local IP Address ===")
    print("Hostname:", hostname)
    print("Local IP:", local_ip)
    print()


# -----------------------------
# Task 2: DNS Lookup
# -----------------------------
def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)

        print("=== DNS Lookup ===")
        print(f"Domain: {domain}")
        print(f"IP Address: {ip}")
        print()

    except socket.gaierror:
        print("DNS lookup failed")
        print()


# -----------------------------
# Task 3: Port Checker
# -----------------------------
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # timeout after 1 second
    sock.settimeout(1)

    result = sock.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is OPEN on {host}")
    else:
        print(f"Port {port} is CLOSED on {host}")

    sock.close()


# -----------------------------
# Task 4: Connectivity Check
# -----------------------------
def check_connectivity():
    print("\n=== Internet Connectivity Check ===")

    # Windows uses -n, Linux/Mac use -c
    param = "-n" if platform.system().lower() == "windows" else "-c"

    command = ["ping", param, "1", "google.com"]

    result = subprocess.run(command)

    if result.returncode == 0:
        print("Internet is WORKING")
    else:
        print("No internet connection")


# -----------------------------
# Main Program
# -----------------------------
if __name__ == "__main__":

    # Task 1
    get_local_ip()

    # Task 2
    domain = input("Enter domain for DNS lookup: ")
    dns_lookup(domain)

    # Task 3
    host = input("Enter host to scan ports: ")

    print("\n=== Port Scan ===")
    check_port(host, 80)
    check_port(host, 443)

    # Task 4
    check_connectivity()