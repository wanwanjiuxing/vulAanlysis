import json

import data as data
from django.views import View
from django.http import JsonResponse
from vulList.models import Youke_VulModel,Qibo_VulModel,Zhibo_VulModel,Myun_VulModel,Mdn_VulModel,Mdc_VulModel,Other_VulModel,Total_VulModel,Total_vulsRiseModel,Total_vulsFixModel



class TotalChartsView(View):
    def get(self,request):
        try:
            vuls = Total_VulModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        fixedAmount = 0
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
            if vul.vul_isfixed == 1:
                fixedAmount += 1

        vulsAmount = len(vuls_list)
        fixingAmount = vulsAmount - fixedAmount
        fixedRate = '{:.2f}%'.format(fixedAmount / vulsAmount * 100)
        return JsonResponse({
            "success": "200",
            "data": {
                "vulsAmount":vulsAmount,
                "fixedAmount":fixedAmount,
                "fixingAmount":fixingAmount,
                "fixedRate":fixedRate,
            },
        })

class TotalByItemChartsView(View):
    def get(self,request):
        try:
            youkeVuls = Youke_VulModel.objects.all()
            zhiboVuls = Zhibo_VulModel.objects.all()
            qiboVuls = Qibo_VulModel.objects.all()
            myunVuls = Myun_VulModel.objects.all()
            mdnVuls = Mdn_VulModel.objects.all()
            mdcVuls = Mdc_VulModel.objects.all()
            otherVuls = Other_VulModel.objects.all()
        except youkeVuls.DoesNotExist or zhiboVuls.DoesNotExist or qiboVuls.DoesNotExist or myunVuls.DoesNotExist or mdnVuls.DoesNotExist or mdcVuls.DoesNotExist or otherVuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        youkeFixedAmount = 0
        zhiboFixedAmount = 0
        qiboFixedAmount = 0
        myunFixedAmount = 0
        mdnFixedAmount = 0
        mdcFixedAmount = 0
        otherFixedAmount = 0

        print(len(youkeVuls))
        for vuls in [youkeVuls,zhiboVuls,qiboVuls,myunVuls,mdnVuls,mdcVuls,otherVuls]:
            for vul in vuls:
                if 'youke' in vul.vul_id:
                    if vul.vul_isfixed == 1:
                        youkeFixedAmount += 1
                if 'zhibo' in vul.vul_id:
                    if vul.vul_isfixed == 1:
                        zhiboFixedAmount += 1
                if 'qibo' in vul.vul_id:
                    if vul.vul_isfixed == 1:
                        qiboFixedAmount += 1
                if 'myun' in vul.vul_id:
                    if vul.vul_isfixed == 1:
                        myunFixedAmount += 1
                if 'mdn' in vul.vul_id:
                    if vul.vul_isfixed == 1:
                        mdnFixedAmount += 1
                if 'mdc' in vul.vul_id:
                    if vul.vul_isfixed == 1:
                        mdcFixedAmount += 1
                if 'other' in vul.vul_id:
                    if vul.vul_isfixed == 1:
                        otherFixedAmount += 1
        resList = [
            {
                "item":"有课",
                "fixedAmount":youkeFixedAmount,
                "fixingAmount":len(youkeVuls) - youkeFixedAmount,
                "fixedRate":round(youkeFixedAmount / len(youkeVuls) * 100),
            },
            {
                "item": "直播",
                "fixedAmount": zhiboFixedAmount,
                "fixingAmount": len(zhiboVuls) - zhiboFixedAmount,
                "fixedRate":round(zhiboFixedAmount / len(zhiboVuls) * 100),
            },
            {
                "item": "企播",
                "fixedAmount": qiboFixedAmount,
                "fixingAmount": len(qiboVuls) - qiboFixedAmount,
                "fixedRate":round(qiboFixedAmount / len(qiboVuls) * 100),
            },
            {
                "item": "目睹云",
                "fixedAmount": myunFixedAmount,
                "fixingAmount": len(myunVuls) - myunFixedAmount,
                "fixedRate":round(myunFixedAmount / len(myunVuls) * 100),
            },
            {
                "item": "虚拟化活动",
                "fixedAmount": mdnFixedAmount,
                "fixingAmount": len(mdnVuls) - mdnFixedAmount,
                "fixedRate":round(mdnFixedAmount / len(mdnVuls) * 100),
            },
            {
                "item": "新目睹云",
                "fixedAmount": mdcFixedAmount,
                "fixingAmount": len(mdcVuls) - mdcFixedAmount,
                "fixedRate":round(mdcFixedAmount / len(mdcVuls) * 100),
            },
            {
                "item": "其他",
                "fixedAmount": otherFixedAmount,
                "fixingAmount": len(otherVuls) - otherFixedAmount,
                "fixedRate":round(otherFixedAmount / len(otherVuls) * 100),
            },
        ]

        return JsonResponse({
            "success": "200",
            "data": resList,
        })

