import requests
from lxml import etree
from requests.exceptions import ConnectTimeout, ConnectionError

    # 使用方法请翻到最下方
class GraduateSession:
    
    def __init__(self, username, password) -> None:
        # 初始化request session对象
        self.username = username
        self.password = password
        self.headers = headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://tis.sustech.edu.cn/',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}
        self.session = requests.session()
        # 为session对象提前添加headers
        self.session.headers.update(self.headers)
        
        self.execution = ""

    def login(self):
        self.getJSession()
        self.getExecution()
        self.CasLogin()

    def getJSession(self):
        print("开始登录")
        # 首先打开tis页面获取JSESSIONID 和route参数
        try:
            resp = self.session.get("https://tis.sustech.edu.cn/")
            print(resp.status_code)
            if(resp.status_code == 200):
                print("获取jssessionid route cookies参数成功")
        except ConnectTimeout as e:
            print("获取登录参数 连接超时")
            print(e)
            exit
        except  ConnectionError as e:
            print("获取登录参数错误 连接错误")
            print(e)
            exit

    def getExecution(self):
        print("获取execution参数")
        params = { 'service': 'https://tis.sustech.edu.cn/cas' }
        try:
            resp = self.session.get('https://cas.sustech.edu.cn/cas/login', params=params)
            print(resp.status_code)
            # exection参数隐藏在了html页面当中
            service_html = resp.text
            self.execution = self.getExecutionCookies(service_html)

        except ConnectTimeout as e:
            print("execution 获取出错")
            print(e)
            exit(-1)

        except ConnectionError as e:
            print("execution 获取出错")
            print(e)
            exit(-1)

    def CasLogin(self):
        params = { 'service': 'https://tis.sustech.edu.cn/cas' }

        data = {
            'username': self.username,
            'password': self.password,
            'execution': self.execution,
            '_eventId': 'submit',
            'geolocation': '',
        }
        login_url = "https://cas.sustech.edu.cn/cas/login"
        try:
            resp = self.session.post(params=params, data=data, url=login_url)
            print(resp.text)
            print(resp.status_code)
            print("登录成功")
        except ConnectTimeout as e:
            print("CAS 登录超时")
            print(e)
            exit(-1)
        except ConnectionError as e:
            print("CAS 登录连接错误")
            print(e)
            exit(-1)

    def getExecutionCookies(self, html:str):
        html_etree = etree.HTML(html)
        execution = str(html_etree.xpath("//section[@class='cas-field']//input[@name='execution']/@value")[0])
        print(execution)
        return execution
    
if __name__ == '__main__':
    # 使用前需要设置好用户名和密码
    username = "xxxxxxxx"
    password = "xxxxxxxx"

    # 用用户名和密码初始化session对象
    session = GraduateSession(username, password)
    session.login()  # 登录cas和tis系统

    # 后面就可以调用session对象的方法来请求页面了

    session.get("xxxxxx")