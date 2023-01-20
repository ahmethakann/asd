from django.urls import path
from haberler.api import views as api_views


urlpatterns = [
    path('yazarlar/', api_views.GazeteciListCreateAPIView.as_view() , name='yazar-listesi' ),
    path('makaleler/', api_views.MakaleListCreateAPIView.as_view() , name='makale-listesi' ),
    path('makaleler/<int:pk>/', api_views.MakaleDetailAPIView.as_view() , name='makale-detay' ),
]

# FUNCTION METHOD BASED VIEWLER
"""
urlpatterns = [
    path('makaleler/', api_views.api_detail_makale_view, name='makale-listesi' ),
    path('makaleler/<int:pk>/', api_views.makale_detail_api_view, name='makale-detay' ),
]
""" 