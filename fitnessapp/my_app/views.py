from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Workout
from .forms import ActivityForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def workout_index(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/index.html', {'workouts': workouts})

@login_required
def workout_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    activity_form = ActivityForm()
    return render(request, 'workouts/detail.html', {
        'workout': workout, 'activity_form': activity_form
    })

class WorkoutCreate(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['name', 'image_filename']
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    success_url = '/workouts/'


class WorkoutUpdate(LoginRequiredMixin, UpdateView):
    model = Workout
    fields = ['name', 'image_filename']

class WorkoutDelete(LoginRequiredMixin, DeleteView):
    model = Workout
    success_url = '/workouts/'

@login_required
def add_activity(request, workout_id):
    form = ActivityForm(request.POST)
    if form.is_valid():
        new_activity = form.save(commit=False)
        new_activity.workout_id = workout_id
        new_activity.save()
    return redirect('workout-detail', workout_id=workout_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('workout-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

