from django.shortcuts import render
from django.shortcuts import redirect   

from app.models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()

    return render(request, "app/index.html", {
        "posts": posts
    })


def create(request):
    new_post_data = request.POST
    new_post = Post(
        title = new_post_data['title'],
        text = new_post_data['text'],
    )
    new_post.save()

    return redirect("/")


def delete(request, id):
    post_to_delete = Post.objects.get(id=id)
    post_to_delete.delete()

    return redirect("/")


def edit(request, id):
    post_to_edit = Post.objects.get(id=id)

    if request.method == "GET":
        return render(request, "app/edit.html", {
            "post_to_edit": post_to_edit
        })
    else:
        new_data = request.POST
        post_to_edit.title = new_data['title']
        post_to_edit.text = new_data['text']
        post_to_edit.save()

        return redirect("/")