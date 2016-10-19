from bot import Bot
# from .bot import Bot
if __name__=="__main__":
    one = Bot(
        username="13711119526",
        password="E2ilPE5t7",
        type="None",

        headers="{'Host': 'm.weibo.cn', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip,deflate', 'Cookie': {'SSOLoginState': '1476809913', 'M_WEIBOCN_PARAMS': 'featurecode%3D20000181%26fid%3D1005053227846251%26uicode%3D10000011', 'H5_INDEX': '3', 'H5_INDEX_TITLE': 'ChaosKin9', '_T_WM': '3174d550c3d913475e78e9fb5646ebbb', 'SCF': 'Ap2iLAJlczRzygt24OgHKivZWtgp_Hrepnrz1n3dsDocTjE9B_VSs4taCOw9oblXlm_8X1kDzE-pPeYDmMIycVQ.', 'SUB': '_2A251AiTpDeTxGeVM71cZ9ijEyz2IHXVWDUyhrDV6PUJbkdBeLUbmkW2M5Ti262FMkw0gVh8h4h-Ctp-2WA..', 'SUHB': '0mxkdGq62Yq-c0', '_TTT_USER_CONFIG_H5': '%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A10%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D'}, 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Connection': 'keep-alive'}"
    )
    # # one.login()
    # # one.saveHTML()
    one.gotoIndex()
    # one.GetMessages()
    one.TransmitWeibo("@ExcuteK 张宇是个大傻逼",4030469299805026)
    #one.Care(1863157844)
    # one.Search(content=u"微博抽奖平台　红包")