from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
def direct(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)

def index(request):
    # item_list = Item.objects.all()
    # return HttpResponse(item_list)
    return(HttpResponse("<h1>Hello HAI Gays I Love You <>"))

def item(request):
    return(HttpResponse("<b2>Hai Whats it<h2>"))

def context(request):
    item_list =Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {

    }
    return HttpResponse(template.render(context,request))

def clear_view(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/proper_index.html')
    context = {
        'item_list': item_list,
    }

    return HttpResponse(template.render(context,request))

def html_view(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/using_html.html')
    context = {
        'item_list': item_list,
    }

    return HttpResponse(template.render(context,request))


def short_html(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/using_html.html')
    context = {
        'item_list': item_list,
    }

    return render(request,'food/using_html.html',context)

def detail(request,item_id):
    return HttpResponse("This is item no/id %s"% item_id)

def particular_detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/click_get.html',context)
    # return HttpResponse("This is item no/id: %s" % item_id)
