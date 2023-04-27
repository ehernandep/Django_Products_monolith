from django.urls import path, include
from .views import ProductBackendEndAPIView, ProductFrontEndAPIView, LinkAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('products/frontend', ProductFrontEndAPIView.as_view()),
    path('products/backend', ProductBackendEndAPIView.as_view()),
    path('links', LinkAPIView.as_view())

]
