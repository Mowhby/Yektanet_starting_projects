from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import *
from .forms import NewForm


class viewAds(View):
    http_method_names = ['get']

    def get(self, request):
        ads = ad.objects.all()
        views = []
        for a in ads:
            views.append(view(ad=a, user_ip=request.META.get('REMOTE_ADDR')))
        view.objects.bulk_create(views)
        advertisers = advetiser.objects.all()
        for adv in advertisers:
            adv.filtered_ads = adv.ad_set.filter(approve=True)
        context = {'advertisers': advertisers}
        return render(request, "index.html", context=context)


def new_form(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("viewAds")
        else:
            return redirect("new_form")
    else:
        context = {}
        context['form'] = NewForm
        return render(request, "form.html", context=context)


class Redirect_view(View):
    http_method_names = ['get']

    def get(self, request, id: int):
        AD = ad.objects.get(id=id)
        click.objects.create(ad=AD, user_ip=request.META.get('REMOTE_ADDR'))
        link = AD.link
        return redirect(link)


class Status_view(View):
    http_method_names = ['get']

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
        views_same_ip = []
        for c in clicks:
            views_same_ip = view.objects.filter(user_ip=c.user_ip, ad=AD)
            find_view = float('inf')
            for i in range(len(views_same_ip)):
                sec = (c.created_on - views_same_ip[i].created_on).total_seconds()
                if find_view > sec >= 0:
                    find_view = sec
            sum += find_view
        Response += f"<h2> average difference between each click and related view in seconds is {sum / len(clicks)}</h2><dl>"
        return HttpResponse(Response)
