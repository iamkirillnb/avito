from django.urls import path
from .views import LinksView

urlpatterns = [
    path('add/<int:by_number>/', LinksView.as_view()),
    path('stat/', LinksView.as_view()),

]
