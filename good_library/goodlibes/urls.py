from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="goodlibes-home"),
    path("about/", views.about, name="goodlibes-about"),
    # path("books/new/", views.create, name="book-create"),
    # path("book/<int:book_id>/", views.show, name="book-show"),
]
