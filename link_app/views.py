from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def main_site(request):
    print("Dane\n",request.body)
    return render(request,'link_app/main.html')