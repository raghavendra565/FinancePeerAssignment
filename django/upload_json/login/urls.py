from django.urls import path

from .views import LoginUser


login_user = LoginUser.as_view({
    'post': 'post',
})

urlpatterns = [
    path('user', login_user, name="login")
]