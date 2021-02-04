from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from .models import Admin, Farmers, Suppliers,Post


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')


def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, f'Your account has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)


@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form

        }

    return render(request, 'update_profile.html', context)
    @login_required(login_url='/accounts/login/')
    def farm(request):
        farms = Farmers.objects.all()
    return render(request, 'farmer.html', {"farms": farms})


@login_required(login_url='/accounts/login/')
def new_farmer(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewFarmerForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.admin = current_user.profile

            image.save()

        return redirect('farmer')

    else:
        form = NewFarmerForm()
    return render(request, 'new_farmer.html', {"form": form})


def edit_farmer(request):
    current_user = request.user
    if request.method == 'POST':
        form = EditFarmerForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            image = form.save(commit=False)
            image.admin = current_user.profile

            image.save()
        return redirect('farmer')

    else:
        form = EditFarmerForm()
    return render(request, 'edit_farmer.html', {'form': form})


@login_required(login_url='/accounts/login/')
def farmer(request, id):
    farmer = Farmers. farm_farmer(id=id)
    return render(request, 'farmer.html', {'farmer': farmer})


@login_required(login_url='/accounts/login/')
def newfarmer(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewFarmerForm(request.POST, request.FILES)
        if form.is_valid():
            farmer = form.save(commit=False)
            farmer.user = current_user

            farmer.save()

        return redirect('farmer')

    else:
        form = NewFarmerForm()
    return render(request, 'newfarmer.html', {"form": form})


@login_required(login_url='/accounts/login/')
def postfarmer(request, id):
    post = Post.farmer_post(id=id)
    return render(request, 'farmerpost.html', {'post': post})


@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user

            post.save()

        return redirect('farmer')

    else:
        form = NewPostForm()
    return render(request, 'post.html', {"form": form})
