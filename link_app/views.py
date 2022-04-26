from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@ensure_csrf_cookie
def main_site(request):
    print("Dane\n",request.body)
    return render(request,'link_app/main.html')