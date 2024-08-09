from django.shortcuts import render

# Create your views here.
def luiz(request):
    return render(request, "luiz.html")

def taina(request):
    return render(request, "taina.html")
