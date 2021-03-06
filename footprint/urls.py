from django.urls import path
from . import views
from .views import PostDetailView, PostCreateView

urlpatterns = [
    path('', PostCreateView.as_view(), name="footprint-home"),
    path('submission/<int:pk>/', PostDetailView.as_view(), name="footprint-detail"),
]
