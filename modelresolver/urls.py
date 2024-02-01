from django.urls import path

from . import views

urlpatterns = [
    path("testsol/<int:problem_id>/partialsol/", views.testPartialSolution, name="testPartialSolution"),
    path("solve/<int:problem_id>/solution", views.resolveProbleme, name="resolveProbleme"),
]