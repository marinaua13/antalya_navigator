from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Author, Offer, Service


def index(request: HttpRequest) -> HttpResponse:

    num_authors = Author.objects.count()
    num_offers = Offer.objects.count()
    num_services = Service.objects.count()

    context = {
        "num_authors": num_authors,
        "num_offers": num_offers,
        "num_services": num_services,
    }
    return render(request, "catalog/index.html", context=context)
