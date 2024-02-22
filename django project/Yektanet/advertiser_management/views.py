from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .models import *
from .forms import NewForm


# create a function
def viewAds(request):
    ads = ad.objects.all()
    for a in ads:
        a.views += 1
        a.advertiser.views +=1
        a.save()
        a.advertiser.save()
    advertisers = advetiser.objects.all()
    context = {
        'advertisers': advertisers
    }
    return render(request, "index.html", context=context)


def new_form(request):
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("viewAds")
        else:

            # uncomment the below line to see errors
            # in the form (if any)
            # print(form.errors)
            return redirect("new_form")
    else:
        context = {}
        context['form'] = NewForm
        return render(request, "form.html", context=context)


class Redirect_view(View):
    http_method_names = ['get']

    def get(self, request, id: int):
        ads = ad.objects.all()
        for a in ads:
            if a.id == int(id):
                a.clicks += 1
                a.advertiser.clicks +=1
                a.save()
                a.advertiser.save()
                link = a.link
                break
        return redirect(link)
