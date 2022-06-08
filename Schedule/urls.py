from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', views.LessonsDetail.as_view(), name='lessons_detail'),
    path('filter/', views.LessonFilterView.as_view(), name='lesson_filter')
]
