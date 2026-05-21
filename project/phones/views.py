from django.shortcuts import redirect, render
from django.views import generic
from django.http import JsonResponse
from .forms import PhoneCompareForm
from .models import Phone
import datetime


def health(request):
    return JsonResponse({
        "status": "ok",
        "service": "phone-store",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
    })


class PhoneListView(generic.ListView):
    model = Phone
    template_name = 'phone_list.html'


class PhoneDetailView(generic.DetailView):
    model = Phone
    template_name = 'phone_detail.html'


class PhoneCompareView(generic.View):
    def get(self, request):
        form = PhoneCompareForm()
        return render(request, 'phone_compare.html', context={'form': form})
    
    def post(self, request):
        form = PhoneCompareForm(request.POST)
        best_price = None
        best_screen_size = None
        best_camera = None
        best_storage = None

        if form.is_valid():
            phone_one = form.cleaned_data['phone_one']
            phone_two = form.cleaned_data['phone_two']

            if phone_one and phone_two:
                if phone_one.price != phone_two.price:
                    best_price = min(phone_one.price, phone_two.price)
                
                if phone_one.screen_size != phone_two.screen_size:
                    best_screen_size = max(phone_one.screen_size, phone_two.screen_size)

                if phone_one.camera_resolution != phone_two.camera_resolution:
                    best_camera = max(phone_one.camera_resolution, phone_two.camera_resolution)

                if phone_one.storage != phone_two.storage:
                    best_storage = max(phone_one.storage, phone_two.storage)

            return render(request, 'phone_compare.html', context={
                'form': form,
                'phone_one': phone_one,
                'phone_two': phone_two,
                'best_price': best_price,
                'best_camera': best_camera,
                'best_screen_size': best_screen_size,
                'best_storage': best_storage,
            })
