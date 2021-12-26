import json
import time

from django.views import View
from django.http import JsonResponse
from vulList.models import Youke_VulModel,Qibo_VulModel,Zhibo_VulModel,Myun_VulModel,Mdn_VulModel,Mdc_VulModel,Other_VulModel,Total_VulModel
# Create your views here.
#有课视图
class YoukeVulListView(View):
    def get(self,request):
        try:
            vuls = Youke_VulModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        for vul in vuls:
            vul_dict = {
                "vul_id":vul.vul_id,
                "vul_name":vul.vul_name,
                "vul_jira":vul.vul_jira,
                "vul_sendto":vul.vul_sendto,
                "vul_fixer":vul.vul_fixer,
                "vul_sendtime":vul.vul_sendtime,
                "vul_estimatefixedtime":vul.vul_estimatefixedtime,
                "vul_fixedtime":vul.vul_fixedtime,
                "vul_isfixed":vul.vul_isfixed,
                "vul_type":vul.vul_type,
                "vul_remarks":vul.vul_remarks,
            }
            vuls_list.append(vul_dict)
        return JsonResponse({
            "success": "200",
            "data": vuls_list,
        })

    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = Youke_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed = vul_dict['vul_isfixed'],
                vul_type = vul_dict['vul_type'],
            )
            vul.save()

            vulTTL = Total_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vulTTL.save()
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        resDict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

class YoukeVulListDetailView(View):
    def get(self,request,pk):
        try:
            vul = Youke_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": vul_dict,
        })

    def put(self,request,pk):
        try:
            vul = Youke_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = json.loads(request.body.decode())
        vul.vul_id = vul_dict['vul_id']
        vul.vul_name = vul_dict['vul_name']
        vul.vul_jira = vul_dict['vul_jira']
        vul.vul_sendto = vul_dict['vul_sendto']
        vul.vul_fixer = vul_dict['vul_fixer']
        vul.vul_sendtime = vul_dict['vul_sendtime']
        vul.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vul.vul_fixedtime = vul_dict['vul_fixedtime']
        vul.vul_isfixed = vul_dict['vul_isfixed']
        vul.vul_type = vul_dict['vul_type']
        vul.vul_remarks = vul_dict['vul_remarks']
        vul.save()

        vulTTL.vul_id = vul_dict['vul_id']
        vulTTL.vul_name = vul_dict['vul_name']
        vulTTL.vul_jira = vul_dict['vul_jira']
        vulTTL.vul_sendto = vul_dict['vul_sendto']
        vulTTL.vul_fixer = vul_dict['vul_fixer']
        vulTTL.vul_sendtime = vul_dict['vul_sendtime']
        vulTTL.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vulTTL.vul_fixedtime = vul_dict['vul_fixedtime']
        vulTTL.vul_isfixed = vul_dict['vul_isfixed']
        vulTTL.vul_type = vul_dict['vul_type']
        vulTTL.vul_remarks = vul_dict['vul_remarks']
        vulTTL.save()

        res_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": res_dict,
        })

    def delete(self,request,pk):
        try:
            vul =Youke_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul.delete()
        vulTTL.delete()
        return JsonResponse({
            "success": "200",
            "data": "删除成功",
        })

#企播视图
class QiboVulListView(View):
    def get(self,request):
        try:
            vuls = Qibo_VulModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        for vul in vuls:
            vul_dict = {
                "vul_id":vul.vul_id,
                "vul_name":vul.vul_name,
                "vul_jira":vul.vul_jira,
                "vul_sendto":vul.vul_sendto,
                "vul_fixer":vul.vul_fixer,
                "vul_sendtime":vul.vul_sendtime,
                "vul_estimatefixedtime":vul.vul_estimatefixedtime,
                "vul_fixedtime":vul.vul_fixedtime,
                "vul_isfixed":vul.vul_isfixed,
                "vul_type":vul.vul_type,
                "vul_remarks":vul.vul_remarks,
            }
            vuls_list.append(vul_dict)
        return JsonResponse({
            "success": "200",
            "data": vuls_list,
        })

    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = Qibo_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vul.save()

            vulTTL = Total_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vulTTL.save()
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        resDict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

