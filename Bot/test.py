from bot import Bot
import sys,os
import WeiBotManage
from WeiBotManage.Bot.models import  Bot as Bot_db

sys.path.append(os.path.abspath("../"))
os.environ['DJANGO_SETTINGS_MODULE']='WeiBotManage.WeiBotManage.settings'
from WeiBotManage.WeiBotManage import settings
from WeiBotManage.Bot.models import  Bot as Bot_db
if __name__=="__main__":
    #
    # one = Bot(username="15995097268",password="xlsd1996",type="None")
    # # one.login()
    # # one.saveHTML()
    # one.gotoIndex()
    # one.saveHTML()
    # print(os.path.abspath("../"))
    print(Bot_db.objects.all())
    # TODO: use sqlalchemy to get bot data