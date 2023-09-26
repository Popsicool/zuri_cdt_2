
from django.urls import path, include
from . import views

# urlpatterns = [
#   path("", views.Home.as_view(), name="home")
# ]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.Home, basename='user')
custom_urls = [
    path("signup",views.RegisterApi.as_view(),name="register",),
]

urlpatterns = [
    path('',include(router.urls)),
    path("", include(custom_urls)),
]
