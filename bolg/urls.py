from django.urls import path
from django.conf.urls import url
import bolg.views as bv

urlpatterns = [
    path('index/', bv.index, name='main-view'),
    path('article/<article_id>/', bv.article_page, name='article_page'),
]

app_name = 'blog'