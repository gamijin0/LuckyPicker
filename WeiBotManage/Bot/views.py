from django.shortcuts import render_to_response,RequestContext,redirect,resolve_url
from django.contrib import messages
from .models import Bot_db,WeiBo_db,Blogger_db,TransmitedRelationship
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
            if(bot_db.isValid==True):
                bot_db.message_num = one.GetMessages()
        else:
            # 无cookies必无效
            bot_db.isValid = False
        bot_db.save()
    return redirect(resolve_url(to='botManage'))


#搜索合适的微博并存入数据库,以便以后使用
def SearchAndStore(request):
    if(request.method=='GET'):
        bot_db = Bot_db.objects.all()[0]
        one = Bot(
            username=bot_db.username,
            password=bot_db.password,
            type="None",
            headers=bot_db.cookies,
        )
        try:
            search_res_list = one.Search(u'微博抽奖平台 红包')
            for tu in search_res_list:
                weibo = WeiBo_db(id=tu[1],content=tu[2])
                blogger = Blogger_db(uid=tu[0])
                blogger.save()
                weibo.blogger = blogger
                weibo.save()
                print("one WeiBo added into database")
            messages.success(request,"[%d]条数据被搜索到." % len(search_res_list))
        except Exception as e:
            messages.error(request, str(e))

    return redirect(resolve_url(to='botManage'))


#显示当前搜索到的微博信息
def showWeiBoInfo(request):
    weibo_list = WeiBo_db.objects.all()
    kwvars={
        'weibo_list':weibo_list,
    }
    return render_to_response("Bot/weiboList.html",kwvars,RequestContext(request))


#转发并关注
def careAndTransmit(request):
    LIMIT_NUM = 1 #转发限制
    limit = 1
    bot_db_list = Bot_db.objects.all()
    for bot_db in bot_db_list:
        if(bot_db.isValid==True):
            one = Bot()
            one.set(bot_db=bot_db)
            for weibo in WeiBo_db.objects.all():
                one.Care(uid=weibo.blogger.uid)
                if(len(TransmitedRelationship.objects.filter(weibo_id=weibo.id,bot_id=bot_db.username))==0):
                    one.TransmitWeibo(content="手动比心...",id=weibo.id)
                    limit+=1
                    if(limit>LIMIT_NUM):
                        break
                else:
                    print("账号[%s]已经转发过微博[%s]." % (bot_db.username,weibo.id))

    return redirect(resolve_url(to='botManage'))