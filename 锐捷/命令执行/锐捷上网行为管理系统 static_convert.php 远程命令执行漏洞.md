1.漏洞介绍：
:::info
   锐捷上网行为管理系统/view/IPV6/naborTable/static_convert.php接口存在任意命令执行漏洞。攻击者可以通过漏洞执行任意命令从而获取服务器权限，可能导致内网进一步被攻击。
:::
2.语法：

- Fofa：
```
body="c33367701511b4f6020ec61ded352059"
```

- Hunter
```
body="c33367701511b4f6020ec61ded352059"
```

- Quake
```
body="c33367701511b4f6020ec61ded352059"
```
首页：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/40540518/1719492580968-c6728884-8c78-49f6-b44e-046701244a6d.png#averageHue=%23fefefe&clientId=u8585b10d-d6a6-4&from=paste&height=526&id=u4a281608&originHeight=657&originWidth=1405&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=75935&status=done&style=none&taskId=ubce25ebe-4059-4c99-8ada-9dec0ccd480&title=&width=1124)
复现：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/40540518/1719492557983-49bccf89-8f7c-4b25-bdf7-bcb0b36c5244.png#averageHue=%23f9f8f8&clientId=u8585b10d-d6a6-4&from=paste&height=418&id=u5efac41c&originHeight=522&originWidth=1232&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=86304&status=done&style=none&taskId=ua97ee79a-5a89-44c5-b348-4508486fac6&title=&width=985.6)
携带poc
