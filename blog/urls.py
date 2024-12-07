from django.urls import path
from . import views
from .views import(
    BlogHomePageView,
    PostDetailView
)
from django.urls import path


app_name = 'blog'

urlpatterns = [
    path('', BlogHomePageView.as_view(), name='home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),
]


