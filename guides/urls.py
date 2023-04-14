from django.urls import path
from . import views

urlpatterns = [
    path('', views.GuideListView.as_view(), name='guides_list'),
    path('guides/<int:pk>', views.GuideDetailView.as_view(), name='guide_detail'),
    path('create', views.GuideCreateView.as_view(), name='guide_create'),
    path('guide/<int:pk>/update', views.GuideUpdateView.as_view(), name='guide_update'),
    path('guide/<int:pk>/update', views.GuideDeleteView.as_view(), name='guide_delete'),
]