class QiboVulListDetailView(View):
    def get(self,request,pk):
        try:
            vul = Qibo_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": vul_dict,
        })

    def put(self,request,pk):
        try:
            vul = Qibo_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = json.loads(request.body.decode())
        vul.vul_id = vul_dict['vul_id']
        vul.vul_name = vul_dict['vul_name']
        vul.vul_jira = vul_dict['vul_jira']
        vul.vul_sendto = vul_dict['vul_sendto']
        vul.vul_fixer = vul_dict['vul_fixer']
        vul.vul_sendtime = vul_dict['vul_sendtime']
        vul.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vul.vul_fixedtime = vul_dict['vul_fixedtime']
        vul.vul_isfixed = vul_dict['vul_isfixed']
        vul.vul_type = vul_dict['vul_type']
        vul.vul_remarks = vul_dict['vul_remarks']
        vul.save()

        vulTTL.vul_id = vul_dict['vul_id']
        vulTTL.vul_name = vul_dict['vul_name']
        vulTTL.vul_jira = vul_dict['vul_jira']
        vulTTL.vul_sendto = vul_dict['vul_sendto']
        vulTTL.vul_fixer = vul_dict['vul_fixer']
        vulTTL.vul_sendtime = vul_dict['vul_sendtime']
        vulTTL.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vulTTL.vul_fixedtime = vul_dict['vul_fixedtime']
        vulTTL.vul_isfixed = vul_dict['vul_isfixed']
        vulTTL.vul_type = vul_dict['vul_type']
        vulTTL.vul_remarks = vul_dict['vul_remarks']
        vulTTL.save()

        res_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": res_dict,
        })

    def delete(self,request,pk):
        try:
            vul =Qibo_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul.delete()
        vulTTL.delete()
        return JsonResponse({
            "success": "200",
            "data": "删除成功",
        })

#直播视图
class ZhiboVulListView(View):
    def get(self,request):
        try:
            vuls = Zhibo_VulModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        for vul in vuls:
            vul_dict = {
                "vul_id": vul.vul_id,
                "vul_name": vul.vul_name,
                "vul_jira": vul.vul_jira,
                "vul_sendto": vul.vul_sendto,
                "vul_fixer": vul.vul_fixer,
                "vul_sendtime": vul.vul_sendtime,
                "vul_estimatefixedtime": vul.vul_estimatefixedtime,
                "vul_fixedtime": vul.vul_fixedtime,
                "vul_isfixed": vul.vul_isfixed,
                "vul_type": vul.vul_type,
                "vul_remarks": vul.vul_remarks,
            }
            vuls_list.append(vul_dict)
        return JsonResponse({
            "success": "200",
            "data": vuls_list,
        })

    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = Zhibo_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vul.save()
            vulTTL = Total_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],

            )
            vulTTL.save()
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        resDict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

