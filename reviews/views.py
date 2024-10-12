from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(
        request,
        'register.html',
        context=context
    )


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('review_list')
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }

    return render(
        request,
        'login.html',
        context=context
    )


def user_logout(request):
    logout(request)

    return redirect(
        'review_list'
    )


def review_list(request):
    reviews = Review.objects.all().order_by('-pub_date')

    context = {
        'reviews': reviews
    }

    return render(
        request,
        'review_list.html',
        context=context
    )


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()

            return redirect(
                'review_list'
            )
    else:
        form = ReviewForm()

    context = {
        'form': form
    }

    return render(
        request,
        'add_review.html',
        context=context
    )
