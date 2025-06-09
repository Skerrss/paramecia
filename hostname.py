import socket
import whois
import concurrent.futures
from typing import List, Dict
import os
from time import sleep

def get_hostname(domain: str) -> Dict[str, str]:
    result = {"domain": domain, "hostname": "", "ip": "", "isp": "", "error": ""}
    try:
        ip = socket.gethostbyname(domain)
        result["ip"] = ip
        
        hostname = socket.gethostbyaddr(ip)[0]
        result["hostname"] = hostname
        
        w = whois.whois(domain)
        result["isp"] = w.get("org", "Unknown ISP")
        
    except socket.gaierror:
        result["error"] = "Failed to resolve domain"
    except Exception as e:
        result["error"] = str(e)
    
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(f"Domain: {result['domain']}, Hostname: {result['hostname']}, IP: {result['ip']}, ISP: {result['isp']}, Error: {result['error']}\n")
    
    return result

def process_domains(domains: List[str]) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_domain = {executor.submit(get_hostname, domain): domain for domain in domains}
        for future in concurrent.futures.as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                result = future.result()
                print(f"Processed {domain}: {result['hostname']} ({result['ip']})")
            except Exception as e:
                print(f"Error processing {domain}: {str(e)}")
            sleep(0.1)

def main():
    input_file = "list.txt"
    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found!")
        return
    
    with open(input_file, "r", encoding="utf-8") as f:
        domains = [line.strip() for line in f if line.strip()]
    
    if not domains:
        print("Error: No domains found in list.txt!")
        return
    
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write("")

    print("Starting hostname extraction...")
    process_domains(domains)
    print("Scanning complete. Results saved to result.txt")

if __name__ == "__main__":
    main()
