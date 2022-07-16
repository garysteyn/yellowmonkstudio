from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


@csrf_exempt
def lol(request):
    if request.method == 'GET':
        print("pancakes")

        json_object = {'key': "value"}
        return JsonResponse(json_object)

