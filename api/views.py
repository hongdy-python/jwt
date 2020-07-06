from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.authentication import JWTauthentication
from api.serializers import UserModelSerializer
from utils.response import APIResponse


class UserDetailAPIView(APIView):
    # 登录访问
    permission_classes = [IsAuthenticated]
    # 使用自定义的校验规则
    authentication_classes = [JWTauthentication]

    # 默认规则
    # authentication_classes = [JSONWebTokenAuthentication]
    def get(self, request, *args, **kwargs):
        return APIResponse(results={"username": request.user.username})


class Loginapiview(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user_ser = UserModelSerializer(data=request.data)
        user_ser.is_valid(raise_exception=True)

        return APIResponse(data_message="ok", token=user_ser.token, results=UserModelSerializer(user_ser.obj).data)
