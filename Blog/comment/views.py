from django.shortcuts import render

from .forms import CommentForm
from django.shortcuts import redirect
from django.urls import resolve
from urllib.parse import urlparse

def add_comment(request):
    comment_form = CommentForm(request.POST)
    comment_form.instance.author_id = request.user.id
    if comment_form.is_valid():
        comment_form.save()
    else:
        print('form invalid')
    referer = request.META['HTTP_REFERER']
    return redirect(referer)

    #print(comment_form.instance.__dict__)
    # print(referer)
    # url = urlparse(referer)
    # url = resolve(url.path)
    # print("url",url)

def delete_comment(request, pk):
    comment = Comment.objects.filter(pk=pk)
    if comment.exists() and comment[0].author == request.user:
        comment.delete()

    referer = request.META['HTTP_REFERER']
    return redirect(referer)
