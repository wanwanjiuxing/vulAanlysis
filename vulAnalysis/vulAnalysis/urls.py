"""vulAnalysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,re_path
from vulList import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^api/youkeVulList/$',views.YoukeVulListView.as_view()),
    re_path('^api/youkeVulList/(?P<pk>\d+)/$',views.YoukeVulListDetailView.as_view()),

    re_path('^api/qiboVulList/$',views.QiboVulListView.as_view()),
    re_path('^api/qiboVulList/(?P<pk>\d+)/$',views.QiboVulListDetailView.as_view()),

    re_path('^api/zhiboVulList/$', views.ZhiboVulListView.as_view()),
    re_path('^api/zhiboVulList/(?P<pk>\d+)/$', views.ZhiboVulListDetailView.as_view()),

    re_path('^api/myunVulList/$', views.MyunVulListView.as_view()),
    re_path('^api/myunVulList/(?P<pk>\d+)/$', views.MyunVulListDetailView.as_view()),

    re_path('^api/mdnVulList/$', views.MdnVulListView.as_view()),
    re_path('^api/mdnVulList/(?P<pk>\d+)/$', views.MdnVulListDetailView.as_view()),
    #mdc漏洞路由
    re_path('^api/mdcVulList/$', views.MdcVulListView.as_view()),
    re_path('^api/mdcVulList/(?P<pk>\d+)/$', views.MdcVulListDetailView.as_view()),
    #其他漏洞路由
    re_path('^api/otherVulList/$', views.OtherVulListView.as_view()),
    re_path('^api/otherVulList/(?P<pk>\d+)/$', views.OtherVulListDetailView.as_view()),
    #所有漏洞路由
    re_path('^api/totalVulList/$', views.TotalVulListView.as_view()),
    re_path('^api/totalVulList/(?P<pk>\d+)/$', views.TotalVulListDetailView.as_view()),

]
