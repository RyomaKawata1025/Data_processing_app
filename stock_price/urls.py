
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nikkei/',views.nikkei,name='nikkei'),
    path('sp500/',views.sp500,name='sp500'),
    path('usdjpy/',views.usdjpy,name='usdjpy'),
    path('bitcoin/',views.bitcoin,name='bitcoin'),
    path('plot_comparison/', views.get_svg_comparison, name='plot_comparison'),

]
