from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_db>', views.listing, name='listing'),
    path('seach', views.search, name='search'),
]
