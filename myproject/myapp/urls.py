from django.urls import path
from .views import HomeView, CustomLoginView, profile_view, like_post_view, dislike_post_view, delete_post_view
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile_view, name='profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('delete_post/<int:post_id>/', delete_post_view, name='delete_post'),
    path('like_post/<int:post_id>/', like_post_view, name='like_post'),
    path('dislike_post/<int:post_id>/', dislike_post_view, name='dislike_post'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)