class ZhiboVulListDetailView(View):
    def get(self,request,pk):
        try:
            vul = Zhibo_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": vul_dict,
        })

    def put(self,request,pk):
        try:
            vul = Zhibo_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = json.loads(request.body.decode())
        vul.vul_id = vul_dict['vul_id']
        vul.vul_name = vul_dict['vul_name']
        vul.vul_jira = vul_dict['vul_jira']
        vul.vul_sendto = vul_dict['vul_sendto']
        vul.vul_fixer = vul_dict['vul_fixer']
        vul.vul_sendtime = vul_dict['vul_sendtime']
        vul.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vul.vul_fixedtime = vul_dict['vul_fixedtime']
        vul.vul_isfixed = vul_dict['vul_isfixed']
        vul.vul_type = vul_dict['vul_type']
        vul.vul_remarks = vul_dict['vul_remarks']
        vul.save()

        vulTTL.vul_id = vul_dict['vul_id']
        vulTTL.vul_name = vul_dict['vul_name']
        vulTTL.vul_jira = vul_dict['vul_jira']
        vulTTL.vul_sendto = vul_dict['vul_sendto']
        vulTTL.vul_fixer = vul_dict['vul_fixer']
        vulTTL.vul_sendtime = vul_dict['vul_sendtime']
        vulTTL.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vulTTL.vul_fixedtime = vul_dict['vul_fixedtime']
        vulTTL.vul_isfixed = vul_dict['vul_isfixed']
        vulTTL.vul_type = vul_dict['vul_type']
        vulTTL.vul_remarks = vul_dict['vul_remarks']
        vulTTL.save()

        res_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": res_dict,
        })

    def delete(self,request,pk):
        try:
            vul =Zhibo_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul.delete()
        vulTTL.delete()
        return JsonResponse({
            "success": "200",
            "data": "删除成功",
        })

#目睹云视图
class MyunVulListView(View):
    def get(self,request):
        try:
            vuls = Myun_VulModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        for vul in vuls:
            vul_dict = {
                "vul_id": vul.vul_id,
                "vul_name": vul.vul_name,
                "vul_jira": vul.vul_jira,
                "vul_sendto": vul.vul_sendto,
                "vul_fixer": vul.vul_fixer,
                "vul_sendtime": vul.vul_sendtime,
                "vul_estimatefixedtime": vul.vul_estimatefixedtime,
                "vul_fixedtime": vul.vul_fixedtime,
                "vul_isfixed": vul.vul_isfixed,
                "vul_type": vul.vul_type,
                "vul_remarks": vul.vul_remarks,
            }
            vuls_list.append(vul_dict)
        return JsonResponse({
            "success": "200",
            "data": vuls_list,
        })

    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = Myun_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vul.save()
            vulTTL = Total_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vulTTL.save()
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        resDict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

class MyunVulListDetailView(View):
    def get(self,request,pk):
        try:
            vul = Myun_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": vul_dict,
        })

    def put(self,request,pk):
        try:
            vul = Myun_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = json.loads(request.body.decode())
        vul.vul_id = vul_dict['vul_id']
        vul.vul_name = vul_dict['vul_name']
        vul.vul_jira = vul_dict['vul_jira']
        vul.vul_sendto = vul_dict['vul_sendto']
        vul.vul_fixer = vul_dict['vul_fixer']
        vul.vul_sendtime = vul_dict['vul_sendtime']
        vul.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vul.vul_fixedtime = vul_dict['vul_fixedtime']
        vul.vul_isfixed = vul_dict['vul_isfixed']
        vul.vul_type = vul_dict['vul_type']
        vul.vul_remarks = vul_dict['vul_remarks']
        vul.save()

        vulTTL.vul_id = vul_dict['vul_id']
        vulTTL.vul_name = vul_dict['vul_name']
        vulTTL.vul_jira = vul_dict['vul_jira']
        vulTTL.vul_sendto = vul_dict['vul_sendto']
        vulTTL.vul_fixer = vul_dict['vul_fixer']
        vulTTL.vul_sendtime = vul_dict['vul_sendtime']
        vulTTL.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vulTTL.vul_fixedtime = vul_dict['vul_fixedtime']
        vulTTL.vul_isfixed = vul_dict['vul_isfixed']
        vulTTL.vul_type = vul_dict['vul_type']
        vulTTL.vul_remarks = vul_dict['vul_remarks']
        vulTTL.save()

        res_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": res_dict,
        })

    def delete(self,request,pk):
        try:
            vul =Myun_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul.delete()
        vulTTL.delete()
        return JsonResponse({
            "success": "200",
            "data": "删除成功",
        })

