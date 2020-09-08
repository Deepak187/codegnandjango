from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Post, Comment
from django.views.generic.edit import CreateView
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin as logindecorator
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
def Index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


class PostCreate(logindecorator,CreateView):
    model = Post
    fields = ['title', 'description', 'image', ]
    template_name = 'create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required()
def details(request, pk):
    p = Post.objects.get(pk=pk)
    context = {'p': p}
    return render(request, 'detail.html', context)


def details(request, pk):
    p = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post_id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            c = Comment(post_id=pk, comment=comment, user=request.user)
            c.save()
            # return HttpResponseRedirect(reverse('codegnanapp:index'))
            return HttpResponseRedirect(reverse('codegnanapp:details', kwargs={'pk': pk}))

    else:
        form = CommentForm()
    return render(request, 'detail.html', {'form': form, 'p': p, 'comments': comments})


def like(request):
    if request.is_ajax():
        post_id = request.GET.get('post')
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
        data = {'likes': post.likes}
    return JsonResponse(data)
