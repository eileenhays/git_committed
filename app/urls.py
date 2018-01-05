from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:user_id>/<int:count_frequency>/<str:period>', views.set_commitment, name='commitment'),
	path('<int:user_id>', views.progress, name='user_progress'),
]