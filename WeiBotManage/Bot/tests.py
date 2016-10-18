from bot import Bot
if __name__=="__main__":
    one = Bot(
        username="15995097268",
        password="xlsd1996",
        type="None",

        headers="{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive', 'Cookie': {'SUB': '_2A251AKuBDeTxGeVP7lcY9ibIwz6IHXVWCjXJrDV6PUJbkdBeLWX_kW1rc4s9zmzVyzzGznRGpVwmGijUUQ..', 'M_WEIBOCN_PARAMS': 'uicode%3D20000174', '_T_WM': 'd84a71d49bc7c7fb49b88edf731f55a3', 'SCF': 'Alhi3iuZKNjYbnL77hWoMvkQoE4edClB0S5n_r6NteS2u6p08-Xjk7DnXr_Em6P9tglZ1FZUg-UySu_l2XM-Ex8.', 'SSOLoginState': '1476713425', 'SUHB': '0WGs38QIif1oa5', '_TTT_USER_CONFIG_H5': '%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A10%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D'}, 'Host': 'm.weibo.cn', 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip,deflate', 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64;rv'}"
    )
    # # one.login()
    # # one.saveHTML()
    one.gotoIndex()
    one.GetMessages()
    #one.TransmitWeibo("@ExcuteK 张宇是个大傻逼",4030469299805026)
    #one.Care(1863157844)
    one.Search(content="微博抽奖平台 红包")