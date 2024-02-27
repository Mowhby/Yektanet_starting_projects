from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .forms import NewForm
from .serializer import AdvertiserSerializer, AdSerializer


class viewAds(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request):
        ads = ad.objects.all()
        views = [view(ad=ad, user_ip=request.META.get('REMOTE_ADDR')) for ad in ads]
        view.objects.bulk_create(views)

        advertisers = advetiser.objects.all()
        for adv in advertisers:
            adv.filtered_ads = adv.ad_set.filter(approve=True)

        context = {'advertisers': advertisers}
        return Response(context)


class New_form(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'form.html'

    def get(self, request):
        context = {'form': NewForm}
        return Response(context)

    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect("viewAds")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Redirect_view(APIView):

    def get(self, request, id: int):
        AD = ad.objects.get(id=id)
        click.objects.create(ad=AD, user_ip=request.META.get('REMOTE_ADDR'))
        redirect_url = AD.link
        return Response({"redirect_url": redirect_url}, status=status.HTTP_302_FOUND)


class Status_view(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id: int):
        AD = ad.objects.get(id=id)
        data_saver = []
        for i in range(24):
            str1 = f"{i}:00"
            str2 = f"{(i + 1) % 24}:00"
            clicks = click.objects.filter(created_on__time__range=[str1, str2], ad=AD)
            views = view.objects.filter(created_on__time__range=[str1, str2], ad=AD)
            if len(views) != 0:
                data_saver.append([i, len(clicks), len(views), len(clicks) / len(views)])
            else:
                data_saver.append([i, len(clicks), len(views), 0])
        data_saver.sort(key=lambda x: x[3], reverse=True)
        Response = f"<h2>{AD.title}</h2><dl>"
        for i in range(24):
            Response += "<dt>"
            Response += f"{data_saver[i][0]}:00 - {data_saver[i][0] + 1}:00"
            Response += "</dt><dd>"
            Response += f"clicks: {data_saver[i][1]} and views: {data_saver[i][2]} and rate click/view = {data_saver[i][3]}"
            Response += "</dd>"
        Response += "</dl>"

        clicks = click.objects.filter(ad=AD)
        sum = 0
        for c in clicks:
            views_same_ip = view.objects.filter(user_ip=c.user_ip, ad=AD)
            find_view = float('inf')
            for i in range(len(views_same_ip)):
                sec = (c.created_on - views_same_ip[i].created_on).total_seconds()
                if find_view > sec >= 0:
                    find_view = sec
            sum += find_view
        Response += f"<h2> average difference between each click and related view in seconds is {sum / len(clicks)}</h2>"
        return HttpResponse(Response)
