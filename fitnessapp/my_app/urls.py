from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('workouts/', views.workout_index, name='workout-index'),
    path('workouts/<int:workout_id>/', views.workout_detail, name='workout-detail'),
    path('workouts/create/', views.WorkoutCreate.as_view(), name='workout-create'),
    path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workout-update'),
    path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workout-delete'),
    path(
        'workouts/<int:workout_id>/add-activity/', 
        views.add_activity, 
        name='add-activity'
    ),
    path('accounts/signup/', views.signup, name='signup'),
]