#mdn视图
class MdnVulListView(View):
    def get(self,request):
        try:
            vuls = Mdn_VulModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        for vul in vuls:
            vul_dict = {
                "vul_id": vul.vul_id,
                "vul_name": vul.vul_name,
                "vul_jira": vul.vul_jira,
                "vul_sendto": vul.vul_sendto,
                "vul_fixer": vul.vul_fixer,
                "vul_sendtime": vul.vul_sendtime,
                "vul_estimatefixedtime": vul.vul_estimatefixedtime,
                "vul_fixedtime": vul.vul_fixedtime,
                "vul_isfixed": vul.vul_isfixed,
                "vul_type": vul.vul_type,
                "vul_remarks": vul.vul_remarks,
            }
            vuls_list.append(vul_dict)
        return JsonResponse({
            "success": "200",
            "data": vuls_list,
        })

    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = Mdn_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vul.save()
            vulTTL = Total_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vulTTL.save()
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        resDict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

class MdnVulListDetailView(View):
    def get(self,request,pk):
        try:
            vul = Mdn_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": vul_dict,
        })

    def put(self,request,pk):
        try:
            vul = Mdn_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = json.loads(request.body.decode())
        vul.vul_id = vul_dict['vul_id']
        vul.vul_name = vul_dict['vul_name']
        vul.vul_jira = vul_dict['vul_jira']
        vul.vul_sendto = vul_dict['vul_sendto']
        vul.vul_fixer = vul_dict['vul_fixer']
        vul.vul_sendtime = vul_dict['vul_sendtime']
        vul.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vul.vul_fixedtime = vul_dict['vul_fixedtime']
        vul.vul_isfixed = vul_dict['vul_isfixed']
        vul.vul_type = vul_dict['vul_type']
        vul.vul_remarks = vul_dict['vul_remarks']
        vul.save()

        vulTTL.vul_id = vul_dict['vul_id']
        vulTTL.vul_name = vul_dict['vul_name']
        vulTTL.vul_jira = vul_dict['vul_jira']
        vulTTL.vul_sendto = vul_dict['vul_sendto']
        vulTTL.vul_fixer = vul_dict['vul_fixer']
        vulTTL.vul_sendtime = vul_dict['vul_sendtime']
        vulTTL.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vulTTL.vul_fixedtime = vul_dict['vul_fixedtime']
        vulTTL.vul_isfixed = vul_dict['vul_isfixed']
        vulTTL.vul_type = vul_dict['vul_type']
        vulTTL.vul_remarks = vul_dict['vul_remarks']
        vulTTL.save()

        res_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": res_dict,
        })

    def delete(self,request,pk):
        try:
            vul =Mdn_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul.delete()
        vulTTL.delete()
        return JsonResponse({
            "success": "200",
            "data": "删除成功",
        })

#mdc视图
class MdcVulListView(View):
    def get(self,request):
        try:
            vuls = Mdc_VulModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        for vul in vuls:
            vul_dict = {
                "vul_id":vul.vul_id,
                "vul_name":vul.vul_name,
                "vul_jira":vul.vul_jira,
                "vul_sendto":vul.vul_sendto,
                "vul_fixer":vul.vul_fixer,
                "vul_sendtime":vul.vul_sendtime,
                "vul_estimatefixedtime":vul.vul_estimatefixedtime,
                "vul_fixedtime":vul.vul_fixedtime,
                "vul_isfixed":vul.vul_isfixed,
                "vul_type":vul.vul_type,
                "vul_remarks":vul.vul_remarks,
            }
            vuls_list.append(vul_dict)
        return JsonResponse({
            "success": "200",
            "data": vuls_list,
        })

    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = Mdc_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vul.save()
            vulTTL = Total_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vulTTL.save()
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        resDict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

