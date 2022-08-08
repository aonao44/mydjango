from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import SignUpView

app_name = "accounts"

urlpatterns = [

    path('signup', SignUpView.as_view(), name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),
]
