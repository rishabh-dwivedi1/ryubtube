from django.shortcuts import render, redirect, get_object_or_404
from .models import Video, Comment
from .forms import VideoForm, CommentForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def home(request):

    videos = Video.objects.all().order_by('-views')

    return render(request, 'home.html', {
        'videos': videos
    })


def register_view(request):

    form = RegisterForm()

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    return render(request, 'register.html', {
        'form': form
    })


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect('home')

    return render(request, 'login.html')


def logout_view(request):

    logout(request)

    return redirect('home')


@login_required
def upload_video(request):

    form = VideoForm()

    if request.method == 'POST':

        form = VideoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            video = form.save(commit=False)

            video.user = request.user

            video.save()

            return redirect('dashboard')

    return render(request, 'upload.html', {
        'form': form
    })


@login_required
def dashboard(request):

    videos = Video.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'videos': videos
    })


def watch_video(request, video_id):

    video = get_object_or_404(Video, id=video_id)

    comments = Comment.objects.filter(video=video)

    video.views += 1

    video.save()

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:

            comment = form.save(commit=False)

            comment.user = request.user

            comment.video = video

            comment.save()

            return redirect(
                'watch_video',
                video_id=video.id
            )

    else:

        form = CommentForm()

    return render(request, 'watch.html', {
        'video': video,
        'comments': comments,
        'form': form
    })


def like_video(request, video_id):

    video = get_object_or_404(Video, id=video_id)

    video.likes += 1

    video.save()

    return redirect(
        'watch_video',
        video_id=video.id
    )


def search(request):

    query = request.GET.get('q')

    videos = Video.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )

    return render(request, 'search.html', {
        'videos': videos,
        'query': query
    })