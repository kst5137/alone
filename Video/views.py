from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# from Video.forms import VideoForm
from Video.models import Video

from .forms import VideoForm



def upload(request):
    if request.method == "GET":
        videoform = VideoForm()  # 입력칸에 아무것도 없는 상태로 준다
        return render(request, 'video/upload.html',
                      {'form': videoform})
    elif request.method == 'POST':
        videoform = VideoForm(request.POST, request.FILES)
        if videoform.is_valid():
            video = videoform.save()
            video.save()
            return redirect('/Video/list')
        else:
            videoform = VideoForm()
    return render(request, 'Video/upload.html', {'form': videoform})

def ss(request):

    return render(request, 'Video/ss.html')

def posts(request):
    posts = Video.objects.all()  # board table에서 모든 데이터를 다 가져옴

    return render(request, 'video/list.html',
                  {'posts': posts})

def delete(request, bid):
    post = Video.objects.get(Q(id=bid))
    if request.user != post.writer:
        return render(request, 'Video/list.html')
    post.delete()
    return redirect('/Video/list')

def update(request, bid):
    post = Video.objects.get(Q(id=bid))  # 게시글 하나를 가져오는것
    if request.user != post.writer:
        return render(request, 'Video/list.html')
    post.delete()
    if request.method == "GET":
        # boardForm = BoardForm()      #입력칸에 아무것도 없는 상태로 준다
        videoForm = VideoForm(instance=post)  # 입력칸에 아무것도 없는 상태로 준다
        return render(request, 'video/update.html', {'videoForm': videoForm})
    elif request.method == "POST":
        videoForm = VideoForm(request.POST)
        # boardForm에서 사용자가 보내온 데이터를 받느다
        if videoForm.is_valid():  # boardForm안에 값이 유효한다면
            post.title = videoForm.cleaned_data['title']
            post.tag = videoForm.cleaned_data['tag']
            post.file = videoForm.cleaned_data['file']

            post.save()
            # return redirect('/board/read/' + str(bid))
            return redirect('/Video/list')