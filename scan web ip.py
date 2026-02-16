import socket
import argparse

def scan_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] Domain: {domain} -> IP: {ip}")
        return ip
    except socket.gaierror:
        print(f"[-] Could not resolve domain: {domain}")
        return None

def port_scan(ip, ports):
    print(f"\nScanning ports on {ip}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="Simple IP and Port Scanner")
    parser.add_argument("domain", help="Domain name to scan (e.g., google.com)")
    parser.add_argument(
        "-p", "--ports", nargs="+", type=int, default=[80, 443, 22, 21],
        help="List of ports to scan (default: 80 443 22 21)"
    )
    args = parser.parse_args()

    ip = scan_ip(args.domain)
    if ip:
        port_scan(ip, args.ports)

if __name__ == "__main__":
    main()