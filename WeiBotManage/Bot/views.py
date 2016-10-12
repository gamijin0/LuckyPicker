from django.shortcuts import render_to_response,RequestContext,redirect,resolve_url
from django.contrib import messages
from .models import Bot
# Create your views here.

def manage(request):
    botlist = Bot.objects.all()
    kwvars={
        'botlist':botlist,
    }
    return render_to_response("Bot/manage.html",kwvars,RequestContext(request))

def addBot(request):

    try:
        if(request.method=="POST"):
            one = Bot(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if(one.username=="" or one.password==""):
                raise Exception("账号或密码不能为空.")
            one.save()
    except Exception as e:
        print(e)
        messages.error(request,str(e))

    return redirect(resolve_url(to='botManage'))