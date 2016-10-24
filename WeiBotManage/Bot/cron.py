from django_cron import CronJobBase,Schedule
from .models import Bot_db as Bot_db
from Bot.views import careAndTransmit

# 暂时不使用此功能

class BotLoginCheck(CronJobBase):
    # 用于循环检查所有的Bot的状态
    RUN_EVERY_MINS = 1 #every 1 mins

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)

    code = 'WeiBot.LoginCheck' # a unique code

    def do(self):
        careAndTransmit(None)