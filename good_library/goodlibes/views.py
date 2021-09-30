from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Author, Book


def not_found_404(request, exception):
    data = {"err": exception}
    return render(request, "404.html", data)


def server_error_500(request):
    return render(request, "500.html")


def home(request):
    data = {"books": Book.objects.all()}
    return render(request, "home.html", data)


def about(request):
    return render(request, "about.html")


@login_required
def create(request):
    if request.method == "POST":
        dog = NewBookForm(request.POST)
        if dog.is_valid():
            dog_id = dog.save().id
            return redirect("dog-show", dog_id=dog_id)
    else:
        form = NewBookForm()
    data = {"form": form}
    return render(request, "dogs/new.html", data)
