from selenium import webdriver

class Bot:
    # attrs
    username = str
    password = str
    driver_type = str
    driver = None
    isLogined = bool
    loginURL = "http://weibo.com/login.php"
    # funcs


    """
    初始化函数
    """
    def __init__(self,username:str,password:str,type:str = "PhantomJS"):
        self.username = username
        self.password = password
        self.driver_type = type

        if(self.driver_type=="PhantomJS"):
            self.driver = webdriver.PhantomJS()
        elif(self.driver_type=="FireFox"):
            self.driver = webdriver.Firefox()


    def login(self,loginURL = "http://weibo.com/login.php"):
        print("Login...")
        self.loginURL = loginURL
        self.driver.get("http://weibo.com/login.php")
        pass


