from bot import Bot
if __name__=="__main__":
    one = Bot(
        username="15995097268",
        password="xlsd1996",
        type="None",

        headers="{'Connection': 'keep-alive', 'Cookie': {'_T_WM': 'd84a71d49bc7c7fb49b88edf731f55a3', 'SUHB': '079TVdD54xI1s-', '_TTT_USER_CONFIG_H5': '%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A10%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D', 'M_WEIBOCN_PARAMS': 'uicode%3D20000174', 'SCF': 'Alhi3iuZKNjYbnL77hWoMvkQoE4edClB0S5n_r6NteS2u6p08-Xjk7DnXr_Em6P9tglZ1FZUg-UySu_l2XM-Ex8.', 'SUB': '_2A256-yTUDeTxGeVP71sX8CjOwz6IHXVWBEycrDV6PUJbkdBeLUX2kW0-nkOOBmmx4uJudbxsflI0NQlrcg..', 'SSOLoginState': '1476351108'}, 'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0(X11;Linuxx86_64;rv', 'Upgrade-Insecure-Requests': '1', 'Host': 'm.weibo.cn'}",
    )
    # # one.login()
    # # one.saveHTML()
    one.gotoIndex()
    one.GetMessages()