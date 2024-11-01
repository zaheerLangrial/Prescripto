from django.urls import path
from .views import CategoryListView, UserListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('doctors/', UserListView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)