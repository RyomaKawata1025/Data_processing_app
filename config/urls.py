
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views

urlpatterns = [
    path('stock_price/', include('stock_price.urls')),
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='home.html'),name='home'),
    path('accounts/',include('allauth.urls')),
    #path('accounts/login/',views.LoginView.as_view(),name='login')
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)