import os #line:1
import re #line:2
import threading #line:3
import platform #line:4
from colorama import init ,Fore ,Style #line:5
init (autoreset =True )#line:7
def parse_credentials (O00O0OO0OO0000O00 ,OOO000O0OO0OOO00O ,O0OOOO0O00O0OOOO0 ,O0O00O0OO0OO0O0OO ):#line:9
    O0000OOOOO0OOOOO0 =[r'(https?://[^\s]*wp-login\.php):([^\s:]+):([^\s:]+)',r'(https?://[^\s]*wp-login\.php)\|([^\s|]+)\|([^\s|]+)',r'(https?://[^\s]*wp-login\.php)#([^\s@]+)@([^\s@]+)',r'(https?://[^\s]*wp-login\.php)#([^\s@]+)@([^\s@]+)@([^\s@]+)',r'(https?://[^\s]*wp-login\.php)\s*:\s*([^\s:]+)\s*:\s*([^\s:]+)']#line:16
    try :#line:18
        with open (O00O0OO0OO0000O00 ,'r',encoding ='utf-8',errors ='ignore')as OOOO0OO0O0000000O :#line:19
            for OOO000O0O0O0O00O0 in OOOO0OO0O0000000O :#line:20
                for O0OO0000OOO00O000 in O0000OOOOO0OOOOO0 :#line:21
                    try :#line:22
                        OOO0000O0OOOOOOOO =re .findall (O0OO0000OOO00O000 ,OOO000O0O0O0O00O0 ,re .IGNORECASE )#line:23
                        for O0O0O0OO0O0O00O00 in OOO0000O0OOOOOOOO :#line:24
                            OOO000OOOO00OOO0O =O0O0O0OO0O0O00O00 [0 ]#line:25
                            with O0OOOO0O00O0OOOO0 :#line:26
                                if len (O0O0O0OO0O0O00O00 )==3 :#line:27
                                    O000O0OOO0O0O0OO0 =f"{OOO000OOOO00OOO0O}@{O0O0O0OO0O0O00O00[1]}#{O0O0O0OO0O0O00O00[2]}"#line:28
                                elif len (O0O0O0OO0O0O00O00 )==4 :#line:29
                                    O000O0OOO0O0O0OO0 =f"{OOO000OOOO00OOO0O}@{O0O0O0OO0O0O00O00[1]}#{O0O0O0OO0O0O00O00[2]}@{O0O0O0OO0O0O00O00[3]}"#line:30
                                if O000O0OOO0O0O0OO0 not in OOO000O0OO0OOO00O :#line:31
                                    OOO000O0OO0OOO00O .add (O000O0OOO0O0O0OO0 )#line:32
                                    print (f"{Style.RESET_ALL}[{Fore.GREEN}+{Style.RESET_ALL}] {O000O0OOO0O0O0OO0} {Style.RESET_ALL}[ {Fore.GREEN}FOUND{Style.RESET_ALL} ]")#line:34
                                    with open (O0O00O0OO0OO0O0OO ,'a',encoding ='utf-8')as OOOOOO00OO0O0O0OO :#line:35
                                        OOOOOO00OO0O0O0OO .write (f"{O000O0OOO0O0O0OO0}\n")#line:36
                    except re .error as OOOOO0O0O000O0O00 :#line:37
                        print (f"{Style.RESET_ALL}[{Fore.RED}!{Style.RESET_ALL}] Regex error in {O00O0OO0OO0000O00} for pattern {O0OO0000OOO00O000}: {OOOOO0O0O000O0O00}")#line:38
    except Exception as OO0000OO000OOOO0O :#line:39
        print (f"{Style.RESET_ALL}[{Fore.RED}!{Style.RESET_ALL}] Error reading {O00O0OO0OO0000O00}: {OO0000OO000OOOO0O}")#line:40
