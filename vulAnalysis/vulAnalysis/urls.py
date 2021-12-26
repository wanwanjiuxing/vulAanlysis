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
    # 漏洞数量展示by项目--输入输出
    re_path('^api/charts/totalByTimeType1Rise/$', chatViews.TotalByTimeRiseType1ChartsView.as_view()),
    # 漏洞数量展示by项目--用户权限
    re_path('^api/charts/totalByTimeType2Rise/$', chatViews.TotalByTimeRiseType2ChartsView.as_view()),
    # 漏洞数量展示by项目--第三方组件
    re_path('^api/charts/totalByTimeType3Rise/$', chatViews.TotalByTimeRiseType3ChartsView.as_view()),
    # 漏洞数量展示by项目--安全配置
    re_path('^api/charts/totalByTimeType4Rise/$', chatViews.TotalByTimeRiseType4ChartsView.as_view()),
    # 漏洞数量展示by项目--文件上传下载
    re_path('^api/charts/totalByTimeType5Rise/$', chatViews.TotalByTimeRiseType5ChartsView.as_view()),
    # 漏洞数量展示by项目--命令执行&代码执行
    re_path('^api/charts/totalByTimeType6Rise/$', chatViews.TotalByTimeRiseType6ChartsView.as_view()),
    # 漏洞数量展示by项目--业务逻辑
    re_path('^api/charts/totalByTimeType7Rise/$', chatViews.TotalByTimeRiseType7ChartsView.as_view()),
    # 漏洞数量展示by项目--弱口令
    re_path('^api/charts/totalByTimeType8Rise/$', chatViews.TotalByTimeRiseType8ChartsView.as_view()),
    # 漏洞数量展示by项目--其他
    re_path('^api/charts/totalByTimeType9Rise/$', chatViews.TotalByTimeRiseType9ChartsView.as_view()),

    # 漏洞修复趋势by项目--有课
    re_path('^api/charts/totalByTimeFixItem1/$', chatViews.TotalByTimeFixItem1ChartsView.as_view()),
    # 漏洞修复趋势by项目--有课
    re_path('^api/charts/totalByTimeFixItem2/$', chatViews.TotalByTimeFixItem2ChartsView.as_view()),
    # 漏洞修复趋势by项目--有课
    re_path('^api/charts/totalByTimeFixItem3/$', chatViews.TotalByTimeFixItem3ChartsView.as_view()),
    # 漏洞修复趋势by项目--有课
    re_path('^api/charts/totalByTimeFixItem4/$', chatViews.TotalByTimeFixItem4ChartsView.as_view()),
    # 漏洞修复趋势by项目--有课
    re_path('^api/charts/totalByTimeFixItem5/$', chatViews.TotalByTimeFixItem5ChartsView.as_view()),
    # 漏洞修复趋势by项目--有课
    re_path('^api/charts/totalByTimeFixItem6/$', chatViews.TotalByTimeFixItem6ChartsView.as_view()),
    # 漏洞修复趋势by项目--有课
    re_path('^api/charts/totalByTimeFixItem7/$', chatViews.TotalByTimeFixItem7ChartsView.as_view()),
    # 漏洞修复趋势by项目--有课
    re_path('^api/charts/totalByTimeFixItem8/$', chatViews.TotalByTimeFixItem8ChartsView.as_view()),

    #添加数据接口
    re_path('^api/totalVulsRise/$', chatViews.TotalVulsRiseView.as_view()),
    re_path('^api/totalVulsFix/$', chatViews.TotalVulsFixView.as_view()),
    re_path('^api/totalVulsType1Rise/$', chatViews.TotalVulsRiseType1View.as_view()),
    re_path('^api/totalVulsType2Rise/$', chatViews.TotalVulsRiseType2View.as_view()),
    re_path('^api/totalVulsType3Rise/$', chatViews.TotalVulsRiseType3View.as_view()),
    re_path('^api/totalVulsType4Rise/$', chatViews.TotalVulsRiseType4View.as_view()),
    re_path('^api/totalVulsType5Rise/$', chatViews.TotalVulsRiseType5View.as_view()),
    re_path('^api/totalVulsType6Rise/$', chatViews.TotalVulsRiseType6View.as_view()),
    re_path('^api/totalVulsType7Rise/$', chatViews.TotalVulsRiseType7View.as_view()),
    re_path('^api/totalVulsType8Rise/$', chatViews.TotalVulsRiseType8View.as_view()),
    re_path('^api/totalVulsType9Rise/$', chatViews.TotalVulsRiseType9View.as_view()),
    #添加数据接口--修复趋势--by项目--有课
    re_path('^api/totalVulsFixItem1/$', chatViews.TotalVulsFixItem1View.as_view()),
    # 添加数据接口--修复趋势--by项目--官网
    re_path('^api/totalVulsFixItem2/$', chatViews.TotalVulsFixItem2View.as_view()),
    # 添加数据接口--修复趋势--by项目--企播
    re_path('^api/totalVulsFixItem3/$', chatViews.TotalVulsFixItem3View.as_view()),
    # 添加数据接口--修复趋势--by项目--直播
    re_path('^api/totalVulsFixItem4/$', chatViews.TotalVulsFixItem4View.as_view()),
    # 添加数据接口--修复趋势--by项目--目睹云
    re_path('^api/totalVulsFixItem5/$', chatViews.TotalVulsFixItem5View.as_view()),
    # 添加数据接口--修复趋势--by项目--MDN
    re_path('^api/totalVulsFixItem6/$', chatViews.TotalVulsFixItem6View.as_view()),
    # 添加数据接口--修复趋势--by项目--MDC
    re_path('^api/totalVulsFixItem7/$', chatViews.TotalVulsFixItem7View.as_view()),
    # 添加数据接口--修复趋势--by项目--互联网
    re_path('^api/totalVulsFixItem8/$', chatViews.TotalVulsFixItem8View.as_view()),

]
