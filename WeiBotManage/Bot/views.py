from django.shortcuts import render

# Create your views here.

def manage(request):

    return render(request=request, template_name="Bot/manage.html")