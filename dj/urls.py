from django.urls import include, path
from .views import DoctorDetailView
urlpatterns = [
    path("<pk>/", DoctorDetailView.as_view(), name="doctor-detail"),
]
