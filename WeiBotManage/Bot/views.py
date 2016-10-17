from django.shortcuts import render_to_response,RequestContext,redirect,resolve_url
from django.contrib import messages
from .models import Bot_db
from .bot import Bot
# Create your views here.

#显示管理页面
def manage(request):
    botlist = Bot_db.objects.all()
    kwvars={
        'botlist':botlist,
    }
    return render_to_response("Bot/manage.html",kwvars,RequestContext(request))


#用于添加用户
def addBot(request):

    try:
        if(request.method=="POST"):
            one = Bot_db(
                username=str(request.POST['username']).replace(' ',''),
                password=request.POST['password']
            )
            if(one.username=="" or one.password==""):
                raise Exception("账号或密码不能为空.")
            print("One Bot[%s] added." % (one.username))
            one.save()
    except Exception as e:
        messages.error(request,str(e))

    return redirect(resolve_url(to='botManage'))

#用于删除用户
def delBot(request):
    try:
        if (request.method == "POST"):
            oneToDel = Bot_db.objects.get(username=request.POST['username'])
            if(oneToDel.isValid==True):
                raise Exception("无法删除正在运行的账号！")
            Bot_db.delete(oneToDel)
            print("One Bot[%s] deleted." % (oneToDel.username))
    except Exception as e:
        print(e)
        messages.error(request, str(e))

    return redirect(resolve_url(to='botManage'))


#用于添加cookies
def addCookies(request):
    try:
        if(request.method=="POST"):
            one =Bot_db.objects.get(username=request.POST['username'])
            headers_dict = headerParser(str(request.POST['newCookies']).strip())
            one.cookies = str(headers_dict).replace('\r','')
            print("Bot[%s]'s cookies added." % (one.username))
            one.save()
    except Exception as e:
        messages.error(request,str(e))

    return redirect(resolve_url(to='botManage'))



#将headers解析位dict
def headerParser(headers:str):

    #分行
    res=[]
    headers = str(headers).replace('\r','').replace(' ','')
    res = headers.split('\n')
    res=res[1:]
    #将每行转化为dict
    res_dict = dict()
    for line in res:
        res_dict.setdefault(str(line).split(':')[0],str(line).split(':')[1])

    #将res_dict['Cookie']的值转化为dict
    cookie_dict = dict()
    for d in str(res_dict['Cookie']).split(';'):
        cookie_dict.setdefault(str(d).split('=')[0],str(d).split('=')[1])
    res_dict['Cookie'] = cookie_dict
    return res_dict


#页面上手动执行检查Bot状态
def checkBotStatusManually(request):

    bot_dblist = Bot_db.objects.all()
    for bot_db in bot_dblist:
        if (len(bot_db.cookies) != 0):
            # 若有cookie则进行检查
            one = Bot(
                username=bot_db.username,
                password=bot_db.password,
                type="None",
                headers=bot_db.cookies
            )
            bot_db.isValid = one.gotoIndex()  # 返回bool
        else:
            # 无cookies必无效
            bot_db.isValid = False
        bot_db.save()
    return redirect(resolve_url(to='botManage'))