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
    headers = dict()
    cookies = dict()
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