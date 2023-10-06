from django.shortcuts import render,redirect
from app2.models import CustomUser
# Create your views here.
def home(request):
    return render(request,'homepage.html',)


def loginuser(request):
    return render(request, 'loginpage.html')


from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser  # Import your CustomUser model
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone = request.POST.get('phone')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')  # Redirect back to the registration page with an error message

        # Check if a user with the same email or username already exists
        if CustomUser.objects.filter(email=email).exists() or CustomUser.objects.filter(username=username).exists():
            messages.error(request, "User with the same email or username already exists.")
            return redirect('register')  # Redirect back to the registration page with an error message

        # Create the user and save it (Note: Password should be hashed in production)
        user = CustomUser.objects.create_user(username=username, email=email, password=password, phone=phone)
        user.save()

        # Log the user in after registration (optional)
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("/homepage.html")

    return render(request, 'registerpage.html')


