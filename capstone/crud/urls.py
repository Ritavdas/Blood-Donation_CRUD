from django.contrib import admin
from django.urls import path
from crud.views import IndexView, EmpView

urlpatterns = [
    path('', IndexView.as_view()),
    path('emp', EmpView.as_view(),)
]
