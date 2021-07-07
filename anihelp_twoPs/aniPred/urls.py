from django.urls import path, include
from .views import PredictFormView

app_name='anipred'
urlpatterns = [
    path('',PredictFormView.as_view(),name='predict')
]