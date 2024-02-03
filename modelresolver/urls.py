from django.urls import path

from . import views

urlpatterns = [
    path("testsol/<int:problem_id>/<str:partialsol>", views.testPartialSolution, name="testPartialSolution"),
    path("solve/<int:problem_id>/<str:user_solution>", views.resolveProbleme, name="resolveProbleme"),
]