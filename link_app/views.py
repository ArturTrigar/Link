from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
@api_view
def main_site(request):
    print("Dane\n",request.body)
    return render(request,'link_app/main.html')