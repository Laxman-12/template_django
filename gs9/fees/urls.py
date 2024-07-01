from django.urls import path
from . import views
urlpatterns = [
    path('feesndj/',views.fees_django),
    path('feespy/',views.fees_python),
]