def extract_credentials_from_folder (OOO00000OO00O000O ,OO0OO00OOOOOOOOOO ,O0OO0OOO00OO0OOO0 ):#line:42
    open (OO0OO00OOOOOOOOOO ,'w',encoding ='utf-8').close ()#line:43
    O000OOO0OO00O0O0O =set ()#line:44
    O0OO0O0O00O00OO0O =threading .Lock ()#line:45
    O0OO00OOOOOOOOOOO =[]#line:46
    O000000OO0O0OOO0O =[OOO0OO0O0000OO00O for OOO0OO0O0000OO00O in os .listdir (OOO00000OO00O000O )if OOO0OO0O0000OO00O .endswith ('.txt')]#line:47
    if not O000000OO0O0OOO0O :#line:49
        print (f"{Style.RESET_ALL}[{Fore.RED}!{Style.RESET_ALL}] Tidak ada file .txt di {OOO00000OO00O000O}.")#line:50
        return #line:51
    def O000000OOOOOOO0OO ():#line:53
        while O000000OO0O0OOO0O :#line:54
            OO0000OOOOO0OO000 =O000000OO0O0OOO0O .pop ()#line:55
            O0O0O00000OOO00OO =os .path .join (OOO00000OO00O000O ,OO0000OOOOO0OO000 )#line:56
            parse_credentials (O0O0O00000OOO00OO ,O000OOO0OO00O0O0O ,O0OO0O0O00O00OO0O ,OO0OO00OOOOOOOOOO )#line:57
    for _OO0O000000000OO00 in range (min (O0OO0OOO00OO0OOO0 ,len (O000000OO0O0OOO0O ))):#line:59
        O0O000O00OO0OO000 =threading .Thread (target =O000000OOOOOOO0OO )#line:60
        O0OO00OOOOOOOOOOO .append (O0O000O00OO0OO000 )#line:61
        O0O000O00OO0OO000 .start ()#line:62
    for O0O000O00OO0OO000 in O0OO00OOOOOOOOOOO :#line:64
        O0O000O00OO0OO000 .join ()#line:65
    print (f"{Fore.GREEN}Hasil disimpan ke {OO0OO00OOOOOOOOOO}{Style.RESET_ALL}")#line:67
def main ():#line:69
    if platform .system ()=="Windows":#line:71
        os .system ('cls')#line:72
    else :#line:73
        os .system ('clear')#line:74
    print (f"""
{Fore.WHITE}
 ██████╗ ██╗  ██╗███████╗ █████╗ ██╗     ███████╗██╗  ██╗██╗████████╗██╗  ██╗███████╗███╗   ███╗ █████╗ 
██╔═══██╗╚██╗██╔╝╚════██║██╔══██╗██║     ██╔════╝╚██╗██╔╝██║╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔══██╗
██║   ██║ ╚███╔╝    ██╔╝ ███████║██║     █████╗   ╚███╔╝ ██║   ██║   ███████║█████╗  ██╔████╔██║███████║
██║   ██║ ██╔██╗   ██╔╝  ██╔══██║██║     ██╔══╝   ██╔██╗ ██║   ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══██║
╚██████╔╝██╔╝ ██╗  ██║   ██║  ██║███████╗███████╗██╔╝ ██╗██║   ██║   ██║  ██║███████╗██║ ╚═╝ ██║██║  ██║
 ╚═════╝ ╚═╝  ╚═╝  ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝

 > KALO ADA ERROR KE ALEX ASMODEUS AJA DIA YANG BUAT TOOLS INI
{Style.RESET_ALL}
    """)#line:88
    O00O0000O0O00000O =input ("Masukkan directory yang berisi .txt: ").strip ()#line:90
    O0000000OO0O0OOOO =input ("Masukkan nama result (example: result.txt): ").strip ()#line:91
    O0O0O0OOO0O000OOO =int (input ("Masukkan Threads: "))#line:92
    O0OOOO0OOO000OO0O =input ("Mamulakan scan! Adakah kamu mau melanjutkan? (y/n): ").strip ().lower ()#line:93
    if O0OOOO0OOO000OO0O !='y':#line:95
        print (f"{Style.RESET_ALL}[{Fore.RED}!{Style.RESET_ALL}] Scan dibatalkan.")#line:96
        return #line:97
    if not os .path .isdir (O00O0000O0O00000O ):#line:99
        print (f"{Style.RESET_ALL}[{Fore.RED}!{Style.RESET_ALL}] Directory {O00O0000O0O00000O} tidak valid.")#line:100
        return #line:101
    extract_credentials_from_folder (O00O0000O0O00000O ,O0000000OO0O0OOOO ,O0O0O0OOO0O000OOO )#line:103
if __name__ =="__main__":#line:105
    main ()
