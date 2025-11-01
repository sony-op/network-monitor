from monitor.ping import ping_host
from monitor.scanner import scan_network
import csv, time

NETWORK = "192.168.1.0/24"  # Change to your subnet (use `ip a` to check)

def main():
    print("🔍 Scanning Network...")
    devices = scan_network(NETWORK)
    print(f"Found {len(devices)} devices.\n")

    with open("data/logs.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "MAC", "Status", "Timestamp"])
        for device in devices:
            status = ping_host(device['ip'])
            writer.writerow([device['ip'], device['mac'], "Online" if status else "Offline", time.ctime()])
            print(f"{device['ip']} ({device['mac']}) → {'Online' if status else 'Offline'}")

if __name__ == "__main__":
    main()
