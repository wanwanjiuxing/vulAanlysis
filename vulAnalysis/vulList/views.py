import json
import time

from django.views import View
from django.http import JsonResponse
from vulList.models import Youke_VulModel
# Create your views here.

class VulListView(View):
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

class VulListDetailView(View):
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
            vul =Youke_VulModel.objects.get(vul_id=pk)
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

