from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='login'), name='dispatch')
class RegisterView(View):

    def get(self, request):
        user_form = UserCreationForm()
        return render(request, 'register.html', {'user_form': user_form})

    def post(self, request):
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()

            is_superuser = request.POST.get('is_superuser')
            if is_superuser:
                user.is_superuser = True
                user.is_staff = True
                user.save()

            return redirect('tickets_list')
        return render(request, 'register.html', {'user_form': user_form})


class LoginView(View):

    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('tickets_list')
        return render(request, 'login.html', {'login_form': login_form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')
