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
from vulList import views,chatViews
#
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^api/youkeVulList/$',views.YoukeVulListView.as_view()),
    re_path('^api/youkeVulList/(?P<pk>[a-zA-Z0-9]+)/$',views.YoukeVulListDetailView.as_view()),

    re_path('^api/qiboVulList/$',views.QiboVulListView.as_view()),
    re_path('^api/qiboVulList/(?P<pk>[a-zA-Z0-9]+)/$',views.QiboVulListDetailView.as_view()),

    re_path('^api/zhiboVulList/$', views.ZhiboVulListView.as_view()),
    re_path('^api/zhiboVulList/(?P<pk>[a-zA-Z0-9]+)/$', views.ZhiboVulListDetailView.as_view()),

    re_path('^api/myunVulList/$', views.MyunVulListView.as_view()),
    re_path('^api/myunVulList/(?P<pk>[a-zA-Z0-9]+)/$', views.MyunVulListDetailView.as_view()),

    re_path('^api/mdnVulList/$', views.MdnVulListView.as_view()),
    re_path('^api/mdnVulList/(?P<pk>[a-zA-Z0-9]+)/$', views.MdnVulListDetailView.as_view()),
    #mdc漏洞路由
    re_path('^api/mdcVulList/$', views.MdcVulListView.as_view()),
    re_path('^api/mdcVulList/(?P<pk>[a-zA-Z0-9]+)/$', views.MdcVulListDetailView.as_view()),
    #其他漏洞路由
    re_path('^api/otherVulList/$', views.OtherVulListView.as_view()),
    re_path('^api/otherVulList/(?P<pk>[a-zA-Z0-9]+)/$', views.OtherVulListDetailView.as_view()),
    #所有漏洞路由
    re_path('^api/totalVulList/$', views.TotalVulListView.as_view()),
    re_path('^api/totalVulList/(?P<pk>[a-zA-Z0-9]+)/$', views.TotalVulListDetailView.as_view()),

    #漏洞数量展示
    re_path('^api/charts/total/$', chatViews.TotalChartsView.as_view()),
    re_path('^api/charts/totalByItem/$', chatViews.TotalByItemChartsView.as_view()),
    re_path('^api/charts/totalByType/$', chatViews.TotalByTypeChartsView.as_view()),
    re_path('^api/charts/totalByTimeRise/$', chatViews.TotalByTimeRiseChartsView.as_view()),
    re_path('^api/charts/totalByTimeFix/$', chatViews.TotalByTimeFixChartsView.as_view()),

    #添加数据接口
    re_path('^api/totalVulsRise/$', chatViews.TotalVulsRiseView.as_view()),
    re_path('^api/totalVulsFix/$', chatViews.TotalVulsFixView.as_view()),

]
