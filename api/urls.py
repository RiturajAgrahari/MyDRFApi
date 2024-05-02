from django.urls import path
from . import views

urlpatterns = [
    path("portfolio_contact_me/", views.portfolio_contact_me, name="portfolio_contact_me")
]