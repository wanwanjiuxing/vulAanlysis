import json
from django.conf import settings
import jwt
from django.views import View
from django.http import JsonResponse
from vulList.loginModels import User_Model

class LoginsView(View):
    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)
        try:
            vuls = User_Model.objects.get(username=vul_dict['username'])
            if vuls.password == vul_dict['password']:
                return JsonResponse({
                    "success": "200",
                    "data": {
                      "username":vuls.username,
                      "access":vuls.token,
                    },
                })
            else:
                return JsonResponse({
                    "success": "403",
                    "data": "登录失败",
                })
        except:
            return JsonResponse({
                "success":"403",
                "data":"登录失败",
            })


    def put(self, request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = User_Model(
                username=vul_dict['username'],
                fullname=vul_dict['fullname'],
                phonenumber=vul_dict['phonenumber'],
                password=vul_dict['password'],
            )
            vul.save()
            resDict = {
                "username": vul.username,
                "fullname": vul.fullname,
                "phonenumber": vul.phonenumber,
                "token": User_Model.objects.get(username=vul_dict['username']).token,
            }
            return JsonResponse({
                "success": "200",
                "data": resDict,
            })

        except:
            return JsonResponse({
                "success": "403",
                "data": "创建用户失败",
            })



class UserView(View):

    def post(self, request):
        try:
            user = jwt.decode(request.META['HTTP_TOKEN'],settings.SECRET_KEY,algorithms=['HS256'])['data']['username']
        except:
            return JsonResponse({
                "success": "403",
                "data": "登录失败",
            })
        if user == 'test9':
            vul_bytes = request.body
            vul_str = vul_bytes.decode()
            vul_dict = json.loads(vul_str)
            try:
                vuls = User_Model.objects.get(username=vul_dict['username'])
                if vuls.password == vul_dict['password']:
                    return JsonResponse({
                        "success": "200",
                        "data": vuls.token,
                    })
                else:
                    return JsonResponse({
                        "success": "403",
                        "data": "登录失败",
                    })
            except vuls.DoesNotExist:
                return JsonResponse({
                    "success": "404",
                    "data": "未查询到内容",
                })
        else:
            return JsonResponse({
                        "success": "403",
                        "data": "无权访问",
                    })