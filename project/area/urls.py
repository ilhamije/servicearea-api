from django.urls import path, re_path
from rest_framework_simplejwt import views as jwt_views
from .views import (ServiceAreaList, ServiceAreaDetail, ServiceAreaByUser)


app_name = "areas"

urlpatterns = [
    path('', ServiceAreaList.as_view(), name="servicearea_list"),
    path('<int:pk>', ServiceAreaDetail.as_view(), name="servicearea_detail"),
    path('u/<int:user_id>', ServiceAreaByUser.as_view(), name="servicearea_byuser"),
]