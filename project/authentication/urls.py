from django.urls import path, re_path
from rest_framework_simplejwt import views as jwt_views
from .views import (CustomUserCreate, CustomUserList, CustomUserDetail,
                    ObtainTokenPairView)


app_name = "auth"

urlpatterns = [
    path('providers', CustomUserCreate.as_view(), name="providers_create"),
    path('providers/', CustomUserList.as_view(), name="providers_list"),
    path('providers/<int:pk>', CustomUserDetail.as_view(), name="providers_detail"),
    path('token/obtain', ObtainTokenPairView.as_view(), name='token_create'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
