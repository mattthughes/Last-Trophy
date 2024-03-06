from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic

# Create your views here.
def index(request):
    return render(
        request,
        "trophy_hunter/index.html"
    )
