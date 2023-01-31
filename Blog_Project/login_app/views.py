from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse, reverse_lazy
from login_app.forms import UserRegisterForm, UserUpdateForm, AvatarForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from login_app.models import Avatar
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('home')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='login.html',
        context={'form': form},
    )

@login_required
def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()  # Esto lo puedo usar porque es un model form
            success_url = reverse('home')
            return redirect(success_url)
    else:  # GET
        form = UserRegisterForm()
    return render(
        request=request,
        template_name='register.html',
        context={'form': form},
    )

def home(request):
    return render(
        request=request,
        template_name='home.html',
    )

def about(request):
    return render(
        request=request,
        template_name='about.html',
    )

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')
    template_name = 'profile_form.html'

    def get_object(self, queryset=None):
        return self.request.user
     

def add_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.save()
            avatar.user = request.user
            form.save()
            return redirect('home')
    else:
        form = AvatarForm()
    return render(request, 'avatar_form.html', {'form': form})

def show_contact(request):
    return render(
        request=request,
        template_name='contact_page.html',
    )

def list_users(request):
    cntxt = {
        'users': User.objects.all()
    }
    return render(
        request=request,
        template_name='list_users.html',
        context=cntxt,
    ) 

def delete_user(request, id):
    user_to_delete = User.objects.get(id=id)
    if request.method == "POST":
        user_to_delete.delete()
        sucess_url = reverse('list_users')
        return redirect(sucess_url)

def index(request):
    return HttpResponseRedirect("home")

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_pass.html', {'form': form})
