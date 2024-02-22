# 南方科技大学研究生教务系统登录API

## 使用方法

**安装依赖**

`pip install requests`
`pip install lxml`

**填入用户名和密码**

```py
if __name__ == '__main__':
    # 使用前需要设置好用户名和密码
    username = "xxxxxxxx"
    password = "xxxxxxxx"
```

**初始化session对象**
```py
    # 用用户名和密码初始化session对象
    session = GraduateSession(username, password)
    session.login()  # 登录cas和tis系统
```

然后可以用session对象执行 GET POST 等一系列请求
```py
session.get(url)
```

具体使用依场景而定

抢课、自动化操作、签到

CAS系统登录原理也适用于校内其他系统