class MdcVulListDetailView(View):
    def get(self,request,pk):
        try:
            vul = Mdc_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": vul_dict,
        })

    def put(self,request,pk):
        try:
            vul = Mdc_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = json.loads(request.body.decode())
        vul.vul_id = vul_dict['vul_id']
        vul.vul_name = vul_dict['vul_name']
        vul.vul_jira = vul_dict['vul_jira']
        vul.vul_sendto = vul_dict['vul_sendto']
        vul.vul_fixer = vul_dict['vul_fixer']
        vul.vul_sendtime = vul_dict['vul_sendtime']
        vul.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vul.vul_fixedtime = vul_dict['vul_fixedtime']
        vul.vul_isfixed = vul_dict['vul_isfixed']
        vul.vul_type = vul_dict['vul_type']
        vul.vul_remarks = vul_dict['vul_remarks']
        vul.save()

        vulTTL.vul_id = vul_dict['vul_id']
        vulTTL.vul_name = vul_dict['vul_name']
        vulTTL.vul_jira = vul_dict['vul_jira']
        vulTTL.vul_sendto = vul_dict['vul_sendto']
        vulTTL.vul_fixer = vul_dict['vul_fixer']
        vulTTL.vul_sendtime = vul_dict['vul_sendtime']
        vulTTL.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vulTTL.vul_fixedtime = vul_dict['vul_fixedtime']
        vulTTL.vul_isfixed = vul_dict['vul_isfixed']
        vulTTL.vul_type = vul_dict['vul_type']
        vulTTL.vul_remarks = vul_dict['vul_remarks']
        vulTTL.save()

        res_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": res_dict,
        })

    def delete(self,request,pk):
        try:
            vul =Mdc_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul.delete()
        vulTTL.delete()
        return JsonResponse({
            "success": "200",
            "data": "删除成功",
        })

#其他视图
class OtherVulListView(View):
    def get(self,request):
        try:
            vuls = Other_VulModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        for vul in vuls:
            vul_dict = {
                "vul_id": vul.vul_id,
                "vul_name": vul.vul_name,
                "vul_jira": vul.vul_jira,
                "vul_sendto": vul.vul_sendto,
                "vul_fixer": vul.vul_fixer,
                "vul_sendtime": vul.vul_sendtime,
                "vul_estimatefixedtime": vul.vul_estimatefixedtime,
                "vul_fixedtime": vul.vul_fixedtime,
                "vul_isfixed": vul.vul_isfixed,
                "vul_type": vul.vul_type,
                "vul_remarks": vul.vul_remarks,
            }
            vuls_list.append(vul_dict)
        return JsonResponse({
            "success": "200",
            "data": vuls_list,
        })

    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = Other_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vul.save()
            vulTTL = Total_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vulTTL.save()
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        resDict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

class OtherVulListDetailView(View):
    def get(self,request,pk):
        try:
            vul = Other_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": vul_dict,
        })

    def put(self,request,pk):
        try:
            vul = Other_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = json.loads(request.body.decode())
        vul.vul_id = vul_dict['vul_id']
        vul.vul_name = vul_dict['vul_name']
        vul.vul_jira = vul_dict['vul_jira']
        vul.vul_sendto = vul_dict['vul_sendto']
        vul.vul_fixer = vul_dict['vul_fixer']
        vul.vul_sendtime = vul_dict['vul_sendtime']
        vul.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vul.vul_fixedtime = vul_dict['vul_fixedtime']
        vul.vul_isfixed = vul_dict['vul_isfixed']
        vul.vul_type = vul_dict['vul_type']
        vul.vul_remarks = vul_dict['vul_remarks']
        vul.save()

        vulTTL.vul_id = vul_dict['vul_id']
        vulTTL.vul_name = vul_dict['vul_name']
        vulTTL.vul_jira = vul_dict['vul_jira']
        vulTTL.vul_sendto = vul_dict['vul_sendto']
        vulTTL.vul_fixer = vul_dict['vul_fixer']
        vulTTL.vul_sendtime = vul_dict['vul_sendtime']
        vulTTL.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vulTTL.vul_fixedtime = vul_dict['vul_fixedtime']
        vulTTL.vul_isfixed = vul_dict['vul_isfixed']
        vulTTL.vul_type = vul_dict['vul_type']
        vulTTL.vul_remarks = vul_dict['vul_remarks']
        vulTTL.save()

        res_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": res_dict,
        })

    def delete(self,request,pk):
        try:
            vul =Other_VulModel.objects.get(vul_id=pk)
            vulTTL = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist or vulTTL.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul.delete()
        vulTTL.delete()
        return JsonResponse({
            "success": "200",
            "data": "删除成功",
        })

