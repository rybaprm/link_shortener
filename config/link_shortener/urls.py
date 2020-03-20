from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'link_shortener'

urlpatterns = [
    #path('', views.MainView.as_view()),
	path('', views.LinkShortenerFormView.as_view(), name='maine'),
	path('my_links', views.ShortLinkList.as_view()),
	path('<slug:pk>/update/', views.ShortLinkUpdate.as_view(), name='update'),
	path('<slug:pk>/delete/', views.ShortLinkDelete.as_view(), name='delete'),
	path('<slug:pk>/', views.ShortLinkDetail.as_view(), name='detail'),
]

