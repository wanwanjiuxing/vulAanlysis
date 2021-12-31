import json
from django.conf import settings
import jwt
from django.views import View
from django.http import JsonResponse
from vulList.testsModels import User

class LoginsView(View):
    def post(self,request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)
        try:
            vuls = User.objects.get(username=vul_dict['username'])
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
                "success":"404",
                "data":"未查询到内容",
            })


    def put(self, request):
        vul_bytes = request.body
        vul_str = vul_bytes.decode()
        vul_dict = json.loads(vul_str)

        try:
            vul = User(
                username=vul_dict['username'],
                fullname=vul_dict['fullname'],
                phonenumber=vul_dict['phonenumber'],
                password=vul_dict['password'],
            )
            vul.save()

        except vul.DoesNotExist:
            return JsonResponse({
                "success": "404",
                "data": "未查询到内容",
            })
        resDict = {
            "username": vul.username,
            "fullname": vul.fullname,
            "phonenumber": vul.phonenumber,
            "token": User.objects.get(username=vul_dict['username']).token,
        }
        return JsonResponse({
            "success": "200",
            "data": resDict,
        })

def user(request):
    if request.method == 'GET':
        _jsondata = {
            "user": "ops-coffee",
            "site": "https://ops-coffee.cn"
        }

        return JsonResponse({"state": 1, "message": _jsondata})
    else:
        return JsonResponse({"state": 0, "message": "Request method 'POST' not supported"})

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
                vuls = User.objects.get(username=vul_dict['username'])
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

    def get(self,request):
        return JsonResponse({
            "success": "200",
            "data": {
                "username":"test",
                "access":"12323",
            },
        })