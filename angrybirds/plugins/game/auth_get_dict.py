import datetime
import os
import time
import socket
import subprocess
import signal


def kill_port(port: str):
    cmd = "netstat -nlp | grep :%s| awk '{print $7}' | awk -F \"/\" '{ print $1 }'" % port
    status, output = subprocess.getstatusoutput(cmd)
    if status != 0 or output == '':
        return False
    pids = output.split('\n')
    if output.startswith("("):
        pids = pids[2:]
    elif output.startswith("（"):
        pids = pids[1:]
    elif len(pids) == 0:
        return False
    for pid in pids:
        try:
            os.kill(int(pid), signal.SIGKILL)
        except OSError:
            pass


def recv_data(port, ip='127.0.0.1'):
    if not isinstance(port, int):
        port = int(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for _ in range(300):
        try:
            s.connect((ip, port))
            data = s.recv(4)
            s.shutdown(2)
            break
        except Exception as e:
            time.sleep(0.2)
            data = e
    return True, data


def main(auth_dict):
    begin = datetime.date(2020, 5, 1)
    end = datetime.date(2020, 12, 30)
    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        real_time = day.strftime("%m/%d/%Y")
        real_time += " 08:00:00"
        cmd = f'date -s "{real_time}";hwclock -w'  # 设置时间并写入bios
        os.system(cmd)
        cmd = "/bin/sh -c \"/home/ptd/work/authserver_pku_10/bin/stopauthsh\""
        with open(os.devnull, 'w') as devnull:
            subprocess.Popen(
                cmd,
                shell=True,
                stdout=devnull,
                stderr=devnull,
                encoding='utf-8',
                cwd="/home/ptd/work/authserver_pku_10/bin/",
            )
        kill_port(str(55555))
        cmd = "rm -rf /usr/lib/.libuuu.so"
        os.system(cmd)
        cmd = "/home/ptd/work/authserver_pku_10/bin/authserver -d"
        with open(os.devnull, 'w') as devnull:
            subprocess.Popen(
                cmd,
                shell=True,
                stdout=devnull,
                stderr=devnull,
                encoding='utf-8',
                cwd="/home/ptd/work/authserver_pku_10/bin/",
            )
        res, data = recv_data(55555)
        if not res:
            raise Exception(res)
        auth_dict[day.strftime("%m/%d/%Y")] = data


if __name__ == '__main__':
    auth_dict = {}
    try:
        main(auth_dict)
    except Exception as e:
        print(repr(e))
    finally:
        print(auth_dict)
