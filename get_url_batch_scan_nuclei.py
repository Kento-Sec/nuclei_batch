import argparse
import sys
import os

parser = argparse.ArgumentParser(description="get_url_batch_scan_nuclei.py")
parser.add_argument("-f", "--file", type=str, metavar="file", help="txt目标路径 eg:\"/XX/XX/xx.txt\"")
args = parser.parse_args()

if len(sys.argv) != 3:
    print(
        "[-]  参数错误！\neg1:>>>python get_url_batch_scan_nuclei.py -f txt存放路径 ")

target_file = args.file
open_target = open(target_file)

for line in open_target:
    print(line+"准备扫描=========")
    print("nuclei -me result -rl 300 -c 100 -vv -u "+line)
    run = os.system("nuclei -me result -rl 300 -c 100 -vv -v -u "+line)
    print(run)

print("完成！！！！！！！！！！")
open_target.close(target_file)
