from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

class RegisterView(CreateView):
    model = User
    template_name = ""
    fields = ["first_name", "last_name", "username", "email", "password"]
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        password_confirm = self.request.POST.get('password_confirm')
        
        if password != password_confirm:
            error_message = "passwords do not match"
            return render(self.request, self.template_name, {'error_message': error_message})
        
        if User.objects.filter(username=username).exists():
            error_message = 'Username already exists'
            return render(self.request, self.template_name, {'error_message': error_message})
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        return super().form_valid(form)
    

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your desired URL
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})