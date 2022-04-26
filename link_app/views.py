from django.shortcuts import render

# Create your views here.
def main_site(request):
    print("Dane\n",request.body)
    return render(request,'link_app/main.html')