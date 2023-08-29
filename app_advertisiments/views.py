from .models import Advertisiment
from django.shortcuts import render, redirect, reverse
from prog.урок8.advertisiments.app_auth.forms import AdvertisementForm

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
@login_required(login_url=reverse_lazy("login"))


def index(request):
    advertisements = Advertisiment.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "app_advertisiments/index.html", context)
def top_sellers(request):
    advertisements = Advertisiment.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "app_advertisiments/top-sellers.html", context)

def advertisiment_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisiment(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            return redirect(reverse("main-page"))
    form = AdvertisementForm()
    context = {"form": form}
    return render(request, "app_advertisiments/advertisement-post.html", context)
