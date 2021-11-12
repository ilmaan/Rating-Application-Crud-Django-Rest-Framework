
# import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# import requests
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView



class feedback_api(APIView):
    def get(self, request,pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        if id is not None:
            fb = Feedback.objects.get(id=id)
            serializer = FeedbackSerializer(fb)
            return Response(serializer.data)

        fb = Feedback.objects.all()
        serializer = FeedbackSerializer(fb, many=True)
        return Response(serializer.data)

    def post(self,request,pk=None, format=None):
        data = request.data
        serializer = FeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Added'})
        return Response(serializer.errors) 


    def put(self,request,pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        fb = Feedback.objects.get(pk=id)
        data = request.data
        serializer = FeedbackSerializer(fb,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Put Data Updated'})
        return Response(serializer.errors)

    
    def patch(self,request,pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        fb = Feedback.objects.get(pk=id)
        data = request.data
        serializer = FeedbackSerializer(fb,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Patch Data Updated'})
        return Response(serializer.errors)


    def delete(self,request,pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        fb = Feedback.objects.get(pk=id)
        fb.delete()
        return Response({'msg':'Data Deleeted'}) 


