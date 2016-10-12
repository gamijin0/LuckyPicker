import requests
from selenium import webdriver

class Bot:
    # attrs
    username = str
    password = str

    #if use selenium###################
    driver_type = str
    driver = None
    ###################################

    #if use requests###################
    session = requests.session()
    headers = {
        'Host': "passport.weibo.cn",
        'User - Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'Accept - Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept - Encoding': "gzip, deflate, br",
        'Content - Type': "application/x-www-form-urlencoded",
        'Referer': "https://passport.weibo.cn/signin/login",
        'Connection': "keep-alive",
    }
    cookies = {
            'H5_INDEX': "3",
            'M_WEIBOCN_PARAMS': "uicode=20000174",
            'H5_INDEX_TITLE': "ChaosKin9",
            'SCF': "Alhi3iuZKNjYbnL77hWoMvkQoE4edClB0S5n_r6NteS2u6p08-Xjk7DnXr_Em6P9tglZ1FZUg-UySu_l2XM-Ex8.",
            'SSOLoginState': "1476280075",
            'SUB': "_2A256-k9bDeTxGeNI7lYU9ybMyDuIHXVWBVETrDV6PUJbkdBeLWnfkW1NwRHJE8cEDUvnNpgMcOSDacgpTQ..",
            'SUHB': "0oUoVUAEYRaUmO",
            '_T_WM': "d84a71d49bc7c7fb49b88edf731f55a3",
        }
    ###################################


    page_source =str
    isLogined = bool
    loginURL = "https://passport.weibo.cn/signin/login"
    indexURL = "http://m.weibo.cn/"
    # funcs


    """
    初始化函数
    """
    def __init__(self,username:str,password:str,type:str = "PhantomJS",cookies:dict=dict()):
        self.username = username
        self.password = password
        self.driver_type = type

        if(self.driver_type=="PhantomJS"):
            self.driver = webdriver.PhantomJS()
        elif(self.driver_type=="FireFox"):
            self.driver = webdriver.Firefox()
        elif(self.driver_type=="None"):
            self.driver=None

        self.cookies = cookies

        #设置窗口大小以防止js不绘制
        if(self.driver is not None):
            self.driver.set_window_size(800,600)


    #用于打印页面代码
    def printHTML(self):
        print(self.driver.page_source)

    #保存页面以检查
    def saveHTML(self):
        try:
            #创建文件夹
            if(self.driver is not None):
                self.page_source = self.driver.page_source
            import os
            filepath = "./TempHTML"
            if(os.path.exists(filepath)==False):
                os.mkdir(filepath)
            #文件名
            import datetime
            filename = "%s[%s].htm" % (self.username,str(datetime.datetime.now())[-12:-7])
            #存储html
            with open(os.path.join(filepath,filename),'w') as f:
                f.write(self.page_source)

        except Exception as e:
            print(e)
            exit(1)

    #访问主页
    def gotoIndex(self):

        if(self.driver is None):
            #使用requests访问
            res=self.session.get(url=self.indexURL,cookies = self.cookies)
            self.page_source = res.content.decode('gb2312')
        else:
            #使用webdriver访问
            pass