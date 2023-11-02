from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment, Tag, Category, Recomment
from .forms import PostForm, CommentForm, RecommentForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

class PostListView(ListView):
    model = Post
    ordering = '-pk'

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

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
    template_name = 'blog/form.html'

    def test_func(self):
        return self.get_object().author == self.request.user
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs = {'pk':self.object.pk})


post_edit = PostUpdateView.as_view()


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        return self.get_object().author == self.request.user

post_delete = PostDeleteView.as_view()


class CategoryListView(ListView):
    model = Post
    template_name = 'blog/category.html'
    context_object_name = 'posts'
    paginate_by = 5
    ordering = '-pk'

    def get_queryset(self):
        # 카테고리 별 검색 기능
        self.category = get_object_or_404(Category, name=self.kwargs['category_name'])
        qc = super().get_queryset().filter(category=self.category)

        q = self.request.GET.get('q', '')
        if q:
            qc = qc.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return qc

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_name"] = self.category.name
        context["categories"] = Category.objects.all()
        return context
    
categoryview = CategoryListView.as_view()


class TagListView(ListView):
    model = Post
    template_name = 'blog/posttag.html'
    context_object_name = 'tagposts'
    paginate_by = 5
    ordering = '-pk'

    def get_queryset(self):
        # 태그 별 검색 기능
        self.tag = get_object_or_404(Tag, name=self.kwargs['tag_name'])
        qt = super().get_queryset().filter(tags__name=self.tag)

        q = self.request.GET.get('q', '')
        if q:
            qt = qt.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return qt

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_name"] = self.tag.name
        context["tags"] = Tag.objects.all()
        return context
    
tagview = TagListView.as_view()


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/form.html'
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs = {'pk':self.object.post.pk})

comment_new = CommentCreateView.as_view()

class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def form_valid(self, form):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.post = comment.post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs = {'pk':self.object.post.pk})
    
comment_edit = CommentUpdateView.as_view()

class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        return self.get_object().author == self.request.user
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs = {'pk':self.object.post.pk})

comment_delete = CommentDeleteView.as_view()

## CBV로 변경 필요
def _404_errorpage(request, pk):
# 삭제된 게시물 접속 시 404 에러페이지 구현
    object = get_object_or_404(Post, pk=pk)
    return render(request, '404.html', {'object':object})


class ReCommentCreateView(LoginRequiredMixin, CreateView):
    model = Recomment
    form_class = RecommentForm
    template_name = 'blog/form.html'
    
    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        # comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        recomment = form.save(commit=False)
        recomment.author = self.request.user
        recomment.post = post
        # recomment.comment = comment
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs = {'pk':self.object.post.pk})
    
create_recomment = ReCommentCreateView.as_view()

