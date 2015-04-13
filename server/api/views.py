from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
from .models import USER,Status
from .serializers import UserSerializer,StatusSerializer


@csrf_exempt
def status_list(request,pk):
    if request.method == 'GET':
        status = Status.objects.filter(user=pk)
        serializer = StatusSerializer(status, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StatusSerializer(data=data, safe=False)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400,safe=False)

@csrf_exempt
def status_detail(request,pk):
    try:
        status = Status.objects.get(pk=pk)
    except Status.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = StatusSerializer(status)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StatusSerializer(status,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        status.delete()
        return HttpResponse(status=204)

# Create your views here.


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        user = USER.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data, safe=False)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400,safe=False)

@csrf_exempt
def user_detail(request,pk):
    try:
        user = USER.objects.get(pk=pk)
    except Status.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)