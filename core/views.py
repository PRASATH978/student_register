from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import StudentRegisterForm, LoginForm
from django.contrib import messages
from .models import User 

def student_register(request):
    form = StudentRegisterForm()
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student registered successfully.')
            return redirect('student_login')
    return render(request, 'core/student_register.html', {'form': form})

def student_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_student:
                login(request, user)
                return redirect('student_dashboard')
            else:
                messages.error(request, "You're not authorized as student.")
    return render(request, 'core/student_login.html', {'form': form})

def admin_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_admin or user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.error(request, "You're not authorized as admin.")

    return render(request, 'core/admin_login.html', {
        'form': form
    })



def user_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'core/home.html')

def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')

def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')



from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and (user.is_admin or user.is_superuser)

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    students = User.objects.filter(is_student=True)
    return render(request, 'core/admin_dashboard.html', {
        'students': students
    })
