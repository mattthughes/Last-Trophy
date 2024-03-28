from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic

# Create your views here.
def index(request):
    return render(
        request,
        "trophy_hunter/index.html"
    )

def error_400(request,  exception):
        data = {}
        return render(request,'trophy_hunter/403_csrf.html', data)


def error_403(request, exception):
        data = {}
        return render(request,'trophy_hunter/403_csrf.html', data)


def error_404(request,  exception):
        data = {}
        return render(request,'trophy_hunter/403_csrf.html', data)





