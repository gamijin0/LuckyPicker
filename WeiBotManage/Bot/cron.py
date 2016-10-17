from django_cron import CronJobBase,Schedule
from .models import Bot_db as Bot_db
from .bot import Bot


class BotLoginCheck(CronJobBase):
    # 用于循环检查所有的Bot的状态
    RUN_EVERY_MINS = 1 #every 1 mins

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    code = 'WeiBot.LoginCheck' # a unique code

    def do(self):
        botlist = Bot_db.objects.all()
        for bot_db in botlist:
            if(len(bot_db.cookies)!=0):
                #若有cookie则进行检查
                one = Bot(
                    username=bot_db.username,
                    password=bot_db.password,
                    type="None",
                    headers=bot_db.cookies
                )
                bot_db.isValid = one.gotoIndex() #返回bool
            else:
                #无cookies必无效
                bot_db.isValid=False
            bot_db.save()