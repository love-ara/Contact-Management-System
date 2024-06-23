from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddContactForm, UserRegistrationForm
from .models import Contact


def home(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'home.html', {'contacts': contacts})


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
        return render(request, 'login.html', {'contacts': contacts})


def contact_list(request, pk):
    if request.user.is_authenticated:
        contact_detail = Contact.objects.get(id=pk)
        return render(request, 'contact.html', {'contact_detail': contact_detail})
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
        form = AddContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            contact.save()
            messages.success(request, 'Contact created successfully')
            return redirect('home')
    else:
        form = AddContactForm()
    return render(request, 'create_contact.html', {'form': form})


# delete contact
def delete_contact(request, pk):
    if request.user.is_authenticated:
        delete_this = Contact.objects.get(id=pk)
        delete_this.delete()
        messages.success(request, "Contact deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You Must Be Logged In")
        return redirect('home')

    # update contact


# def update_contact(request, pk):
#     if not request.user.is_authenticated:
#         messages.error(request, "You must be logged in to update a contact")
#         return redirect('login')
#
#     contact = get_object_or_404(Contact, id=pk)
#     if request.method == 'POST':
#         form = AddContactForm(request.POST, instance=contact)
#
#         if form.is_valid():
#             Contact.objects.get(pk).delete()
#             form.save()
#             messages.success(request, 'Contact updated successfully')
#             return redirect('home')
#         else:
#             messages.error(request, 'There was an error updating the contact')
#     else:
#         form = AddContactForm(instance=contact)
#     return render(request, 'contact_form.html', {'form': form})


def update_contact(request, pk):
    if request.user.is_authenticated:
        current_contact = Contact.objects.get(id=pk)
        form = AddContactForm(request.POST or None, instance=current_contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact has been updated successfully")
            return redirect("home")
        return render(request, 'update.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged in to Update Contact")
        return redirect('home')


def search_contact(request):
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(phone_number__icontains=search_term)
        )
        context = {'search_results': search_results, 'search_term': search_term}
        return render(request, 'search.html', context)
    else:
        return redirect('home')
