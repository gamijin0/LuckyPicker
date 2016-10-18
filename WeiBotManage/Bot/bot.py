import requests
from selenium import webdriver
from bs4 import BeautifulSoup

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
    headers = eval("{'Connection': 'keep-alive', 'Cookie': {'_T_WM': 'd84a71d49bc7c7fb49b88edf731f55a3', 'SUHB': '0k1yFH5UJVChAi', 'M_WEIBOCN_PARAMS': 'uicode%3D20000174', 'SCF': 'Alhi3iuZKNjYbnL77hWoMvkQoE4edClB0S5n_r6NteS2u6p08-Xjk7DnXr_Em6P9tglZ1FZUg-UySu_l2XM-Ex8.', 'SUB': '_2A256-08sDeTxGeVP71sX8CjOwz6IHXVWBFFkrDV6PUJbkdBeLWLlkW02jdHGyTIL9-KM1daXjNac-RdsbA..', 'SSOLoginState': '1476345724'}, 'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64;rv', 'Upgrade-Insecure-Requests': '1', 'Host': 'm.weibo.cn'}")
    cookies = dict()
    ###################################


    page_source =str
    isLogined = bool
    loginURL = "https://passport.weibo.cn/signin/login"
    indexURL = "http://m.weibo.cn/"
    messageURL = "http://m.weibo.cn/unread?t="
    # searchURL = "http://m.weibo.cn/p/index?containerid=100103type=&q="
    searchURL = "http://m.weibo.cn/container/getIndex?containerid=100103type"
    # funcs


    # 初始化函数
    def __init__(self,username:str,password:str,type:str = "PhantomJS",headers:str=""):
        self.username = username
        self.password = password
        self.driver_type = type

        if(self.driver_type=="PhantomJS"):
            self.driver = webdriver.PhantomJS()
        elif(self.driver_type=="FireFox"):
            self.driver = webdriver.Firefox()
        elif(self.driver_type=="None"):
            self.driver=None

        if(len(headers)!=0):
            self.headers=eval(headers.replace(' ','').replace('\r',''))

        #设置窗口大小以防止js不绘制
        if(self.driver is not None):
            self.driver.set_window_size(800,600)


    #用于打印页面代码#
    def printHTML(self):
        print(self.driver.page_source)

    #保存页面以检查#
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
            now = datetime.datetime.now()
            filename = "[%s日%s时%s分]%s.htm" % (now.day,now.hour,now.minute,self.username)
            #存储html
            with open(os.path.join(filepath,filename),'w') as f:
                f.write(self.page_source)

        except Exception as e:
            print(e)
            exit(1)

    #访问主页,现用作登录测试
    def gotoIndex(self):
        if(self.driver is None):
            #使用requests访问
            self.cookies = self.headers.pop('Cookie')
            res=self.session.get(
                url=self.indexURL,
                headers = self.headers,
                cookies=self.cookies)
            self.page_source = res.content.decode('utf-8')
            if(res.status_code==200):
                print("Bot[%s] Login Successfully!" % self.username)
                return True
            else:
                print("Bot[%s] Login Failed,please check the res page and headers" % self.username)
                self.saveHTML()
                return False
        else:
            #使用webdriver访问
            pass

        return False

    #用于检查现在有多少未读消息
    def GetMessages(self):
        import time
        timestr = str(time.time())[0:12].replace('.','')
        self.messageURL+=timestr
        res=self.session.get(self.messageURL,
                         headers = self.headers,
                         cookies = self.cookies,
                         )
        import json
        res = json.loads(res.text)
        #print(res)
        # qp 是首页未读消息, ht 是私信消息
        if 'qp' in res and 'new' in res['qp']:
            print("账号[%s]有[%d]条新的首页消息." % (self.username,res['qp']['new']))
        if 'ht' in res and 'new' in res['ht']:
            print("账号[%s]有[%d]条新的私信消息." % (self.username,res['ht']['new']))
            return res['ht']['new']
        # 返回未读私信数量

        return 0


    #用户发送微博
    #content:文字内容
    def sendWeibo(self,content:str):

        data = {
            'content':content,
            'annotations': "",
            'st': "3afdec",
            }
        try:

            cookies = self.cookies
            headers = self.headers
            headers.setdefault("Referer","http://m.weibo.cn/mblog")

            resp = self.session.post(
                url="http://m.weibo.cn/mblogDeal/addAMblog",
                data=data,
                headers = self.headers,
                cookies = cookies,
            )
            # self.page_source=resp.content.decode('utf-8')
            # self.saveHTML()
            if(resp.status_code==200):
                import json,datetime
                res=json.loads(resp.text)
                if(res['ok']==1):
                    print("账号[%s]发送微博成功[%s]." % (self.username,datetime.datetime.now()))

        except Exception as e:
            print(e)


    #转发微博
    #content:微博评论.如需@用户，直接输入“@用户名“
    #id:微博id
    def TransmitWeibo(self,content:str,id:int):
        data={
            'content': content,
            'id':id,
            'annotations': "",
            'st':"aa11fd",
        }
        try:
            headers = self.headers
            headers.setdefault("Referer", "http://m.weibo.cn/repost?id=%d" %(id))
            resp=self.session.post(
                url="http://m.weibo.cn/mblogDeal/rtMblog",
                headers=headers,
                cookies=self.cookies,
                data=data,
            )
            if (resp.status_code ==200):
                import datetime
                print("账号[%s]转发微博成功[%s]." % (self.username, datetime.datetime.now()))
            #self.saveHTML()
            #self.page_source = resp.content.decode('utf-8')
            #print (resp)
        except Exception as e:
            print(e)


    #关注微博用户
    #uid:用户id
    def Care(self,uid:int):
        data={
            'uid':uid,
        }
        try:
            headers = self.headers
            headers.setdefault("Referer","http://m.weibo.cn/u/%d" %(uid))
            resp=self.session.post(
                url="http://m.weibo.cn/attentionDeal/addAttention?",
                headers=headers,
                cookies=self.cookies,
                data=data,
            )
            #无论是否已经关注，都返回关注
            if (resp.status_code ==200):
                 import datetime
                 print("账号[%s]关注用户%d成功[%s]." % (self.username,uid,datetime.datetime.now()))
        except Exception as e:
            print(e)


    #根据关键词进行搜索相关WeiBo
    #content:关键词
    #TODO:what should this func return ?
    def Search(self,content:str):
        import urllib
        queryStr = "=&q="+content
        queryStr = urllib.parse.quote(queryStr)
        referURL = "http://m.weibo.cn/p/index?containerid=100103type"+queryStr
        print(referURL)
        tmpHeaders = self.headers
        tmpHeaders.setdefault('Referer',referURL)
        res=self.session.get(
            url=self.searchURL+queryStr,
            cookies=self.cookies,
            headers = tmpHeaders,
        )
        import json
        res = json.loads(res.text)
        print(res)
        cards = res['cards']
        for i in cards[2]['card_group']:
            print("WeiBo_ID:"+str(i['mblog']['id']))
            print("USER_ID:"+str(i['mblog']['user']['id']))