from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.authentication import JWTauthentication
from api.filter import LimitFilter, ComputerFilterSet
from api.models import Computer
from api.pagination import MyPageNumberPagination, MyLimitPagination
from api.serializers import UserModelSerializer, ComputerModelSerializer
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


class ComputerList(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer
    #通过此参数配置过滤的器类
    filter_backends = [SearchFilter,OrderingFilter, LimitFilter, DjangoFilterBackend]
    #指定当前搜索条件  （search=...）
    search_fields = ['name','price']
    #排序的条件   (ordering=...)
    # ordering = ['price']

    #指定使用的分页器
    # pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitPagination

    #精准匹配
    # filter_class = ComputerFilterSet
