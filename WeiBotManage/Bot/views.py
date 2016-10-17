from django.shortcuts import render_to_response,RequestContext,redirect,resolve_url
from django.contrib import messages
from .models import Bot
# Create your views here.

#显示管理页面
def manage(request):
    botlist = Bot.objects.all()
    kwvars={
        'botlist':botlist,
    }
    return render_to_response("Bot/manage.html",kwvars,RequestContext(request))


#用于添加用户
def addBot(request):

    try:
        if(request.method=="POST"):
            one = Bot(
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
            oneToDel = Bot.objects.get(username=request.POST['username'])
            if(oneToDel.isValid==True):
                raise Exception("无法删除正在运行的账号！")
            Bot.delete(oneToDel)
            print("One Bot[%s] deleted." % (oneToDel.username))
    except Exception as e:
        print(e)
        messages.error(request, str(e))

    return redirect(resolve_url(to='botManage'))


#用于添加cookies
def addCookies(request):
    try:
        if(request.method=="POST"):
            one =Bot.objects.get(username=request.POST['username'])
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
    from .cron import BotLoginCheck
    one = BotLoginCheck()
    one.do()
    return redirect(resolve_url(to='botManage'))