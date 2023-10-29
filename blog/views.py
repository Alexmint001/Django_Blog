from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment, Tag, Category
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required

class PostListView(ListView):
    model = Post
    ordering = '-pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q', '')

        if q:
            queryset = queryset.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return queryset

post_list = PostListView.as_view()


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/form.html'
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)

post_new = PostCreateView.as_view()


class PostDetailView(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        post = Post.objects.get(pk=pk)
        post.view_count += 1
        post.save()
        return super().get_object(queryset)

post_detail = PostDetailView.as_view()


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')
    template_name = 'blog/form.html'

    def test_func(self):
        return self.get_object().author == self.request.user


post_edit = PostUpdateView.as_view()


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        return self.get_object().author == self.request.user

post_delete = PostDeleteView.as_view()



def _404_errorpage(request, pk):
# 삭제된 게시물 접속 시 404 에러페이지 구현
    object = get_object_or_404(Post, pk=pk)
    return render(request, '404.html', {'object':object})


def CategoryView(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    category_posts = Post.objects.filter(category = category)
    categories = Category.objects.all()
    return render(
        request,
        "blog/category.html",
        {
            "category_name": category_name,
            "category_posts": category_posts,
        },
    )