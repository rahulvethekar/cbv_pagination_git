from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from .models import Article
# Create your views here.

class ArticleView(View):
    def get(self,request):
        obj = Article.objects.all()
        paginator = Paginator(obj,2,orphans=1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        template_name = 'app1/article.html'
        context = {'page_obj':page_obj}
        return render(request,template_name,context)

        
