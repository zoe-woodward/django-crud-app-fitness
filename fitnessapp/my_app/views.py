from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout
from .forms import ActivityForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def workout_index(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/index.html', {'workouts': workouts})

def workout_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    activity_form = ActivityForm()
    return render(request, 'workouts/detail.html', {
        'workout': workout, 'activity_form': activity_form
    })

class WorkoutCreate(CreateView):
    model = Workout
    fields = '__all__'
    success_url = '/workouts/'


class WorkoutUpdate(UpdateView):
    model = Workout
    fields = '__all__'

class WorkoutDelete(DeleteView):
    model = Workout
    success_url = '/workouts/'

def add_activity(request, workout_id):
    form = ActivityForm(request.POST)
    if form.is_valid():
        new_activity = form.save(commit=False)
        new_activity.workout_id = workout_id
        new_activity.save()
    return redirect('workout-detail', workout_id=workout_id)