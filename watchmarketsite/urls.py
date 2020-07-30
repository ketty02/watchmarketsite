"""watchmarketsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from watchmarketsite.settings.views import homepage

admin.site.site_header = "WatchMarketSite"
admin.site.site_title = "Just in Time"
admin.site.index_title = "WatchMarketSite"



urlpatterns = [
    path('admin/', admin.site.urls, name='admin-view'),
    path('users/', include('users.urls')),
    path('users/activate', include('activation.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', include('django.contrib.auth.urls')),
    path('', view=homepage, name='homepage')
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#1 - Submit email form                        //PasswordResetView.as_view
#2 - Email sent success message               //PasswordResetDoneView.as_view
#3 - Link to password Rest form in email      //PasswordResetConfirmView.as_view
#4 - Password successfully changed message    //PasswordResetCompleteView.as_view