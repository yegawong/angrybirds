import subprocess
import os
import pwd
import socket


def check_openssl():
    cmd = "openssl version"
    status, output = subprocess.getstatusoutput(cmd)
    if status == 127:
        raise Exception("Not Found openssl, Please install OpenSSL-1.0.2o")
    elif status != 0:
        raise Exception("OpenSSL Failed, Please reinstall")
    t_ver = output.split()[1]
    res = compare_version(t_ver, '1.0.2o')  # t_ver <= '1.0.2o'
    if not res:
        raise Exception("Please install OpenSSL-1.0.2o")


def check_domain_connect(domain: str):
    cmd = "ping -w 1 -c 1 %s" % domain
    status, output = subprocess.getstatusoutput(cmd)
    if status != 0:
        return False
    return True


def get_domain_host(domain: str) -> str:
    if not check_domain_connect(domain):
        return False, None
    ip_list = []
    try:
        addrs = socket.getaddrinfo(domain, None)
        for item in addrs:
            if item[4][0] not in ip_list:
                ip_list.append(item[4][0])
        return True, ip_list[0]
    except Exception:
        return False, None


def get_username() -> str:
    return pwd.getpwuid(os.getuid())[0]


def check_access(file, execute=False):
    if execute:
        return os.access(file, os.R_OK | os.W_OK | os.X_OK)
    else:
        return os.access(file, os.R_OK | os.W_OK)


def check_port(port, ip='127.0.0.1'):
    if not isinstance(port, int):
        port = int(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        return True
    except Exception:
        return False


def check_qt(version) -> tuple:
    status, output = subprocess.getstatusoutput('qmake -v')
    if status != 0:
        return False, None
    s_index = output.find('Qt version ')
    e_index = output.find(' in ')
    t_ver = output[s_index + 11:e_index]
    return compare_version(version, t_ver), t_ver


def compare_version(v1: str, v2: str) -> bool:
    """ compare software version, if a <= b return True"""
    lenv1 = len(v1.split('.'))
    lenv2 = len(v2.split('.'))
    v1 = v1 + '.0' * (lenv2 - lenv1)
    v2 = v2 + '.0' * (lenv1 - lenv2)
    for i in range(max(lenv1, lenv2)):
        a = v1.split('.')[i]
        b = v2.split('.')[i]
        if not a.isdigit():
            a = a[0]
        if not b.isdigit():
            b = b[0]
        if int(a) > int(b):
            return False
    return True
