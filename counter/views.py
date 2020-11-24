from django.shortcuts import render
from .serializers import LinksSerializer
from .models import Search
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from selenium import webdriver
from .pars_cnt import pars, webdriver, sleep, Keys


class LinksView(APIView):

    def get(self, request, by_number):
        links = Search.objects.get(id=by_number)
        context = {'request': links.link, 'region': links.region}
        return Response(context)

    def post(self, request):
        links = request.data.get('result')
        serializer = LinksSerializer(data=links)
        if serializer.is_valid(raise_exception=True):
            link_saved = serializer.save()
            my_requests = Search.objects.all().last()
            counter = pars(my_requests.link)
            sleep(10)
        return Response({'id': my_requests.id, 'request': my_requests.link, 'counter': counter})
