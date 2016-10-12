
#将headers解析位dict
def headerParser(headers:str):

    #分行
    res=[]
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




if(__name__=="__main__"):
    with open("headers.example",'r') as f:
        content = f.read()
    print(headerParser(content))