class TotalByTypeChartsView(View):
    def get(self,request):
        try:
            totalVuls = Total_VulModel.objects.all()
        except totalVuls.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未找到",
            })
        type1 = 0
        type2 = 0
        type3 = 0
        type4 = 0
        type5 = 0
        type6 = 0
        type7 = 0
        type8 = 0
        type9 = 0
        for vuls in totalVuls:
            print(vuls.vul_type)
            if vuls.vul_type == 1:
                type1 += 1
            elif vuls.vul_type == 2:
                type2 += 1
            elif vuls.vul_type == 3:
                type3 += 1
            elif vuls.vul_type == 4:
                type4 += 1
            elif vuls.vul_type == 5:
                type5 += 1
            elif vuls.vul_type == 6:
                type6 += 1
            elif vuls.vul_type == 7:
                type7 += 1
            elif vuls.vul_type == 8:
                type8 += 1
            else:
                type9 += 1

        return JsonResponse({
            "success": "200",
            "data":[
                {
                    "item":"输入输出",
                    "amount":type1,
                },
                {
                    "item": "用户权限",
                    "amount": type2,
                },
                {
                    "item": "第三方组件",
                    "amount": type3,
                },
                {
                    "item": "安全配置",
                    "amount": type4,
                },
                {
                    "item": "文件上传下载",
                    "amount": type5,
                },
                {
                    "item": "命令执行&代码执行",
                    "amount": type6,
                },
                {
                    "item": "业务逻辑",
                    "amount": type7,
                },
                {
                    "item": "弱口令",
                    "amount": type8,
                },
                {
                    "item": "其他",
                    "amount": type9,
                },
            ]
        })

class TotalByTimeRiseChartsView(View):
    def get(self,request):
        try:
            vuls = Total_vulsRiseModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        for vul in vuls:
            vul_dict = {
                "data_id": vul.data_id,
                "vuls_amount": vul.vuls_amount,
            }
            vuls_list.append(vul_dict)

        return JsonResponse({
            "success": "200",
            "data": vuls_list,
        })

class TotalByTimeFixChartsView(View):
    def get(self,request):
        try:
            vuls = Total_vulsFixModel.objects.all()
        except vuls.DoesNotExist:
            return JsonResponse({
                "success":"404",
                "data":"未查询到内容",
            })
        vuls_list = []
        vuls2_list = []
        # for vul in vuls:
        #     vul_dict = {
        #         "data_id": vul.data_id,
        #         "fixed_amount": vul.fixed_amount,
        #         "fixing_amount": vul.fixing_amount,
        #         "fixing_rate":round(vul.fixing_amount / (vul.fixed_amount + vul.fixing_amount) * 100),
        #     }
        #     vuls_list.append(vul_dict)
        for vul in vuls:
            vul_dict = {
                "item":vul.data_id,
                "value":vul.fixing_amount,
                "type":"未整改漏洞",
            }
            vuls_list.append(vul_dict)
        for vul in vuls:
            vul_dict = {
                "item":vul.data_id,
                "value":vul.fixed_amount,
                "type":"已整改漏洞",
            }
            vuls_list.append(vul_dict)
        for vul in vuls:
            vul_dict = {
                "item":vul.data_id,
                "rate":round(vul.fixing_amount / (vul.fixed_amount + vul.fixing_amount) * 100),
            }
            vuls2_list.append(vul_dict)

        return JsonResponse({
            "success": "200",
            "data": {
                "data1":vuls_list,
                "data2":vuls2_list,
            }
        })

#   添加目睹漏洞增长数据接口
class TotalVulsRiseView(View):
    def post(self,request):
        data_bytes = request.body
        data_str = data_bytes.decode()
        data_dict = json.loads(data_str)

        try:
            data = Total_vulsRiseModel(
                data_id = data_dict['data_id'],
                vuls_amount = data_dict['vuls_amount'],
            )
            data.save()

        except data.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "添加失败",
            })
        resDict = {
            "data_id":data.data_id,
            "vuls_amount":data.vuls_amount,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

#  添加目睹漏洞修复趋势图数据接口
class TotalVulsFixView(View):
    def post(self,request):
        data_bytes = request.body
        data_str = data_bytes.decode()
        data_dict = json.loads(data_str)

        try:
            data = Total_vulsFixModel(
                data_id = data_dict['data_id'],
                fixed_amount = data_dict['fixed_amount'],
                fixing_amount = data_dict['fixing_amount'],
            )
            data.save()

        except data.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "添加失败",
            })
        resDict = {
            "data_id":data.data_id,
            "fixed_amount":data.fixed_amount,
            "fixing_amount": data.fixing_amount,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })



