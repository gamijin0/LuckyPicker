from django.shortcuts import render,render_to_response,RequestContext
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
def index(request):

    return render_to_response(template_name="common/index.html",context=RequestContext(request))