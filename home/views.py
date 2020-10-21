from django.views.generic import TemplateView
from django.http import HttpResponse

class HomeView(TemplateView):
    template_name = 'home/main.html'
    
def hello(request):
    view_count = str(int(request.COOKIES.get('view_count', 0)) + 1)
    response = HttpResponse('view count=' + view_count)
    response.set_cookie('view_count', view_count)
    if 'dj4e_cookie' not in request.COOKIES:
        response.set_cookie('dj4e_cookie', '8aa903e4', max_age=1000)
    return response
