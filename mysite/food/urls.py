from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('item/',views.item,name='item'),
    path('direct/',views.direct,name='direct'),
    path('context/',views.context,name='context'),
    path('clear_view/',views.clear_view,name='clear_view'),
    path('html_view/',views.html_view,name='html_view'),
    path('short_html/',views.short_html,name='short_html'),
    #/food/1
    path('<int:item_id>/',views.detail,name='detail'),
    path('detail/<int:item_id>/',views.detail,name='detail'),
    path('particular_detail/',views.particular_detail,name='particular'),
]