#所有漏洞列表视图
class TotalVulListView(View):
    def get(self,request):
        try:
            vuls = Total_VulModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        for vul in vuls:
            vul_dict = {
                "vul_id":vul.vul_id,
                "vul_name":vul.vul_name,
                "vul_jira":vul.vul_jira,
                "vul_sendto":vul.vul_sendto,
                "vul_fixer":vul.vul_fixer,
                "vul_sendtime":vul.vul_sendtime,
                "vul_estimatefixedtime":vul.vul_estimatefixedtime,
                "vul_fixedtime":vul.vul_fixedtime,
                "vul_isfixed":vul.vul_isfixed,
                "vul_type":vul.vul_type,
                "vul_remarks":vul.vul_remarks,
            }
            vuls_list.append(vul_dict)
        return JsonResponse({
            "success": "200",
            "data": vuls_list,
        })

    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = Total_VulModel(
                vul_id=vul_dict['vul_id'],
                vul_name=vul_dict['vul_name'],
                vul_jira=vul_dict['vul_jira'],
                vul_sendto=vul_dict['vul_sendto'],
                vul_fixer=vul_dict['vul_fixer'],
                vul_sendtime=vul_dict['vul_sendtime'],
                vul_estimatefixedtime=vul_dict['vul_estimatefixedtime'],
                vul_fixedtime=vul_dict['vul_fixedtime'],
                vul_isfixed=vul_dict['vul_isfixed'],
                vul_type=vul_dict['vul_type'],
            )
            vul.save()
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        resDict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

class TotalVulListDetailView(View):
    def get(self,request,pk):
        try:
            vul = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": vul_dict,
        })

    def put(self,request,pk):
        try:
            vul = Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul_dict = json.loads(request.body.decode())
        vul.vul_id = vul_dict['vul_id']
        vul.vul_name = vul_dict['vul_name']
        vul.vul_jira = vul_dict['vul_jira']
        vul.vul_sendto = vul_dict['vul_sendto']
        vul.vul_fixer = vul_dict['vul_fixer']
        vul.vul_sendtime = vul_dict['vul_sendtime']
        vul.vul_estimatefixedtime = vul_dict['vul_estimatefixedtime']
        vul.vul_fixedtime = vul_dict['vul_fixedtime']
        vul.vul_isfixed = vul_dict['vul_isfixed']
        vul.vul_type = vul_dict['vul_type']
        vul.vul_remarks = vul_dict['vul_remarks']
        vul.save()

        res_dict = {
            "vul_id": vul.vul_id,
            "vul_name": vul.vul_name,
            "vul_jira": vul.vul_jira,
            "vul_sendto": vul.vul_sendto,
            "vul_fixer": vul.vul_fixer,
            "vul_sendtime": vul.vul_sendtime,
            "vul_estimatefixedtime": vul.vul_estimatefixedtime,
            "vul_fixedtime": vul.vul_fixedtime,
            "vul_isfixed": vul.vul_isfixed,
            "vul_type": vul.vul_type,
            "vul_remarks": vul.vul_remarks,
        }
        return JsonResponse({
            "success": "200",
            "data": res_dict,
        })

    def delete(self,request,pk):
        try:
            vul =Total_VulModel.objects.get(vul_id=pk)
        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        vul.delete()
        return JsonResponse({
            "success": "200",
            "data": "删除成功",
        })

