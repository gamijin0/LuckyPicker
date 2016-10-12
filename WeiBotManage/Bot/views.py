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
                username=request.POST['username'],
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
            one.cookies=request.POST['newCookies']
            print("Bot[%s]'s cookies added." % (one.username))
            one.save()
    except Exception as e:
        messages.error(request,str(e))

    return redirect(resolve_url(to='botManage'))