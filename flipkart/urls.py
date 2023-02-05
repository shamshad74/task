from django.urls import path
from . import views

app_name='flipkart'

urlpatterns = [
    path("scrape/<str:url>/", views.scrape_product, name="scrape_product"),
    path("", views.IndexView.as_view(), name="index"),
    path("fetch/", views.fetch_product, name="fetch_product"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
