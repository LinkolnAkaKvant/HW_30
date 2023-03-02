from django.urls import path
from rest_framework.routers import SimpleRouter

from ads import views
from ads.views import AdViewSet

router = SimpleRouter()
router.register("", AdViewSet)

urlpatterns = [
    path('cat/', views.CategoryListView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDetailView.as_view()),
    path('<int:pk>/image', views.AdImageView.as_view()),
    path('by_user/', views.AuthorAdDetailView.as_view()),

]

urlpatterns += router.urls
