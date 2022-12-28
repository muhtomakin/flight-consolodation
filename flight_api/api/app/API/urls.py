from django.urls import path
from app.API import views

urlpatterns = [
    path('detail/<cities>/<date>', views.data_list),
    path('cities/', views.data_cities)
]
