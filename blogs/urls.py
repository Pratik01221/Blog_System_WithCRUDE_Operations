from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),              # ✅ FIRST
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
    path('<slug:slug>/', views.blogs, name='blogs'),           # ✅ LAST
]
