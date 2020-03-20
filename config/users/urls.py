from django.urls import path, include

from .views import ProfileView
from .routers import router

app_name = 'users'
urlpatterns = [
	path('profile/', ProfileView.as_view(), name='profile'),
	path('api/',include(router.urls)),
]