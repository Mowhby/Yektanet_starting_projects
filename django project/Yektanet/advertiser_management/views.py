from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import *
from .forms import NewForm


class viewAds(View):
    http_method_names = ['get']

    def get(self, request):
        ads = ad.objects.all()
        for a in ads:
            new_view = view(ad=a, user_ip=request.META.get('REMOTE_ADDR'))
            a.advertiser.views += 1
            new_view.save()
            a.advertiser.save()
        advertisers = advetiser.objects.all()
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
        new_click = click(ad=AD, user_ip=request.META.get('REMOTE_ADDR'))
        new_click.save()
        AD.advertiser.clicks+=1
        AD.advertiser.save()
        link = AD.link
        return redirect(link)
