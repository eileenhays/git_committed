from django.urls import path
from . import views as users_views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib import admin


app_name = 'users'
urlpatterns = [
	url(r'^signup/$', users_views.signup, name='signup'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'), #third arg makes it view in same templates dir
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'), # sends user to homepage when logged out
	url(r'^admin/', admin.site.urls),
]