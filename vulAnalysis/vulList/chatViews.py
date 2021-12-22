from django.views import View
from django.http import JsonResponse
from vulList.models import Total_VulModel


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

