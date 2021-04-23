
from django.contrib import admin
from django.urls import path
from discordlogin import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('oauth2',views.home,name='oauth2'),
    path('oauth2/login',views.discord_login,name='oauth_login'),
    path('oauth2/login/redirect',views.login_redirect, name='login_redirect')
]
