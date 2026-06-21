import requests
import os
import time

# Colors
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
W = "\033[0m"
C = "\033[96m"

def banner():
    os.system("clear")
    print(R + """
██████╗ ███████╗██████╗ ████████╗███████╗ █████╗ ███╗   ███╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██████╔╝█████╗  ██████╔╝   ██║   █████╗  ███████║██╔████╔██║
██╔══██╗██╔══╝  ██╔═══╝    ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
██║  ██║███████╗██║        ██║   ███████╗██║  ██║██║ ╚═╝ ██║
╚═╝  ╚═╝╚══════╝╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
""" + W)
    print(Y + "        🔥 REDTEAMNATION - IP GEO TOOL 🔥\n" + W)
    print(C + "        Author: ALIYAN (RedTeamNation)\n" + W)

def ip_lookup(ip):
    print(G + "\n[+] Fetching data...\n" + W)
    url = f"http://ip-api.com/json/{ip}"
    res = requests.get(url)
    data = res.json()

    if data["status"] == "fail":
        print(R + "[-] Invalid IP or no data found!" + W)
        return

    print(B + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + W)
    print(G + f"IP Address   : {data['query']}")
    print(G + f"Country      : {data['country']}")
    print(G + f"Region       : {data['regionName']}")
    print(G + f"City         : {data['city']}")
    print(G + f"ISP          : {data['isp']}")
    print(G + f"Org          : {data['org']}")
    print(G + f"Latitude     : {data['lat']}")
    print(G + f"Longitude    : {data['lon']}")
    print(B + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + W)

    print(Y + f"\nGoogle Maps: https://www.google.com/maps?q={data['lat']},{data['lon']}\n" + W)

def loading():
    print(R + "Initializing REDTEAMNATION tool..." + W)
    for i in range(3):
        time.sleep(0.5)
        print(R + "🔥 LOADING..." + W)

if __name__ == "__main__":
    loading()
    banner()
    ip = input(R + "Enter IP Address: " + W)
    ip_lookup(ip)7