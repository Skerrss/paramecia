import os
import re
import threading
from urllib.parse import urlparse
from colorama import init, Fore

init(autoreset=True)

def process_file(file_path, domain_set, lock, output_file):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            match = re.search(r"(https?://[^/\s]+|[^/\s]+\.(?:id|go\.id|ac\.id|sch\.id))", line)
            if match:
                raw_domain = match.group(0)
                if not raw_domain.startswith("http"):
                    raw_domain = "https://" + raw_domain
                allowed_extensions = ('.id', '.go.id', '.ac.id', '.sch.id')
                if raw_domain.endswith(allowed_extensions):
                    with lock:
                        if raw_domain not in domain_set:
                            domain_set.add(raw_domain)
                            print(f"{Fore.YELLOW}[ {Fore.RESET}Scanning {Fore.YELLOW}]{Fore.RESET} {raw_domain} {Fore.RESET}| {Fore.GREEN}[ FOUND ]{Fore.RESET}")
                            with open(output_file, "a", encoding="utf-8") as out_file:
                                out_file.write(raw_domain + "\n")

def extract_domains_from_folder(folder_path, output_file, max_threads):
    open(output_file, "w", encoding="utf-8").close()
    domain_set = set()
    lock = threading.Lock()
    threads = []
    files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

    def worker():
        while files:
            filename = files.pop()
            file_path = os.path.join(folder_path, filename)
            process_file(file_path, domain_set, lock, output_file)

    for _ in range(min(max_threads, len(files))):
        thread = threading.Thread(target=worker)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Extraction complete. {len(domain_set)} domains saved to {output_file}")

if __name__ == "__main__":
    print("""

███████╗██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗░░░░░░██████╗░░█████╗░███╗░░░███╗
██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝░░░░░░██╔══██╗██╔══██╗████╗░████║
█████╗░░░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░█████╗██║░░██║██║░░██║██╔████╔██║
██╔══╝░░░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░╚════╝██║░░██║██║░░██║██║╚██╔╝██║
███████╗██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░░░░░░░██████╔╝╚█████╔╝██║░╚═╝░██║
╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░░░░░░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝
    """)
    folder_path = input("Masukkan Folder Yang Berisi .txt : ")
    output_file = input("Masukkan Nama Output : ")
    max_threads = int(input("Masukkan Threads : "))
    extract_domains_from_folder(folder_path, output_file, max_threads)
