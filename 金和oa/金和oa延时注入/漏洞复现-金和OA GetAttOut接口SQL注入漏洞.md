##### 1.漏洞描述
金和OA GetAttOut接口存在SQL注入漏洞。
##### 2.搜索语法：
```
搜索语法：
app="金和网络-金和OA" || body="/jc6/platform/sys/login"
```
##### 3.首页：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/40540518/1719834102324-d8579c99-a7af-4266-8e93-71ef5876bc10.png#averageHue=%2343563d&clientId=u13da1d70-b8d2-4&from=paste&height=720&id=u789430fb&originHeight=900&originWidth=1568&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2393277&status=done&style=none&taskId=u0f40d57d-914b-4c78-a5fb-8ecafdd7b5d&title=&width=1254.4)
##### 4.复现：
poc:
![image.png](https://cdn.nlark.com/yuque/0/2024/png/40540518/1719834721255-ba0829ee-f7b1-47b4-a0e3-33e7afd0045a.png#averageHue=%23f8f7f6&clientId=u13da1d70-b8d2-4&from=paste&height=770&id=u85524514&originHeight=963&originWidth=1241&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=140927&status=done&style=none&taskId=u052a9b93-caf2-4dfe-97a3-ac599fe33ed&title=&width=992.8)
