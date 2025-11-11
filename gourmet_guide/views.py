from django.shortcuts import render
from django.views import generic
from .models import Category, Shop
from django.urls import reverse_lazy

import requests
import urllib


class IndexView(generic.ListView):
    model = Shop


class DetailView(generic.DetailView):
    model = Shop
    template_name = "gourmet_guide/wonderful_shop_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        shop_instance = self.get_object()
        print("shop_instance:", shop_instance)
        address = shop_instance.address
        print("address:", address)

        makeUrl = "https://msearch.gsi.go.jp/address-search/AddressSearch?q="
        s_quote = urllib.parse.quote(address)
        print("s_quote:", s_quote)

        response = requests.get(makeUrl + s_quote)
        print("response:", response)
        print("response_text:", response.text)

        coordinates = response.json()[0]["geometry"]["coordinates"]
        print("coordinates:", coordinates)

        reversed_coordinates = reversed(coordinates)
        context["coordinates"] = ",".join(map(str, reversed_coordinates))
        print('context["coordinates"]:', context["coordinates"])
        return context

class CreateView(generic.edit.CreateView):
    model = Shop
    fields = "__all__"


class UpdateView(generic.edit.UpdateView):
    model = Shop
    fields = "__all__"

class DeleteView(generic.edit.DeleteView):
    model = Shop
    success_url = reverse_lazy("gourmet_guide:index")