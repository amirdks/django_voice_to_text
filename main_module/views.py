from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views import View

from main_module.forms import AudioForm


# Create your views here.
class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'main_module/home.html', context)

    def post(self, request: HttpRequest):
        print(request.POST)
        print("-----------")
        print(request.FILES)
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            new_audio = form.save()
            print(new_audio)
            return JsonResponse({"status": "success", "text": "متن تستی"})
        else:
            return JsonResponse({"status": "error"})
