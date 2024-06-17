from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddContactForm, UserRegistrationForm
from .models import Contact


def home(request):
    return render(request, 'home.html')


def user_login(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In')
            return redirect('home')
        else:
            messages.success(request, 'There Was An Error Logging in')
            return redirect('home')
    else:
        return render(request, 'home.html', {'contacts': contacts})


def customer_contact(request, pk):
    if request.user.is_authenticated:
        customer_detail = Contact.objects.get(id=pk)
        return render(request, 'contact.html', {'customer_detail': customer_detail})
    else:
        messages.success(request, 'You Must Be Logged In To View')
        return redirect('home')


# User registration view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully registered and logged in')
                return redirect('home')
            else:
                messages.error(request, 'Registration successful but failed to authenticate user')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


# Login view
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'You have been logged in')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid username or password')
#     return render(request, 'login.html')


# Logout view
def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('home')


# Create contact view
def create_contact(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = AddContactForm(request.POST or None)
        if form.is_valid():
            contact = form.save()
            contact.save()
            contact.shared_with.add(request.user)
            messages.success(request, 'Contact created successfully')
            return redirect('home')
    else:
        form = AddContactForm()
    return render(request, 'contact_form.html', {'form': form})
