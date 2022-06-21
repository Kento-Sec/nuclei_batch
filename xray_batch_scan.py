# python3 bat.py

import os
import hashlib
import re

# 扫描
import argparse


def get_url():
    # parser = argparse.ArgumentParser(description="xray_batch_scan.py")
    # parser.add_argument("-f", "--file", type=str, metavar="file", help="txt目标路径 eg:\"/XX/XX/xx.txt\"")
    # args = parser.parse_args()
    # target_file = args.file
    target_file = open("target.txt")
    lines = target_file.readlines()
    pattern = re.compile(r'^(https|http)://')
    for line in lines:
        try:
            if not pattern.match(line.strip()):
                targeturl="http://"+line.strip()
            else:
                targeturl=line.strip()
            outputfilename=hashlib.md5(targeturl.encode("utf-8"))
            do_scan(targeturl.strip(), outputfilename.hexdigest())
        except Exception as e:
            print(e)
            pass
    target_file.close()
    print("Xray Scan End~")
    return

# 报告
def do_scan(targeturl,outputfilename="test"):
    scan_command="./xray webscan --basic-crawler {} --html-output {}.html".format(targeturl,outputfilename)
    # scan_command = "ping 943ogg.dnslog.cn"
    # print(scan_command)
    os.system(scan_command)
    return

if __name__ == '__main__':
    get_url()

