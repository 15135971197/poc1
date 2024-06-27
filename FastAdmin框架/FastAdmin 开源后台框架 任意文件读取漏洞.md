1.介绍：
:::info
   FastAdmin 开源后台框架/index/ajax/lang接口存在任意文件读取漏洞，未经身份验证攻击者可通过该漏洞读取系统重要文件，例如数据库配置文件、系统配置文件等。
:::
2.：语法：

- Fofa：



```
body="/assets/js/require.js"
```

- Hunter
```
body="/assets/js/require.js"
```

- Quake



```
body="/assets/js/require.js"
```
3.
首页：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/40540518/1719494427876-5d71b013-c9a8-49d8-980f-ee4f85cdd72c.png#averageHue=%2392a6e2&clientId=ub063a226-d6f6-4&from=paste&height=664&id=ud73473a4&originHeight=830&originWidth=1454&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=48984&status=done&style=none&taskId=ue88078a2-b675-4746-a6d7-e2ace3b0a87&title=&width=1163.2)
4.
复现：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/40540518/1719494371829-0c7b15b4-56ac-47b9-b772-552dcea71fce.png#averageHue=%23fbfbfa&clientId=ub063a226-d6f6-4&from=paste&height=729&id=u8c7c7152&originHeight=911&originWidth=1160&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=84585&status=done&style=none&taskId=ua457959f-2ae4-4e7d-8c4c-243c26e6e46&title=&width=928)
