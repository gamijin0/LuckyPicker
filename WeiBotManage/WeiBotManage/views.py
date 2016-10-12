from django.shortcuts import render,render_to_response,RequestContext

def index(request):

    return render_to_response(template_name="common/index.html",context=RequestContext(request))